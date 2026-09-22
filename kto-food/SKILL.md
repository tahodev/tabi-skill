---
name: kto-food
description: 韓国観光公社 TourAPI 4.0 日本語サービスで、韓国各地の飲食店を地域やキーワードから日本語で検索する。無料APIキーが必要。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# kto-food

TourAPI 4.0 JpnService2 で飲食店(コンテンツ種別39)を検索する。2026-09-21 に検証環境から接続し、`areaBasedList2`(地域検索)と `searchKeyword2`(キーワード検索)の両方で `SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

## キーと公式資料

無料の serviceKey を申請する: https://www.data.go.kr/data/15101578/openapi.do

## 基本の流れ

地域から探す(例はソウル=areaCode 1):

```bash
curl -s -m 30 "http://apis.data.go.kr/B551011/JpnService2/areaBasedList2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&contentTypeId=39&areaCode=1&numOfRows=20"
```

キーワードで探す(日本語キーワードはURLエンコードする):

```bash
curl -s -m 30 "http://apis.data.go.kr/B551011/JpnService2/searchKeyword2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&contentTypeId=39&keyword=%E3%82%AB%E3%83%A0%E3%82%BF%E3%83%B3"
```

## レスポンスの読み方

各 item の `title`, `addr1`, `contentid`, `firstimage`, `mapx`, `mapy` を読む。メニューや営業時間が必要なら `contentid` で `detailIntro2` を呼ぶ。`areaCode` の一覧は `areaCode2` で取れる(1=ソウル、2=仁川、6=釜山、39=済州)。

## 注意

観光公社の登録店舗が母集団なので、街のすべての店を網羅するわけではない。営業時間・定休日は変わりやすい。行く前に店の公式情報で最終確認する。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 空の `items`: キーワードを短くするか地域指定を外す。日本語以外のキーワードはヒットしないことがある。
- 生の日本語キーワードをURLに直接入れない(パーセントエンコード必須)。

## English summary

Searches Korean restaurants (content type 39) by region or keyword through the official TourAPI Japanese service. Endpoint existence was confirmed by the expected auth error on 2026-09-21; real-key data was not exercised. Coverage is limited to venues registered with the tourism organization.
