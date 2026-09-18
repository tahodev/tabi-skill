---
name: seoul-events
description: ソウル市の文化イベント情報APIで、コンサート・展示・祭りを月やジャンルで検索する。「来月ソウルでやってる祭りある?」「週末の無料イベントは?」に対応。無料APIキー(サンプルキーで即動作確認できる)。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# seoul-events

ソウルオープンデータ広場のソウル文化イベント情報API(culturalEventInfo)で、ソウル市内のコンサート・展示・祭り・公演を検索するスキル。サンプルキーで実データ取得を確認済み。件数は変動する観測値で、2026-09-19時点では日付フィルタ `2026-10` が159件、ジャンル「축제」が1,507件。

ソウル市内に限定される。韓国全国の祭り・イベントは [kto-tour](../kto-tour/SKILL.md)(日本語対応)を使う。

## キーの取得

ソウルオープンデータ広場(data.seoul.go.kr)で利用申請すると即時発行される(無料)。動作確認だけならサンプルキー `sample` がそのまま使える(1〜5件まで)。

## 基本の流れ

### 1. サンプルキーで動作確認(実測済み)

```bash
curl -s -m 30 "http://openapi.seoul.go.kr:8088/sample/json/culturalEventInfo/1/3/"
```

### 2. 月・ジャンル・タイトルで絞る

パスに検索条件を追加できる:`/{KEY}/json/culturalEventInfo/{START}/{END}/{CODENAME}/{TITLE}/{DATE}/`

```bash
# 対象月は実行時に指定する
MONTH=$(date -d "+1 month" +%Y-%m)
curl -s -m 30 "http://openapi.seoul.go.kr:8088/sample/json/culturalEventInfo/1/3/%20/%20/${MONTH}"

# ジャンル「축제」(祭り)で絞る(件数は変動)
curl -s -m 30 "http://openapi.seoul.go.kr:8088/sample/json/culturalEventInfo/1/3/%EC%B6%95%EC%A0%9C"
```

- 空の条件は `%20`(スペース)で埋める。韓国語はURLエンコードする。
- `CODENAME` は部分一致。「콘서트」(コンサート)、「축제」(祭り)、「전시」(展示)などが使える(いずれも実測済み)。「축제-문화/예술」のような厳密な分類名もあるが、`/` を含むので部分一致の短い語で絞るほうが無難。
- `DATE` は `YYYY-MM` 形式で、その月に重なるイベントを返す。`TITLE` はタイトル部分一致。

## 読み方

- `TITLE` / `PLACE` / `GUNAME`: タイトル、会場、区(강남구 など)。
- `DATE`: 「2026-10-31~2026-10-31」形式の期間。`STRTDATE` / `END_DATE` は日時型、`PRO_TIME` は開催時間帯(「12:00~17:00」)。
- `IS_FREE`: 「무료」(無料)/「유료」(有料)。`USE_FEE`: 料金の自由記述(空欄あり)。
- `PLAYER` / `PROGRAM`: 出演者・プログラム(空欄多め)。
- `ORG_LINK` / `HMPG_ADDR`: 主催者ページとソウル文化ポータルの詳細ページ。旅行者には `HMPG_ADDR` を渡すと確実。
- `MAIN_IMG`: ポスター画像URL。`LAT` / `LOT`: 緯度経度。

## 実レスポンス例(2026-09-14 サンプルキーで実測取得、主要フィールドのみ)

```json
{"CODENAME":"축제-문화/예술","GUNAME":"동작구","TITLE":"[동작문화재단] 2026 동작 빵도동 축제","DATE":"2026-10-31~2026-10-31","PLACE":"노량진 축구장","IS_FREE":"무료","PRO_TIME":"12:00~17:00","HMPG_ADDR":"https://culture.seoul.go.kr/culture/culture/cultureEvent/view.do?cultcode=159308&menuNo=200010"}
```

## 注意

- データはソウル市の登録ベース。小さなイベントや会場都合の中止は反映されないことがある。`HMPG_ADDR` の公式ページで最終確認するよう伝える。
- `USE_FEE` は空でも `IS_FREE` が「유료」のことがある(その逆も)。両方見て答える。
- 過去イベントも大量に混ざるので、必ず `DATE` フィルタか `STRTDATE` で期間を絞る。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **`RESULT.CODE` が `INFO-000` 以外**: `INFO-200` は認証エラー(キー未指定・無効)。`ERROR-335` はサンプルキーで5件超を要求した。
- **ヒット0件**: 条件の組み合わせが厳しすぎることが多い。`DATE` だけに戻して広げる。
- イベントの有無・内容を推測で答えない。

## English summary

Searches Seoul city cultural events (concerts, exhibitions, festivals, performances) via the Seoul Open Data Plaza culturalEventInfo API - verified live with the public `sample` key on 2026-09-14 (observed on 2026-09-19: date filter 2026-10 returned 159 matches and genre filter "축제" 1,507). Free instantly-issued key from data.seoul.go.kr; sample key returns up to 5 rows (ERROR-335 beyond). Path filters after start/end are CODENAME (substring), TITLE (substring), DATE (YYYY-MM); pad empty ones with %20. Key fields: TITLE, PLACE, GUNAME, DATE, IS_FREE (무료/유료), USE_FEE, PRO_TIME, HMPG_ADDR (official detail page - give this to travelers), LAT/LOT. Seoul-only; for nationwide festivals use kto-tour. Always date-filter, and never invent events.
