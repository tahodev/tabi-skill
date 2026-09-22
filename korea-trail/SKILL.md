---
name: korea-trail
description: 韓国観光公社のトゥルヌビ(Durunubi)APIで、コリアぐるれ道(コリアトゥルレギル)など歩行コースの距離・所要時間・難易度を照会する。無料APIキーが必要。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# korea-trail

韓国観光公社のトゥルヌビ(두루누비)APIで、コリアぐるれ道(코리아둘레길)をはじめとする歩行コースを照会する。2026-09-21 に検証環境から接続し、`courseList` と `routeList` の両方で `SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

データは韓国語。旅行者に伝えるときはエージェントが日本語に訳して渡す。

## キーと公式資料

無料の serviceKey を申請する: https://www.data.go.kr/data/15101974/openapi.do

## 基本の流れ

```bash
curl -s -m 30 "http://apis.data.go.kr/B551011/Durunubi/courseList?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&numOfRows=20"
```

コース名の先頭で路線を識別する(例: ヘパランギル=해파랑길、ソウルトゥルレギル=서울둘레길)。路線単位の一覧は:

```bash
curl -s -m 30 "http://apis.data.go.kr/B551011/Durunubi/routeList?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&numOfRows=50"
```

## レスポンスの読み方

コース item の主な項目: `crsKorNm`(コース名), `crsDstnc`(距離・km), `crsTotlRqrmHour`(所要時間・分), `crsLevel`(難易度 1〜3), `sigun`(自治体), `crsCycle`(循環型かどうか)。旅行者には距離と所要時間、難易度をセットで伝える。

## 注意

山道・海岸道は台風や豪雨で通行止めになる。歩く前に `korea-weather-warning` と `korea-disaster-alert` で警報と災害メッセージを確認する。コースの最新の通行可否は各管理団体の告知が優先。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 空の `items`: `numOfRows` を上げて全件をページングする。キーワード検索はこのサービスにない。
- 項目名は韓国語式(ローマ字化された韓国語)なので、読み違いに注意する。

## English summary

Looks up walking-trail courses (Korea Dulle-gil and others) with distance, duration and difficulty through the official Korea Tourism Organization Durunubi API. Endpoint existence was confirmed by the expected auth error on 2026-09-21; real-key data was not exercised. Data is Korean-only; check closures before hiking.
