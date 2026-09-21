---
name: kto-nearby
description: 韓国観光公社 TourAPI 4.0 日本語サービスで、現在地の周辺にある観光スポットを座標と半径で検索する。無料APIキーが必要。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# kto-nearby

TourAPI 4.0 JpnService2 の `locationBasedList2` で、いまいる場所の周辺にある観光地・飲食店・宿を日本語で検索する。2026-09-21 に検証環境から接続し、`SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

## キーと公式資料

無料の serviceKey を申請する: https://www.data.go.kr/data/15101578/openapi.do

## 基本の流れ

```bash
curl -s -m 30 "http://apis.data.go.kr/B551011/JpnService2/locationBasedList2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&mapX=126.9780&mapY=37.5665&radius=1000&numOfRows=20"
```

`mapX` は経度、`mapY` は緯度(例はソウル市庁)。`radius` はメートル(最大20000)。`contentTypeId` で種類を絞れる(12=観光地、14=文化施設、32=宿泊、38=ショッピング、39=飲食店)。

## レスポンスの読み方

各 item の `title`, `addr1`, `dist`(中心からの距離・メートル), `mapx`, `mapy`, `contentid`, `contenttypeid` を読む。`dist` でソートして近い順に提示するとよい。

## 注意

座標は WGS84 系。韓国の地図アプリ(ネイバー等)の座標とずれる場合がある。半径を広げすぎると無関係な施設が混ざる。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 空の `items`: 半径を広げるか `contentTypeId` 指定を外す。
- `mapX` と `mapY` の取り違えに注意(経度が先)。

## English summary

Finds sights, restaurants and lodging near a given coordinate through the official TourAPI JpnService2 locationBasedList2. Endpoint existence was confirmed by the expected auth error on 2026-09-21; real-key data was not exercised. Coordinates are WGS84, longitude first.
