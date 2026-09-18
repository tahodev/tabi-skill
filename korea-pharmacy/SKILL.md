---
name: korea-pharmacy
description: 健康保険審査評価院の公式APIで韓国全国の薬局を名称・地域・現在地周辺から検索する。無料APIキーが必要。
license: MIT
metadata:
  category: health
  locale: ja-JP
---

# korea-pharmacy

健康保険審査評価院(HIRA)の薬局情報サービスで薬局名・住所・電話番号を検索する。2026-09-19 に検証環境から公式オペレーションへ接続し、`SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

公式資料: https://www.data.go.kr/data/15001673/openapi.do

```bash
curl -s -m 30 "https://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList?serviceKey={KEY}&pageNo=1&numOfRows=20&emdongNm=%EB%AA%85%EB%8F%99"

# 現在地周辺(経度xPos・緯度yPos・半径m)
curl -s -m 30 "https://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList?serviceKey={KEY}&pageNo=1&numOfRows=20&xPos={LON}&yPos={LAT}&radius=2000"
```

`yadmNm`(薬局名), `addr`, `telno`, `XPos`, `YPos`, `distance` を読む。営業時間・当番薬局のリアルタイム保証ではないため、急ぎなら電話で営業中か確認する。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 0件: 地域名を広げるか半径を増やす。
- 緊急時は薬局検索ではなく119を案内する。旧1339は使わない。

## English summary

Searches official HIRA pharmacy records by area/name or coordinates. Endpoint returned the expected auth error on 2026-09-19; real-key data was not exercised. Call to confirm opening hours; use 119 for emergencies.
