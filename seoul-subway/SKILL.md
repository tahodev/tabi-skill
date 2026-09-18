---
name: seoul-subway
description: ソウル地下鉄のリアルタイム到着情報(あと何分で来るか)をソウルオープンデータ広場APIで取得する。日本語駅名の対応表つき。「弘大入口から次の電車は?」のような質問に対応。無料APIキーが必要。
license: MIT
metadata:
  category: transit
  locale: ja-JP
---

# seoul-subway

ソウル特別市のオープンAPIで、地下鉄のリアルタイム到着予測を取得するスキル。2026-09-19 再検証ではサンプルキーのHTTP応答は得られたが、APIレベルは `INFO-200`(該当データなし)で、実到着データは未取得。

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

## 注意

- 到着予測はソウル交通公社の提供データそのまま。遅延で狂うことがある。
- 首都圏の一部路線(KORAIL直通など)は対象外のことがある。返ってこなければ「この路線は未対応の可能性がある」と伝える。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **`RESULT.CODE` が `INFO-000` 以外**: `INFO-200` は「該当データなし」= 駅名の誤りか未対応路線。駅名の韓国語表記を見直す(「駅」を付けない: 弘大入口は `홍대입구`、`홍대입구역` ではない)。
- **HTTP 500**: 駅名の文字コードやキー不正のことが多い。まずサンプルキー `sample` で同じリクエストを試して切り分ける。
- **空のrealtimeStationArrivalList**: 終電後など。推測で時刻を言わない。

## English summary

Fetches realtime Seoul subway arrival predictions from the Seoul Open Data Plaza API (HTTP response rechecked on 2026-09-19, but no real arrival row was obtained with the sample key). Needs a free instantly-issued key from data.seoul.go.kr. Station names must be in Korean (without the "역" suffix); a Japanese station-name table is included and the full multilingual dataset is on the public data portal (15044232). Always quote the line and direction (`trainLineNm`) and the data timestamp (`recptnDt`).
