---
name: kto-stay-detail
description: 韓国観光公社 TourAPI 4.0 日本語サービスで宿泊施設を検索し、設備・チェックイン時刻などの詳細を調べる。無料APIキーが必要。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# kto-stay-detail

TourAPI 4.0 の日本語サービス(JpnService2)で宿泊施設(contentTypeId=32)を探し、共通詳細と宿泊固有情報を取得する。2026-09-19 に3オペレーションへ検証環境から接続し、`SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

## キーと公式資料

無料の serviceKey を公共データポータルで申請する: https://www.data.go.kr/data/15101578/openapi.do

## 基本の流れ

```bash
BASE="http://apis.data.go.kr/B551011/JpnService2"
COMMON="serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json"

# ソウル(areaCode=1)の宿泊施設
curl -s -m 30 "$BASE/areaBasedList2?$COMMON&areaCode=1&contentTypeId=32&numOfRows=10"

# 検索結果の contentid で共通詳細と宿泊固有詳細
curl -s -m 30 "$BASE/detailCommon2?$COMMON&contentId={CONTENT_ID}"
curl -s -m 30 "$BASE/detailIntro2?$COMMON&contentId={CONTENT_ID}&contentTypeId=32"
```

`areaBasedList2` の `title`, `addr1`, `contentid` から候補を選び、`detailCommon2` の概要・連絡先、`detailIntro2` の `checkintime`, `checkouttime`, `roomcount`, `parkinglodging`, `reservationurl` などを読む。空欄は「情報なし」とし、推測しない。

## 注意

登録情報が古い場合がある。料金・空室・チェックイン条件は宿泊施設の公式サイトで再確認する。予約操作はしない。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 空の `items`: 地域を広げるか、韓国語版(KorService2)も検討する。
- 詳細が空: `contentId` と `contentTypeId=32` を確認する。

## English summary

Searches lodging in Japanese and reads common/accommodation-specific details through official TourAPI JpnService2. The three operations returned the expected authentication error on 2026-09-19; real-key data was not exercised. Read-only; verify rates and availability with the property.
