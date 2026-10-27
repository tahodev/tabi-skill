---
name: seoul-subway
description: ソウル地下鉄のリアルタイム到着情報(あと何分で来るか)と、駅別の列車時刻表・始発(첫차)・終電(막차)をソウルオープンデータ広場APIで取得する。日本語駅名の対応表つき。「弘大入口から次の電車は?」「明洞の終電は何時?」に対応。無料APIキーが必要。
license: MIT
metadata:
  category: transit
  locale: ja-JP
---

# seoul-subway

ソウル特別市のオープンAPIで、地下鉄のリアルタイム到着予測を取得するスキル。到着予測API(realtimeStationArrival)と列車位置API(realtimePosition)の両方で、サンプルキーのまま実データが取れることを 2026-09-22 に再実測した(後述の「再現可能な実データ確認例」)。本番利用には無料キーを取得する。

## キーの取得

ソウルオープンデータ広場(서울 열린데이터광장) https://data.seoul.go.kr/ で会員登録し、「서울교통공사 실시간 지하철 도착정보」の活用申請をすると即時に認証キーが発行される(無料)。

## 基本の流れ

1. 駅名を**韓国語表記**にする(APIの入力は韓国語)
2. リアルタイム到着APIを呼ぶ
3. 方面・路線で絞って読む

### 1. 駅名を韓国語にする

日本の旅行者が使う駅名の主な対応(抜粋):

| 日本語 | 韓国語(API入力) | 路線 |
| --- | --- | --- |
| ソウル駅 | 서울역 | 1, 4, 空港鉄道 |
| 明洞 | 명동 | 4 |
| 弘大入口 | 홍대입구 | 2, 空港鉄道, 京義中央 |
| 東大門歴史文化公園 | 동대문역사문화공원 | 2, 4, 5 |
| 江南 | 강남 | 2, 新盆唐 |
| 新沙 | 신사 | 3 |
| 梨泰院 | 이태원 | 6 |
| 仁川空港1ターミナル | 인천공항1터미널 | 空港鉄道 |

主要な観光駅44件の対応表を **`data/stations-ja-ko.csv`** に同梱している(日本語 → API入力用韓国語 → 路線)。表にない駅は、全駅の日本語・中国語・英語対応表であるソウル交通公社の公式データ「역명다국어표기」(公共データポータル 15044232、ファイルデータ)を使う: https://www.data.go.kr/data/15044232/fileData.do

### 2. リアルタイム到着APIを呼ぶ

```bash
# 駅名(홍대입구)はパーセントエンコードして渡す
curl -s "http://swopenapi.seoul.go.kr/api/subway/{SEOUL_KEY}/json/realtimeStationArrival/0/10/%ED%99%8D%EB%8C%80%EC%9E%85%EA%B5%AC"
```

末尾のパス要素が駅名(韓国語)。curlはパスをエンコードしないので、駅名は必ずパーセントエンコードしてからURLに埋め込む。エンコード例:

```bash
STATION=$(printf '%s' "홍대입구" | jq -sRr @uri)   # jq がある場合
# または python3 -c 'import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))' "홍대입구"
curl -s "http://swopenapi.seoul.go.kr/api/subway/{SEOUL_KEY}/json/realtimeStationArrival/0/10/${STATION}"
```

`0/10` は取得範囲(開始/件数)。

### 3. レスポンスの読み方

`realtimeStationArrivalList` 配列の各要素:

- `trainLineNm`: 行き先方面(例: 「성남(신흥)방면」= 城南・新興方面)。韓国語。
- `subwayId`: 路線コード。1001〜1009 が1〜9号線、1065 が空港鉄道(AREX)、1063 が京義中央線。
- `arvlMsg2`: 「3分」「전역 진입」(前の駅に進入)などの到着予測メッセージ。
- `recptnDt`: データ生成時刻。古いデータを最新として答えないよう、一緒に伝える。

同じ駅でも路線・方面ごとに行が分かれる。旅行者には「何番線の、どっち方面か」を必ず添えて答える。

**レスポンス例**: `examples/realtime-station-arrival.sample.json`(構造を再現した記述例。2026-09-10時点ではサンプルキーが `ERROR-336` を返し実測取得できなかった)。

**時刻表APIの実測レスポンス例**(2026-10-28 にサンプルキーで実測取得): `examples/search-info-by-subway-name.sample.json`(駅名→コード)、`examples/search-stn-timetable-by-id.sample.json`(駅時刻表)、`examples/search-last-train-by-id.sample.json`(終電)。

## 再現可能な実データ確認例(2026-09-22 実測)

ソウル交通公社の**列車位置API(realtimePosition)** と**到着予測API(realtimeStationArrival)** は、どちらもサンプルキーで実データを確認できる。サンプルキーは検証用なので、本番利用には無料キーを取得する。

```bash
# 1号線(1호선)の現在走行中の列車位置。サンプルキー `sample` のまま動く
curl -s -m 30 "http://swopenapi.seoul.go.kr/api/subway/sample/json/realtimePosition/0/5/1%ED%98%B8%EC%84%A0"
```

確認できた主要フィールド(2026-09-22 13:58 KST 実測、1号線70編成・2号線36編成):

- `errorMessage.code` が `INFO-000` で正常。`errorMessage.total` が走行中の編成数。
- `subwayNm`: 路線名(「1호선」)。`subwayId`: 1001。
- `statnNm`: 列車がいる駅(例: 종로3가 = 鍾路3街)。
- `trainNo`: 列車番号。`recptnDt`: データ生成時刻(例: 2026-09-22 13:58:46)。
- `updnLine`: 0 = 上り/内回り、1 = 下り/外回り。`trainSttus`: 0 = 進入、1 = 到着、2 = 出発、3 = 前駅出発。

2号線(2호선, `%ED%98%B8%EC%84%A0` 部分を `2호선` に変更)でも同様に実データを確認済み(36編成)。到着予測APIも `realtimeStationArrival/0/5/%EC%84%9C%EC%9A%B8` で `INFO-000`、実到着20件(先頭5件)を確認した。サンプルキーの制限は予告なく変わり得るため、`ERROR-33x` が返る場合は無料キーで再確認する。

失敗の見分け方:

- **空レスポンス(該当データなし)**: HTTP 200 で `INFO-200`。駅名の誤りか未対応路線。
- **認証エラー**: キー不正・サンプルキーの制限時は HTTP 200/500 で `ERROR-33x` 系。実キーの有効性と取得範囲を確認する。
- **海外ランナー制限**: 韓国政府系ホストは海外IPからの接続を遮断することがあり、タイムアウトや接続失敗になる(GitHub Actions の米国リージョンランナーで観測済み)。JSONのエラーコードではなく接続自体の失敗で見分ける。

## 時刻表・始発(첫차)・終電(막차)の照会

リアルタイム到着とは別に、ソウル交通公社の**時刻表API**で駅ごとの列車時刻・始発・終電を調べられる。以下はすべて 2026-10-28 に**サンプルキー `sample` のまま実データを取得確認**した(ホストは `openapi.seoul.go.kr:8088`)。取得した実レスポンスは `examples/` に保存済み。本番利用は無料キー推奨。

### 駅名 → 駅コード(SearchInfoBySubwayNameService)

```bash
# 駅名(서울역)はパーセントエンコード
curl -s -m 30 "http://openapi.seoul.go.kr:8088/{KEY}/json/SearchInfoBySubwayNameService/1/5/%EC%84%9C%EC%9A%B8%EC%97%AD/"
```

行ごとに `STATION_CD`(内部コード)・`FR_CODE`(外部コード)・`LINE_NUM`(호선)が返る。同じ駅名でも路線ごとに行が分かれる(例: ソウル駅は1号線0150/FR_CODE 133、4号線0426/426、空港鉄道4201/A01、京義線1251/P313)。

### 駅の時刻表(SearchSTNTimeTableByIDService / SearchSTNTimeTableByFRCodeService)

```bash
# 駅コード 0150(ソウル駅1号線), 平日, 上り/内回り
curl -s -m 30 "http://openapi.seoul.go.kr:8088/{KEY}/json/SearchSTNTimeTableByIDService/1/5/0150/1/1/"
# FR_CODE でも同じ結果が取れる
curl -s -m 30 "http://openapi.seoul.go.kr:8088/{KEY}/json/SearchSTNTimeTableByFRCodeService/1/5/133/1/1/"
```

- パスの最後の2要素は `WEEK_TAG` / `INOUT_TAG`: 曜日は 1=平日、2=土曜、3=日曜・祝日。方面は 1=上り・内回り、2=下り・外回り。
- 各行の `ARRIVETIME` がその駅への到着時刻。**始発は曜日・方面ごとに最早の行、終電は最遅の行**(後述の終電APIで直接も取れる)。`SUBWAYSNAME` / `SUBWAYENAME` が始発駅・終着駅、`TRAIN_NO` が列車番号。
- 時刻表の行数は多い(ソウル駅1号線・平日・上りで246行)。`開始/件数` で分割して読む。

### 終電だけ直接調べる(SearchLastTrainTimeByIDService)

```bash
curl -s -m 30 "http://openapi.seoul.go.kr:8088/{KEY}/json/SearchLastTrainTimeByIDService/1/5/0150/1/1/"
```

`LEFTTIME` が終電の発車時刻(例: 24:48:00)、`SUBWAYENAME` が行き先。曜日・方面の指定は時刻表APIと同じ。`FR_CODE` 版は `SearchLastTrainTimeByFRCodeService`(実在を `INFO-200` で確認)。

### 時刻表の注意

- 提供範囲は**ソウル交通公社が運行する1〜9号線の駅**(公式の提供範囲案内より)。空港鉄道・新盆唐線など他社局の駅は駅名検索には出ても時刻表が返らないことがある。その場合は「この路線は時刻表APIの対象外の可能性がある」と伝える。
- データは**時刻表(計画値)** で、公式案内にも「実際の列車到着時間と異なる場合がある」とある。当日の遅れはリアルタイム到着APIで見る。

## 注意

- 到着予測はソウル交通公社の提供データそのまま。遅延で狂うことがある。
- 首都圏の一部路線(KORAIL直通など)は対象外のことがある。返ってこなければ「この路線は未対応の可能性がある」と伝える。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **`RESULT.CODE` が `INFO-000` 以外**: `INFO-200` は「該当データなし」= 駅名の誤りか未対応路線。駅名の韓国語表記を見直す(「駅」を付けない: 弘大入口は `홍대입구`、`홍대입구역` ではない)。
- **HTTP 500**: 駅名の文字コードやキー不正のことが多い。まずサンプルキー `sample` で同じリクエストを試して切り分ける。
- **空のrealtimeStationArrivalList**: 終電後など。推測で時刻を言わない。

## English summary

Fetches realtime Seoul subway arrival predictions from the Seoul Open Data Plaza API, and also answers first/last train ("첫차/막차") questions via the timetable services: SearchInfoBySubwayNameService (station name to codes), SearchSTNTimeTableByIDService / SearchSTNTimeTableByFRCodeService (per-station timetable; earliest row = first train) and SearchLastTrainTimeByIDService (last train per direction). All three timetable services returned live rows with the sample key on 2026-10-28 (fixtures in examples/). Timetable coverage is Seoul Metro lines 1-9, and times are scheduled, not realtime - day type (weekday/Saturday/Sunday-holiday) and direction must be quoted. Both realtimeStationArrival and realtimePosition returned live arrival/train-position rows with the sample key (reverified 2026-09-22); get a free instantly-issued key from data.seoul.go.kr for production use. Station names must be in Korean (without the "역" suffix); a Japanese station-name table is included and the full multilingual dataset is on the public data portal (15044232). Always quote the line and direction (`trainLineNm`) and the data timestamp (`recptnDt`).
