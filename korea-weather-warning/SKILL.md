---
name: korea-weather-warning
description: 韓国気象庁(KMA)の気象特報APIで、発表中の注意報・警報(豪雨・強風・大雪・台風など)と通報文を照会する。「いま韓国で警報が出ている?」に対応。無料APIキーが必要。
license: MIT
metadata:
  category: weather
  locale: ja-JP
---

# korea-weather-warning

気象庁(기상청, KMA)の気象特報照会サービス(WthrWrnInfoService)で、発表中の気象注意報(주의보)・警報(경보)を取得するスキル。2026-09-10 に2オペレーションの**エンドポイント実在**を確認済み(キーなしで叩き、404ではなく認証エラーが返ることを確認。実キーでのデータ応答はまだ未検証)。予報そのものは [korea-weather](../korea-weather/SKILL.md) スキル参照。

## キーの取得

公共データポータル(data.go.kr)で「기상청 기상특보 조회서비스」(WthrWrnInfoService)に活用申請し、serviceKey を取得する(無料)。ポータル: https://www.data.go.kr/ 、気象庁: https://www.kma.go.kr/

## 基本の流れ

1. 発表中の特報リストを取る
2. 気になる特報の通報文(상세 내용)を取る

### 1. 特報リスト(getWthrWrnList)

```bash
curl -s "http://apis.data.go.kr/1360000/WthrWrnInfoService/getWthrWrnList?serviceKey={KEY}&pageNo=1&numOfRows=20&dataType=JSON"
```

- 気象庁の活用ガイド上の絞り込みパラメータ: `stnId`(発表庁の地点コード), `fromTmFc` / `toTmFc`(発表時刻の範囲・YYYYMMDDHHMM)。
- レスポンスの `body.items.item[]`: 各要素は `stnId`(発表庁コード), `title`(例: 「호우주의보 : 전라남도 ...」= 豪雨注意報: 全羅南道...), `tmFc`(発表時刻), `tmSeq`(通報番号)。

### 2. 通報文(getWthrWrnMsg)

```bash
curl -s "http://apis.data.go.kr/1360000/WthrWrnInfoService/getWthrWrnMsg?serviceKey={KEY}&dataType=JSON&stnId={STN_ID}&tmSeq={TM_SEQ}"
```

- `stnId` / `tmSeq` はリストの該当行から取る。特報の対象地域・期間・内容の全文が返る(韓国語)。

## 特報の種類(読み方の基礎)

- 注意報(주의보)より警報(경보)のほうが強い。
- 主な種類: 호우(豪雨), 강풍(強風), 대설(大雪), 태풍(台風), 폭염(猛暑), 한파(寒波), 황사(黄砂), 풍랑(風浪)。

## 注意

- 特報は発表庁(ソウル・釜山などの地方気象庁)ごとに出る。タイトルに対象地域が入るので、そのまま旅行者に伝える。
- 台風・豪雨シーズンの移動前チェックに使う。最終判断は気象庁の公式発表(kma.go.kr)で確認するよう伝える。
- パラメータの詳細は気象庁の活用ガイドが正本。このスキルはエンドポイント実在の確認済みだが、実キーでの応答検証はまだ(2026-09-10時点)。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **HTTP 401 `SERVICE_KEY_IS_NULL` / 認証エラー**: serviceKey 未指定・不正。
- **`NO_OPENAPI_SERVICE_ERROR`**: サービス名のミス。ベースは `apis.data.go.kr/1360000/WthrWrnInfoService`。
- **`NO_DATA` / 空のitems**: 発表中の特報がない、または期間・地点の条件ミス。条件を広げる。「特報なし」は正常な答え。
- 発表内容を推測で補わない。

## レスポンス例

`examples/getWthrWrnList.sample.json`(構造を再現した記述例。実キーでの実測取得ではない)。

## English summary

Fetches active Korean weather advisories (주의보) and warnings (경보) from the KMA weather-warning API (WthrWrnInfoService) - endpoint existence verified on 2026-09-10 (unauthenticated probes return auth errors, not 404; not yet exercised with a real key). Free data.go.kr serviceKey required. List current warnings with getWthrWrnList, then pull the full bulletin with getWthrWrnMsg using stnId/tmSeq from the list. Warning types include heavy rain, strong wind, heavy snow, typhoon, heat wave, cold wave, yellow dust. Never invent warning content.
