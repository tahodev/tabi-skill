---
name: korea-uv-index
description: 気象庁の生活気象指数APIで、韓国各地の紫外線指数(時間別予測)を照会する。無料APIキーが必要。
license: MIT
metadata:
  category: weather
  locale: ja-JP
---

# korea-uv-index

気象庁(KMA)の生活気象指数 照会サービス(4.0)で、地域別の紫外線指数(자외선지수)を照会する。屋外観光や登山の日に日焼け・熱中症対策の目安として使う。2026-09-21 に検証環境から接続し、`getUVIdxV5` で `SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

## キーと公式資料

無料の serviceKey を申請する: https://www.data.go.kr/data/15085288/openapi.do

## 基本の流れ

`areaNo` は動園予報(동네예보)の地点コード、`time` は `yyyyMMddHH`(例: 06時発表=末尾06):

```bash
TIME=$(date -d 'today' +%Y%m%d06)
curl -s -m 30 "http://apis.data.go.kr/1360000/LivingWthrIdxServiceV5/getUVIdxV5?serviceKey={KEY}&areaNo=1100000000&time=${TIME}&dataType=json"
```

例の `1100000000` はソウル。他地域の地点コードは動園予報の地点一覧から取る。

## レスポンスの読み方

`h0`, `h3`, `h6` ... の3時間ごとの指数値が入る。0-2=弱い、3-5=普通、6-7=強い、8-10=非常に強い、11以上=危険の5段階で旅行者に伝える。

## 注意

発表は1日数回。古い `time` を指定すると空が返るので、その日の最新の発表時刻で取り直す。指数は予測値で、曇り・雨で実感は下がる。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 空の `items`: `time` を直近の発表時刻(06/09/12/15/18時)に合わせて取り直す。
- `areaNo` が不正だと空になる。地点コードの桁欠けに注意する。

## English summary

Reads 3-hourly UV-index forecasts by region through the official KMA living-weather-index API (4.0). Endpoint existence was confirmed by the expected auth error on 2026-09-21; real-key data was not exercised. Use the latest bulletin time of the day; values are forecasts.
