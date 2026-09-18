---
name: korea-hospital
description: 健康保険審査評価院の公式APIで韓国全国の病院・診療所を名称・診療科・現在地周辺から検索する。無料APIキーが必要。
license: MIT
metadata:
  category: health
  locale: ja-JP
---

# korea-hospital

健康保険審査評価院(HIRA)の病院情報サービスで医療機関を検索する。2026-09-19 に検証環境から `getHospBasisList` へ接続し、`SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

公式資料: https://www.data.go.kr/data/15001698/openapi.do

```bash
curl -s -m 30 "https://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList?serviceKey={KEY}&pageNo=1&numOfRows=20&emdongNm=%EB%AA%85%EB%8F%99"

# 現在地周辺(経度xPos・緯度yPos・半径m)
curl -s -m 30 "https://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList?serviceKey={KEY}&pageNo=1&numOfRows=20&xPos={LON}&yPos={LAT}&radius=3000"
```

`yadmNm`, `clCdNm`, `addr`, `telno`, `hospUrl`, `XPos`, `YPos`, `distance` を読む。診療時間・救急受入・日本語対応は別情報なので電話または公式サイトで確認する。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 0件: 半径・地域・診療科条件を広げる。
- 生命に関わる症状は検索を続けず119。対応可否を推測しない。

## English summary

Searches official HIRA hospitals/clinics by area or distance. Endpoint returned the expected auth error on 2026-09-19; real-key data was not exercised. Verify hours, emergency acceptance and language support directly; call 119 for emergencies.
