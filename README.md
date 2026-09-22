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
| 気象特報(注意報・警報)を調べる | `korea-weather-warning` | 気象庁の気象特報APIで発表中の特報と通報文を照会。豪雨・台風シーズンの移動前チェックに | APIキー(無料)が必要 | [korea-weather-warning ガイド](docs/features/korea-weather-warning.md) |
| 観光地・祭りを日本語で検索する | `kto-tour` | 韓国観光公社 TourAPI 4.0 の日本語サービス(JpnService2)。名前も説明も日本語 | APIキー(無料)が必要 | [kto-tour ガイド](docs/features/kto-tour.md) |
| 宿泊施設の詳細を日本語で調べる | `kto-stay-detail` | TourAPI日本語サービスで宿・設備・チェックイン時刻を検索 | APIキー(無料)が必要 | [ガイド](docs/features/kto-stay-detail.md) |
| 韓国全国の祭りを日本語で探す | `kto-festival` | TourAPI日本語サービスで開催日・地域から祭りを検索 | APIキー(無料)が必要 | [ガイド](docs/features/kto-festival.md) |
| ソウルの公共Wi-Fiを探す | `seoul-wifi` | 施設名・住所・座標から公共Wi-Fi設置場所を検索 | APIキー(無料)が必要 | [ガイド](docs/features/seoul-wifi.md) |
| 韓国の薬局を探す | `korea-pharmacy` | HIRA公式APIで地域・現在地周辺の薬局を検索 | APIキー(無料)が必要 | [ガイド](docs/features/korea-pharmacy.md) |
| 韓国の病院を探す | `korea-hospital` | HIRA公式APIで地域・現在地周辺の病院を検索 | APIキー(無料)が必要 | [ガイド](docs/features/korea-hospital.md) |
| AREX直通列車の時刻を調べる | `arex-timetable` | AREX公式サイトの現行時刻表を参照 | 不要 | [ガイド](docs/features/arex-timetable.md) |
| 仁川空港の便情報を調べる | `incheon-airport` | 仁川国際空港公社APIで到着・出発便の遅延・ゲートを照会。空港鉄道データつき | APIキー(無料)が必要 | [incheon-airport ガイド](docs/features/incheon-airport.md) |
| 緊急連絡先を調べる | `korea-emergency` | 112/119/1330(日本語可)・在韓日本国大使館などの静的データ。オフラインでも使える | 不要 | [korea-emergency ガイド](docs/features/korea-emergency.md) |
| 旅の基本を調べる | `korea-etiquette` | コンセント・チップ・T-money・交通マナーのチートシート | 不要 | [korea-etiquette ガイド](docs/features/korea-etiquette.md) |
| 韓国の祝日・記念日を調べる | `korea-holidays` | 韓国天文研究院(KASI)の特日情報APIで祝日・国慶日を照会。旧暦の連休(설날・추석)の正確な日付が取れる | APIキー(無料)が必要 | [korea-holidays ガイド](docs/features/korea-holidays.md) |
| 韓国の空気の状態を調べる | `korea-air-quality` | エアコリア(AirKorea)APIでPM2.5/PM10の等級を照会。「今日ソウルの空気は?」に | APIキー(無料)が必要 | [korea-air-quality ガイド](docs/features/korea-air-quality.md) |
| ソウルのシェアサイクルを調べる | `seoul-bike` | タルンイ(따릉이)のリアルタイム貸出台数を照会。サンプルキーで即試せる | APIキー(無料)が必要 | [seoul-bike ガイド](docs/features/seoul-bike.md) |
| ソウルのイベントを探す | `seoul-events` | ソウル市の文化イベントAPIでコンサート・展示・祭りを月・ジャンルで検索 | APIキー(無料)が必要 | [seoul-events ガイド](docs/features/seoul-events.md) |
| ソウルの混雑状況を調べる | `seoul-crowd` | ソウル市リアルタイム都市データAPIで主要スポットの混雑度(4段階)を照会。「いま明洞は混んでる?」に | APIキー(無料)が必要 | [seoul-crowd ガイド](docs/features/seoul-crowd.md) |
| 1週間先の天気の見通しを調べる | `korea-weather-midterm` | 気象庁の中期予報APIで3〜10日先の天気・気温の見通しを照会 | APIキー(無料)が必要 | [korea-weather-midterm ガイド](docs/features/korea-weather-midterm.md) |
| 市外バスの時刻・運賃を調べる | `kr-intercity-bus` | TAGO市外バスAPIでターミナル間の便を照会。江陵・慶州など地方都市へ | APIキー(無料)が必要 | [kr-intercity-bus ガイド](docs/features/kr-intercity-bus.md) |
| 釜山など地方都市の地下鉄を調べる | `kr-metro` | TAGO地下鉄情報APIで釜山・大邱・大田・光州の駅検索と時刻表を照会 | APIキー(無料)が必要 | [kr-metro ガイド](docs/features/kr-metro.md) |

各スキルの**正本は `<スキル名>/SKILL.md`** です。`docs/features/` のガイドは概要版なので、詳細な手順・パラメータ・エラー対応は必ず SKILL.md を参照してください。

スコープについて:

- 乗換検索アプリや予約サイトのスクレイピングは対象外です。公式API・公開データのみ。
- 予約・購入・発券など状態を変更する操作は扱いません。照会と計算だけです。
検証状態(2026-09-19再整理):

| 状態 | スキル |
| --- | --- |
| 実データ応答確認 | krw-jpy-rate(ECOS, 9/9), seoul-bike / seoul-events / seoul-crowd(9/14), seoul-wifi / arex-timetable(9/19), seoul-subway(列車位置・到着予測APIをサンプルキーで実測, 9/22。本番利用は無料キー推奨) |
| オペレーション存在・認証エラー確認(実キー未実行) | kto-tour / kr-train / kr-bus / korea-weather / incheon-airport(9/9), korea-holidays / korea-air-quality / korea-weather-warning / korea-weather-midterm / kr-intercity-bus / kr-metro(9/14), kto-stay-detail / kto-festival / korea-pharmacy / korea-hospital(9/19) |
| 静的公式情報 | korea-emergency(9/19), korea-etiquette |
- 市外バス(시외버스)は `kr-intercity-bus` で照会できます(2026-09-14 にオペレーション実在確認)。SRT(수서발 고속철도)は公開APIがないため対象外です。

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
| Check weather warnings | `korea-weather-warning` | KMA weather-warning API: active advisories/warnings and bulletins | Free API key required | [korea-weather-warning guide](docs/features/korea-weather-warning.md) |
| Search sights and festivals in Japanese | `kto-tour` | TourAPI 4.0 Japanese service (JpnService2): names and descriptions in Japanese | Free API key required | [kto-tour guide](docs/features/kto-tour.md) |
| Search lodging details in Japanese | `kto-stay-detail` | TourAPI Japanese lodging and detail lookup | Free API key required | [guide](docs/features/kto-stay-detail.md) |
| Search nationwide festivals in Japanese | `kto-festival` | TourAPI festival search by date and region | Free API key required | [guide](docs/features/kto-festival.md) |
| Find Seoul public Wi-Fi | `seoul-wifi` | Public Wi-Fi locations by name, address or coordinates | Free API key required | [guide](docs/features/seoul-wifi.md) |
| Find pharmacies in Korea | `korea-pharmacy` | Official HIRA pharmacy search | Free API key required | [guide](docs/features/korea-pharmacy.md) |
| Find hospitals in Korea | `korea-hospital` | Official HIRA hospital search | Free API key required | [guide](docs/features/korea-hospital.md) |
| Check AREX Express times | `arex-timetable` | Current official AREX timetable | Not required | [guide](docs/features/arex-timetable.md) |
| Check Incheon Airport flights | `incheon-airport` | Arrival/departure status, delays, gates; airport-railroad data | Free API key required | [incheon-airport guide](docs/features/incheon-airport.md) |
| Look up emergency contacts | `korea-emergency` | 112/119/1330 (Japanese OK), Embassy of Japan; works offline | Not required | [korea-emergency guide](docs/features/korea-emergency.md) |
| Look up travel basics | `korea-etiquette` | Plugs, tipping, T-money, transit manners cheat sheet | Not required | [korea-etiquette guide](docs/features/korea-etiquette.md) |
| Check Korean holidays | `korea-holidays` | KASI special-day API: holidays and national days, incl. exact lunar Seollal/Chuseok dates | Free API key required | [korea-holidays guide](docs/features/korea-holidays.md) |
| Check air quality in Korea | `korea-air-quality` | AirKorea API: PM2.5/PM10 grades by city | Free API key required | [korea-air-quality guide](docs/features/korea-air-quality.md) |
| Check Seoul bike-share availability | `seoul-bike` | Realtime Ttareungyi dock counts; testable with a public sample key | Free API key required | [seoul-bike guide](docs/features/seoul-bike.md) |
| Find events in Seoul | `seoul-events` | Seoul cultural-event API: concerts, exhibitions, festivals by month/genre | Free API key required | [seoul-events guide](docs/features/seoul-events.md) |
| Check how crowded a Seoul hotspot is | `seoul-crowd` | Seoul realtime city-data API: 4-level congestion for major hotspots | Free API key required | [seoul-crowd guide](docs/features/seoul-crowd.md) |
| Check the week-ahead weather outlook | `korea-weather-midterm` | KMA mid-range forecast API: 3-10 day outlook and temperatures | Free API key required | [korea-weather-midterm guide](docs/features/korea-weather-midterm.md) |
| Check intercity bus times and fares | `kr-intercity-bus` | TAGO intercity bus API: terminal-to-terminal schedules (regional cities) | Free API key required | [kr-intercity-bus guide](docs/features/kr-intercity-bus.md) |
| Check regional-city subways (Busan, etc.) | `kr-metro` | TAGO subway API: station search and timetables for Busan/Daegu/Daejeon/Gwangju | Free API key required | [kr-metro guide](docs/features/kr-metro.md) |

The canonical source for each skill is its `<skill>/SKILL.md`. The guides under `docs/features/` are summaries only - always refer to SKILL.md for full procedures, parameters, and error handling.

Scope notes:

- No scraping of transfer-search apps or booking sites. Official APIs and public data only.
- Nothing here changes state: no reservations, purchases, or ticketing. Lookups and calculations only.
- Verification differs by skill: some have real response rows, some only confirmed operation existence via the expected auth error, and Seoul subway returned live train-position and arrival rows with the sample key on 2026-09-22. See the Japanese verification matrix above (updated 2026-09-22).

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
