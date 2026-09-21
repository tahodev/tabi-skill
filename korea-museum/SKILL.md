---
name: korea-museum
description: 行政安全部の全国博物館美術館情報標準データAPIで、所在地・開館時間・休館日・料金などを照会する。無料APIキーが必要。韓国語データ。
license: MIT
metadata:
  category: museum
  locale: ja-JP
---

# korea-museum

行政安全部の全国博物館美術館情報標準データAPIで、所在地・開館時間・休館日・料金などを照会する。2026-09-21 に検証環境から操作パスへ接続し、キーなしで `SERVICE_KEY_IS_NULL` が返ることを確認した。これは操作の存在確認であり、実キーによる実データ取得は未検証。

全国標準データは自治体から集約される韓国語データ。旅行者へ渡すときは必要な項目だけ日本語に訳す。

## キーと公式資料

無料の serviceKey を公共データポータルで申請する: https://www.data.go.kr/data/15017323/standard.do

## 基本の流れ

```bash
curl -s -m 30 "https://api.data.go.kr/openapi/tn_pubr_public_museum_artgr_info_api?serviceKey={KEY}&pageNo=1&numOfRows=100&type=json"
```

`pageNo` と `numOfRows` でページングし、返却フィールドの施設名・道路名住所・緯度経度を使って滞在地周辺を絞る。標準データの列は提供自治体によって空欄があり得るため、値のない項目を推測しない。

## 使い方

1. 市道・区名または座標で候補を絞る。
2. 名称、住所、営業時間や料金など返却された実用項目を整理する。
3. 営業・開催・利用条件は現地公式情報で最終確認する。

## 注意

全国標準データは更新時点が自治体ごとに異なる。緊急性のある情報や当日の営業状況には使わず、施設・主催者の公式案内を優先する。位置情報がない行は住所で照合する。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定。
- `SERVICE_KEY_IS_NOT_REGISTERED_ERROR`: 当該APIへの利用申請またはキー反映を確認する。
- `NO_OPENAPI_SERVICE_ERROR`: 操作パスが廃止・変更された可能性がある。公共データポータルの仕様を再確認し、別操作名を推測しない。
- 空の `items`: ページ番号と検索条件を戻し、全件取得後にローカルで絞る。

## English summary

全国博物館美術館情報標準データapiで、所在地・開館時間・休館日・料金などを照会 through Korea's official nationwide standard-data API. The operation returned the expected missing-key error on 2026-09-21; real-key rows were not tested. Data is Korean and may be stale or incomplete by municipality, so confirm time-sensitive details with the venue or organizer.
