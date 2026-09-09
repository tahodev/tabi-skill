<p align="center">
  <a href="https://tahodev.github.io/tabi-skill/">
    <img src="https://tahodev.github.io/tabi-skill/emblem.png" alt="tabi-skill のシンボル — 落款風の「旅」の印" width="120">
  </a>
</p>

<h1 align="center">tabi-skill</h1>

<p align="center">
  韓国旅行を、AIエージェントに。<br>
  <a href="https://tahodev.github.io/tabi-skill/"><strong>紹介サイト — tahodev.github.io/tabi-skill</strong></a>
</p>

[![health-check](https://github.com/tahodev/tabi-skill/actions/workflows/health-check.yml/badge.svg)](https://github.com/tahodev/tabi-skill/actions/workflows/health-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

日本から韓国への旅行を手伝う、AIエージェント向けスキルコレクションです。
韓国観光公社 TourAPI の**日本語サービス**、国土交通部TAGOの列車・バスAPI、ソウル市の地下鉄リアルタイムAPI、気象庁の予報APIなど、公式APIと公開データだけを使った照会系スキルを集めています。

Claude Code、Codex、OpenCode など、`npx skills add` に対応したコーディングエージェントで使えます。

姉妹リポジトリ: 日本の暮らし向け [kurashi-skill](https://github.com/tahodev/kurashi-skill) 、台湾の暮らし向け [baodao-skill](https://github.com/tahodev/baodao-skill) 。

## できること

「ログイン」列は、利用者本人のアカウントやシークレットが必要かどうかだけを示します。

| できること | スキル名 | 説明 | ログイン | ドキュメント |
| --- | --- | --- | --- | --- |
| ウォン・円の為替レートを調べる | `krw-jpy-rate` | 韓国輸出入銀行API / 韓国銀行ECOS APIからレート取得。2ソースで冗長化 | APIキー(無料)が必要 | [krw-jpy-rate ガイド](docs/features/krw-jpy-rate.md) |
| ソウル地下鉄の到着時刻を調べる | `seoul-subway` | ソウルオープンデータ広場APIでリアルタイム到着予測。日本語駅名データつき | APIキー(無料)が必要 | [seoul-subway ガイド](docs/features/seoul-subway.md) |
| KTXの時刻・運賃を調べる | `kr-train` | 国土交通部TAGO列車APIで列車の発着時刻・大人運賃を照会 | APIキー(無料)が必要 | [kr-train ガイド](docs/features/kr-train.md) |
| 高速バスの時刻・運賃を調べる | `kr-bus` | TAGO高速バスAPIでターミナル間の便を照会 | APIキー(無料)が必要 | [kr-bus ガイド](docs/features/kr-bus.md) |
| 韓国各地の天気予報を調べる | `korea-weather` | 気象庁(KMA)公共データ短期予報APIで格子座標ごとの予報を取得 | APIキー(無料)が必要 | [korea-weather ガイド](docs/features/korea-weather.md) |
| 観光地・祭りを日本語で検索する | `kto-tour` | 韓国観光公社 TourAPI 4.0 の日本語サービス(JpnService2)。名前も説明も日本語 | APIキー(無料)が必要 | [kto-tour ガイド](docs/features/kto-tour.md) |
| 仁川空港の便情報を調べる | `incheon-airport` | 仁川国際空港公社APIで到着・出発便の遅延・ゲートを照会。空港鉄道データつき | APIキー(無料)が必要 | [incheon-airport ガイド](docs/features/incheon-airport.md) |
| 緊急連絡先を調べる | `korea-emergency` | 112/119/1330(日本語可)・在韓日本国大使館などの静的データ。オフラインでも使える | 不要 | [korea-emergency ガイド](docs/features/korea-emergency.md) |
| 旅の基本を調べる | `korea-etiquette` | コンセント・チップ・T-money・交通マナーのチートシート | 不要 | [korea-etiquette ガイド](docs/features/korea-etiquette.md) |

各スキルの**正本は `<スキル名>/SKILL.md`** です。`docs/features/` のガイドは概要版なので、詳細な手順・パラメータ・エラー対応は必ず SKILL.md を参照してください。

スコープについて:

- 乗換検索アプリや予約サイトのスクレイピングは対象外です。公式API・公開データのみ。
- 予約・購入・発券など状態を変更する操作は扱いません。照会と計算だけです。
- 全エンドポイントは公開日(2026-09-09)に実測検証済み。以降の仕様変更は health-check CI と issue で追跡します。
- 市外バス(시외버스)は TAGO にサービス自体はあるものの、オペレーションを実測確認できなかったため未収録です([kr-bus の注記](kr-bus/SKILL.md)参照)。

## インストール

```bash
# すべてのスキルをインストール
npx --yes skills add tahodev/tabi-skill --all -g

# 特定のスキルだけインストール
npx --yes skills add tahodev/tabi-skill --skill kto-tour -g
```

Node.js 18 以上と `npx` が必要です。詳しくは [インストールガイド](docs/install.md) を参照してください。

## English

**tabi-skill** (旅, "tabi" = journey) is a collection of AI-agent skills for Japanese travelers in Korea. Read-only lookups built only on official APIs and public datasets: the Korea Tourism Organization TourAPI **Japanese service**, TAGO train/bus APIs, Seoul realtime subway arrivals, KMA weather, Incheon Airport flight status, plus static emergency and etiquette data.

Works with any coding agent that supports `npx skills add` (Claude Code, Codex, OpenCode, ...).

Sibling repos: [kurashi-skill](https://github.com/tahodev/kurashi-skill) (daily life in Japan), [baodao-skill](https://github.com/tahodev/baodao-skill) (daily life in Taiwan).

### What you can do

| What you can do | Skill | Description | Login | Docs |
| --- | --- | --- | --- | --- |
| Check KRW/JPY exchange rates | `krw-jpy-rate` | Korea Eximbank API + Bank of Korea ECOS API (two sources) | Free API key required | [krw-jpy-rate guide](docs/features/krw-jpy-rate.md) |
| Check Seoul subway arrivals | `seoul-subway` | Realtime arrival predictions, with Japanese station-name data | Free API key required | [seoul-subway guide](docs/features/seoul-subway.md) |
| Check KTX times and fares | `kr-train` | TAGO train API: schedules and adult fares | Free API key required | [kr-train guide](docs/features/kr-train.md) |
| Check express bus times | `kr-bus` | TAGO express bus API: terminal-to-terminal schedules | Free API key required | [kr-bus guide](docs/features/kr-bus.md) |
| Check weather in Korea | `korea-weather` | KMA public-data short-term forecast API | Free API key required | [korea-weather guide](docs/features/korea-weather.md) |
| Search sights and festivals in Japanese | `kto-tour` | TourAPI 4.0 Japanese service (JpnService2): names and descriptions in Japanese | Free API key required | [kto-tour guide](docs/features/kto-tour.md) |
| Check Incheon Airport flights | `incheon-airport` | Arrival/departure status, delays, gates; airport-railroad data | Free API key required | [incheon-airport guide](docs/features/incheon-airport.md) |
| Look up emergency contacts | `korea-emergency` | 112/119/1330 (Japanese OK), Embassy of Japan; works offline | Not required | [korea-emergency guide](docs/features/korea-emergency.md) |
| Look up travel basics | `korea-etiquette` | Plugs, tipping, T-money, transit manners cheat sheet | Not required | [korea-etiquette guide](docs/features/korea-etiquette.md) |

The canonical source for each skill is its `<skill>/SKILL.md`. The guides under `docs/features/` are summaries only - always refer to SKILL.md for full procedures, parameters, and error handling.

Scope notes:

- No scraping of transfer-search apps or booking sites. Official APIs and public data only.
- Nothing here changes state: no reservations, purchases, or ticketing. Lookups and calculations only.
- Every endpoint was verified live on release day (2026-09-09). Later spec changes are tracked by the health-check CI and issues.

### Install

```bash
# Install every skill
npx --yes skills add tahodev/tabi-skill --all -g

# Install a single skill
npx --yes skills add tahodev/tabi-skill --skill kto-tour -g
```

Node.js 18+ and `npx` are required. See the [install guide](docs/install.md) for details.

## ライセンス / License

[MIT](LICENSE)
