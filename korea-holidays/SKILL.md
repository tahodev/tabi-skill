---
name: korea-holidays
description: 韓国天文研究院(KASI)の特日情報APIで、韓国の祝日・記念日を照会する。「来月の旅行、祝日と重なる?」「秋夕(チュソク)っていつ?」に対応。旧暦ベースの連休の正確な日付が取れる。無料APIキーが必要。
license: MIT
metadata:
  category: basics
  locale: ja-JP
---

# korea-holidays

韓国天文研究院(한국천문연구원, KASI)の特日情報提供サービス(SpcdeInfoService)で、韓国の祝日(공휴일)・国慶日(국경일)・記念日(기념일)を年月指定で照会するスキル。2026-09-14 に3オペレーションの**エンドポイント実在**を確認済み(キーなしで叩き、404ではなく認証エラー `SERVICE_KEY_IS_NULL` が返ることを確認。実キーでのデータ応答はまだ未検証)。

祝日は交通(KTXの帰省ラッシュ)・観光地の混雑・宮殿や博物館の開休館に直結する。旧暦ベースのソルラル(설날)と秋夕(추석)は毎年日付が変わるので、推測で答えずこのAPIで取る。

## キーの取得

公共データポータル(data.go.kr)で「한국천문연구원 특일 정보제공 서비스」(SpcdeInfoService)に活用申請し、serviceKey を取得する(無料)。ポータル: https://www.data.go.kr/

## 基本の流れ

年月を決めて、該当月の特日リストを取るだけのシンプルな照会。

### 1. 祝日・国慶日(getRestDeInfo)

```bash
curl -s "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo?serviceKey={KEY}&solYear=2026&solMonth=10&_type=json&numOfRows=50"
```

- `solYear` は4桁の年、`solMonth` は2桁の月(01〜12)。月をまたぐ連休(秋夕など)は各日が別レコードで返る。
- レスポンスの `body.items.item[]`: 各要素は `dateName`(例: 「추석」= 秋夕)、`locdate`(YYYYMMDD)、`isHoliday`(Y/N)。
- 代替休日(대체공휴일)は「대체공휴일(...)」という名前の行で出る。

### 2. 記念日(getAnniversaryInfo)

```bash
curl -s "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getAnniversaryInfo?serviceKey={KEY}&solYear=2026&solMonth=03&_type=json&numOfRows=50"
```

- 「삼일절」(三・一節)のような国の記念日が返る。`getHoliDeInfo`(공휴일のみ)も同じパラメータで使える。

## 注意

- `locdate` と `dateName` をセットで伝える。韓国語の祝日名には日本語読みを添える(추석 = 秋夕、설날 = 旧正月、광복절 = 光復節、개천절 = 開天節)。
- 祝日期間中のKTX・高速バスは早めに満席になる。kr-train / kr-bus スキルと組み合わせて案内する。
- 宮殿・博物館の祝日開館・無料開放は年度ごとの告知なので、このAPIの結果だけで断言しない。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **HTTP 401 `SERVICE_KEY_IS_NULL` / 認証エラー**: serviceKey 未指定・不正。
- **`NO_OPENAPI_SERVICE_ERROR`**: サービス名のミス。ベースは `apis.data.go.kr/B090041/openapi/service/SpcdeInfoService`。
- **`NO_DATA` / 空のitems**: その月に該当する特日がないだけ。異常ではない。
- 日付を推測で補わない(旧暦連休は年ごとに変わる)。

## レスポンス例(構造)

```json
{"response":{"body":{"items":{"item":[{"dateName":"추석","locdate":20261004,"isHoliday":"Y"}]},"totalCount":3}}}
```

## English summary

Looks up Korean public holidays, national days, and anniversaries from the Korea Astronomy and Space Science Institute (KASI) SpcdeInfoService - endpoint existence verified on 2026-09-14 (unauthenticated probes return SERVICE_KEY_IS_NULL auth errors, not 404; not yet exercised with a real key). Free data.go.kr serviceKey required. Query by solYear/solMonth with getRestDeInfo (holidays incl. Seollal/Chuseok), getHoliDeInfo, or getAnniversaryInfo. Lunar-calendar holidays move every year - never guess the dates; read locdate + dateName from the response.
