---
name: krw-jpy-rate
description: ウォン(KRW)と円(JPY)の為替レートを調べる。韓国輸出入銀行(한국수출입은행)の無料APIと韓国銀行ECOS APIの2ソース対応。「いま1万ウォンは何円?」「両替はどっちが得?」のような質問に対応。無料APIキーが必要。
license: MIT
metadata:
  category: finance
  locale: ja-JP
---

# krw-jpy-rate

ウォン・円の為替レートを、韓国の公式な無料APIから取得するスキル。2つの独立ソースを持ち、片方が落ちても代替できる。

- ソースA: 韓国輸出入銀行(KEXIM) 現在環율API — 旅行・両替の実務で標準的に使われる。JPY(100)を直接返す。
- ソースB: 韓国銀行(BOK) ECOS API — 国家の公式統計。2026-09-09 にサンプルキーで実データ取得を実測確認(원/엔(100엔) 매매기준율 871.54)。

どちらも無料キーが必要。発行はどちらも即時・無料。

## キーの取得

- **KEXIM**: 韓国輸出入銀行サイトで会員登録後、オープンAPI認証キーを即時発行。公共データポータルにも登録済み: https://www.data.go.kr/data/3068846/openapi.do
- **ECOS**: https://ecos.bok.or.kr/ で会員登録後、オープンAPI認証キーを即時発行。

## ソースA: KEXIM 現在환율API

```bash
curl -s "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={KEXIM_KEY}&searchdate=${RATE_DATE}&data=AP01"
```

- `searchdate`: 調べたい日付(YYYYMMDD)。当日11時前は前営業日のデータになる。土日・韓国の祝日はデータなし(直前営業日を指定する)。
- `data=AP01`: 現在환율(全通貨)。
- レスポンスは配列。JPYの行は `cur_unit` が `"JPY(100)"`(100円あたりのウォン)。
  - `deal_bas_r`: 매매기준율(仲値)。「1万ウォンは何円?」の概算にはこれを使う。
  - `ttb` / `tts`: 電信買相場/売相場。両替・送金の方向に応じて使い分ける。
- 計算例: `deal_bas_r` が 871.54 なら 100円 = 871.54ウォン。1万ウォン ≒ 10000 ÷ 871.54 × 100 ≒ 1,147円。

**レスポンス例**: `examples/kexim-exchangejson.sample.json`(KEXIMは海外IPを遮断するため構造を再現した記述例) / `examples/ecos-key-statistic-list.sample.json`(2026-09-10にサンプルキーで実測取得した実データ)。

## ソースB: ECOS(韓国銀行)

主要統計100の一覧に円レートが含まれる。手軽に検証できるのが利点。

```bash
curl -s "https://ecos.bok.or.kr/api/KeyStatisticList/{ECOS_KEY}/json/kr/1/10"
```

- レスポンスの `KeyStatisticList.row` 配列に `원/엔(100엔) 환율(매매기준율)` と `원/달러 환율(종가)` が入る。`DATA_VALUE` が値、`TIME` が基準日。
- 時系列が必要なら `StatisticSearch` を使う(統計表・項目コードはECOSサイトで確認する)。

## どちらを使うか

- 両替・送金の実務寄りの相場(ttb/tts)が要る → KEXIM。
- 国家統計としての仲値、またはKEXIMに届かない環境(下記「注意」) → ECOS。

## 注意

- **KEXIMのサイトは海外やデータセンターのIPからの接続を遮断することがある**(2026-09-09、海外VPSから接続不可を確認)。その場合はECOSに切り替える。
- レートは1日1回更新の日次データ。リアルタイムの市場レートではない。
- 両替所・カード決済の実勢レートは手数料が乗る。「表示レートと実際の両替額は違う」と旅行者に伝える。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **KEXIMが接続不可(タイムアウト)**: 上記のIP遮断の可能性。ECOSに切り替え、ユーザーには「KEXIMに届かないため韓国銀行のデータで答える」と伝える。
- **KEXIMが null/空配列**: 非営業日の指定。前営業日に変えて再試行。
- **ECOS `RESULT.CODE` が ERROR系**: 認証キーかパラメータの誤り。`INFO-200`(データなし)は日付や項目コードの見直し。
- 数値を推測で補わない。両ソースとも失敗したら「今日のレートを確認できません」と正直に伝える。

## English summary

Fetches KRW/JPY exchange rates from two official free Korean APIs: the Korea Eximbank (KEXIM) rate API (the travel-industry standard, returns JPY(100) directly) and the Bank of Korea ECOS API (national statistics; verified live with real data on 2026-09-09). Both need a free instantly-issued API key. Use `deal_bas_r` (mid rate) for rough yen conversions. KEXIM blocks some overseas/datacenter IPs - fall back to ECOS. Never invent a rate.
