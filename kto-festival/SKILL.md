---
name: kto-festival
description: 韓国観光公社 TourAPI 4.0 日本語サービスで全国の祭り・イベントを開催日から検索する。無料APIキーが必要。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# kto-festival

TourAPI 4.0 JpnService2 の `searchFestival2` で韓国全国の祭りを日本語で検索する。2026-09-19 に検証環境から接続し、`SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

## キーと公式資料

無料の serviceKey を申請する: https://www.data.go.kr/data/15101578/openapi.do

## 基本の流れ

```bash
START=$(date -d 'today' +%Y%m%d)
curl -s -m 30 "http://apis.data.go.kr/B551011/JpnService2/searchFestival2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&eventStartDate=${START}&numOfRows=20"
```

地域を絞る場合は `areaCode` を加える(1=ソウル、2=仁川、6=釜山、39=済州)。`title`, `addr1`, `eventstartdate`, `eventenddate`, `contentid`, `firstimage` を読み、必要なら `detailCommon2` で概要を取る。

## 注意

開催期間内でも中止・時間変更があり得る。主催者または公式詳細ページで最終確認する。ソウル市内だけをジャンル検索する場合は `seoul-events` も使える。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 空の `items`: 開始日を早めるか地域指定を外す。
- 日付は `YYYYMMDD`。過去の固定日をそのまま使わない。

## English summary

Searches nationwide Korean festivals by start date through official TourAPI JpnService2. Endpoint existence was confirmed by the expected auth error on 2026-09-19; real-key data was not exercised. Always verify cancellations and hours with the organizer.
