---
name: korea-weather
description: 韓国気象庁(KMA)の公共データ短期予報APIで、ソウル・釜山・済州など韓国各地の天気予報を取得する。「明日のソウルの天気は?」に対応。無料APIキーが必要。
license: MIT
metadata:
  category: weather
  locale: ja-JP
---

# korea-weather

韓国の気象庁(기상청, KMA)が公共データポータルで提供する短期予報API(단기예보)を使うスキル。2026-09-09 に2オペレーションの実在を確認済み。

## キーの取得

公共データポータル(data.go.kr)で「기상청 단기예보」(VilageFcstInfoService)に活用申請し、serviceKey を取得する(無料)。ポータル: https://www.data.go.kr/ 、気象庁: https://www.kma.go.kr/

## 基本の流れ

1. 場所の格子座標(nx, ny)を決める
2. 発表時刻(base_date, base_time)を決める
3. 予報を取得して項目を読む

### 1. 格子座標

気象庁は予報を5km格子で出す。主な観光地:

| 場所 | nx | ny |
| --- | --- | --- |
| ソウル(鍾路) | 60 | 127 |
| 釜山 | 98 | 76 |
| 済州 | 52 | 38 |

その他の地点は気象庁が配布する格子座標表で確認する。

### 2・3. 取得と読み方

```bash
# 超短期実況(現在に近い値)
curl -s "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={KEY}&pageNo=1&numOfRows=20&dataType=JSON&base_date=20260909&base_time=0800&nx=60&ny=127"

# 短期予報(3日先まで)
curl -s "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={KEY}&pageNo=1&numOfRows=100&dataType=JSON&base_date=20260909&base_time=0800&nx=60&ny=127"
```

- `base_time`: 発表時刻。短期予報は 0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300 の1日8回。発表直後はまだデータがなく、**発表時刻の10分後以降**に照会する。直近の発表を使うこと。
- レスポンスの `body.items.item[]`: 各要素は `category`(項目), `fcstDate`/`fcstTime`(予報対象時刻), `fcstValue`(値)。
- 主なcategory:
  - `TMP`/`T1H`: 気温(℃)
  - `POP`: 降水確率(%)
  - `SKY`: 空模様(1=晴れ, 3=曇りがち, 4=曇り)
  - `PTY`: 降水形態(0=なし, 1=雨, 2=雨/雪, 3=雪, 5=にわか雨, 6=にわか雨/雪, 7=にわか雪)
  - `REH`: 湿度(%), `WSD`: 風速(m/s)
- `resultCode` が `00` なら成功。

## 注意

- 韓国の気象データの利用は気象庁の提供データそのまま。発表時刻を一緒に伝える。
- 台風・豪雨の判断には必ず気象庁の発表(特報)を確認するよう旅行者に伝える。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **`SERVICE_KEY_IS_NULL` / 認証エラー**: serviceKey 未指定・不正。
- **`NO_DATA`**: base_time がまだ発表前、または未来すぎる日付。直近の発表時刻に変える。
- **空のitems**: 座標ミスの可能性。ソウル 60/127 で動作確認して切り分ける。
- 値を推測で作らない。

## English summary

Fetches Korean weather forecasts from the KMA public-data short-term forecast API (2 operations verified live on 2026-09-09). Free data.go.kr serviceKey required. Forecasts are on a 5km grid (Seoul 60/127, Busan 98/76, Jeju 52/38); base times are 8x/day and data appears ~10 minutes after issue. Read categories TMP/POP/SKY/PTY per forecast time. Never invent values.
