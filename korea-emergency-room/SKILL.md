---
name: korea-emergency-room
description: 国立中央医療院(E-Gen)の公式APIで全国の救急医療機関・救急室のリアルタイム空き病床・重症疾患の収容可能情報を照会する。「近くで空いている救急室は?」の参考情報に。無料APIキーが必要。実際の受入可否は119・救急室への電話確認が必須。
license: MIT
metadata:
  category: health
  locale: ja-JP
---

# korea-emergency-room

国立中央医療院(국립중앙의료원、E-Gen)の「全国救急医療機関情報照会サービス」で、救急医療機関の一覧・救急室のリアルタイム空き病床・重症疾患ごとの収容可能情報を照会するスキル。2026-10-28 に4オペレーションの実在を `SERVICE_KEY_IS_NULL` で確認した。実キーでの実データ取得は未検証。

公式資料: https://www.data.go.kr/data/15000563/openapi.do (公共データポータルで活用申請すると無料キー発行)

## 重要な前提(必ず旅行者に添える)

- このAPIは**参考情報**。病床や収容可能情報は各機関の申告データで、**実際の受け入れを保証しない**。
- **緊急時は検索せず119**(救急・消防、通訳サポートあり)。日本語の相談は1330(07:00〜24:00 KST)。
- 「空き病床あり」の表示があっても、症状・診療科・時間帯で断られることがある。搬送前に**救急室へ電話確認**するよう必ず添える。

## オペレーション

```bash
# 救急医療機関の一覧(地域で絞る)
curl -s -m 30 "https://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytListInfoInqire?serviceKey={KEY}"

# 救急室のリアルタイム空き病床(地域で絞る)
curl -s -m 30 "https://apis.data.go.kr/B552657/ErmctInfoInqireService/getEmrrmRltmUsefulSckbdInfoInqire?serviceKey={KEY}"

# 重症疾患の収容可能情報
curl -s -m 30 "https://apis.data.go.kr/B552657/ErmctInfoInqireService/getSrsillDissAceptncPosblInfoInqire?serviceKey={KEY}"

# 現在地(緯度・経度)周辺の救急医療機関
curl -s -m 30 "https://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytLcinfoInqire?serviceKey={KEY}"
```

共通パラメータは公式の活用ガイド(data.go.kr の上記ページ)に従う。主なもの: `pageNo` / `numOfRows`、地域絞り込みの `STAGE1`(시도)・`STAGE2`(시군구)、位置検索の `WGS84_LAT` / `WGS84_LON`。2026-10-28 は認証エラーでの実在確認までで、実キーでの応答フィールドは未確認のため、詳細なパラメータ名・フィールド名は公式ガイドを参照する。

公式説明にある提供情報(2026-10-28 照合): 診療日・診療科目・救急医療機関分類・代表電話・救急室電話・リアルタイム空き病床(救急室・手術室・胸部集中治療室・一般集中治療室・入院室など)・重症疾患(脳梗塞の再灌流・腹部損傷の手術・救急内視鏡など)の収容可能情報・位置情報。

## レスポンスの読み方(実キー利用時)

- 空き病床は 0 や負数(満床・超過)になることがある。0以下は「現在満床の表示」として伝え、推測で空きを言わない。
- データの生成時刻があれば必ず一緒に伝える。古い情報を現在の空きとして答えない。
- 重症疾患の「収容可能」表示は**設備・体制の情報**であり、その時点の受入確約ではない。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL` / `returnReasonCode 20`: キー未指定・無効、または活用申請未完了。
- `NO_OPENAPI_SERVICE_ERROR` (12): オペレーション名の誤り。
- 0件: 地域コード(STAGE1/STAGE2)の表記を見直す。
- **生命に関わる状況では検索を続けず119に電話**。受入可否をこのAPIだけで判断しない。

## English summary

Queries Korea's official emergency-care API (National Medical Center / E-Gen) for emergency medical institutions, realtime ER bed availability, and severe-condition capability info. Four operations (list, realtime beds, severe-condition capability, location-based search) returned the expected SERVICE_KEY_IS_NULL auth error on 2026-10-28; real-key responses were not exercised, so parameter and field details defer to the official guide. This is reference data only and never a guarantee of acceptance: in an emergency call 119, for Japanese-language help call 1330, and always confirm with the ER by phone before transport.
