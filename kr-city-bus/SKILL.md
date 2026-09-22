---
name: kr-city-bus
description: 国土交通部TAGOのバス到着情報APIで、地方都市の市内バスの停留所別リアルタイム到着予測を照会する。無料APIキーが必要。
license: MIT
metadata:
  category: transit
  locale: ja-JP
---

# kr-city-bus

国土交通部TAGOのバス情報APIで、市内バス(시내버스)の停留所別の到着予測を照会する。2026-09-21 に検証環境から接続し、`getCtyCodeList`(都市コード), `getSttnNoList`(停留所検索), `getSttnAcctoArvlPrearngeInfoList`(到着予測)の各オペレーションで `SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

## キーと公式資料

無料の serviceKey を申請する: https://www.data.go.kr/data/15098530/openapi.do

## 基本の流れ

1. 対応都市のコードを取る:

```bash
curl -s -m 30 "http://apis.data.go.kr/1613000/ArvlInfoInqireService/getCtyCodeList?serviceKey={KEY}&_type=json"
```

2. 停留所名(韓国語)から停留所IDを探す(例は大田の停留所名検索。名前はURLエンコード):

```bash
curl -s -m 30 "http://apis.data.go.kr/1613000/BusSttnInfoInqireService/getSttnNoList?serviceKey={KEY}&cityCode=25&nodeNm={STATION_NAME}&_type=json"
```

3. 停留所ID(`nodeId`)で到着予測を取る:

```bash
curl -s -m 30 "http://apis.data.go.kr/1613000/ArvlInfoInqireService/getSttnAcctoArvlPrearngeInfoList?serviceKey={KEY}&cityCode=25&nodeId={NODE_ID}&_type=json"
```

## レスポンスの読み方

到着予測 item の `routeno`(路線番号), `arrprevstationcnt`(あと何駅か), `arrtime`(到着までの秒数)を読む。路線番号から路線の起終点を確認したいときは `BusRouteInfoInqireService/getRouteNoList` で路線IDを引ける(2026-09-21 オペレーション実在確認)。

## 注意

対応都市はバス情報システム(BIS)導入自治体に限られ、都市ごとに更新精度が違う。ソウル市内のバスはこのサービスの対象外。大都市間の移動は `kr-bus`(高速バス)と `kr-intercity-bus`(市外バス)を使う。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 空の `items`: `cityCode` が対応都市か確認する。`getCtyCodeList` の戻りと照合する。
- `nodeNm` は韓国語の停留所名をパーセントエンコードして渡す。日本語名ではヒットしない。

## English summary

Realtime city-bus arrival predictions for Korean regional cities via the official TAGO bus APIs (city codes, stop search, arrival forecasts). Endpoint existence was confirmed by the expected auth error on 2026-09-21; real-key data was not exercised. Seoul city buses are out of scope.
