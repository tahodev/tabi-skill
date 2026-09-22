---
name: kto-course
description: 韓国観光公社 TourAPI 4.0 日本語サービスで、おすすめ旅行コース(モデルコース)を地域から日本語で検索する。無料APIキーが必要。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# kto-course

TourAPI 4.0 JpnService2 の `areaBasedList2` で旅行コース(コンテンツ種別25)を検索する。2026-09-21 に検証環境から接続し、`SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

## キーと公式資料

無料の serviceKey を申請する: https://www.data.go.kr/data/15101578/openapi.do

## 基本の流れ

```bash
curl -s -m 30 "http://apis.data.go.kr/B551011/JpnService2/areaBasedList2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&contentTypeId=25&areaCode=1&numOfRows=20"
```

`areaCode` を外せば全国対象になる(1=ソウル、2=仁川、6=釜山、39=済州)。

## レスポンスの読み方

各 item の `title`, `addr1`, `contentid`, `firstimage` を読む。コースの概要は `detailCommon2`、コース内の各スポット(サブコース)は `detailInfo2` を `contentid` で呼んで取る。

## 注意

コースは観光公社の推奨ルートであり、移動時間や営業状況は含まれない。組み込む前に各スポットの現況を別途確認する。日帰りか宿泊かの目安は概要文を参照。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 空の `items`: 地域指定を外して全国で試す。コース登録が少ない地域がある。

## English summary

Finds recommended travel courses (content type 25) by region through the official TourAPI Japanese service. Endpoint existence was confirmed by the expected auth error on 2026-09-21; real-key data was not exercised. Verify each stop's current status separately.
