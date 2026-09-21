# Changelog

このファイルは [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) の形式にしたがう。バージョン付けは [SemVer](https://semver.org/lang/ja/) ベース。

## 更新ルール(メンテナ向け)

- **スキルを追加・削除したとき**: 対象バージョンの `Added` / `Removed` にスキル名と概要を1行で記録する。
- **スキルが使うエンドポイント・データソースを変えたとき**: `Changed` に新旧のURLや式を記録する。外部データの仕様変更への追従もここ。
- CHANGELOG を更新したら、リリース時に git tag と GitHub Release を同じバージョンで切る(現状は手動)。

## [Unreleased]

### Added
- `kto-stay-detail`, `kto-festival`, `seoul-wifi`, `korea-pharmacy`, `korea-hospital`, `arex-timetable`
- `kto-nearby` - TourAPI JpnService2 `locationBasedList2` で現在地周辺の観光スポットを座標・半径指定で検索(無料APIキー。2026-09-21 オペレーション実在確認)
- `kto-food` - TourAPI JpnService2 で飲食店(コンテンツ種別39)を地域・キーワード検索。`areaBasedList2` / `searchKeyword2` を使用(無料APIキー。2026-09-21 オペレーション実在確認)
- `kto-course` - TourAPI JpnService2 で旅行コース(コンテンツ種別25)を地域検索(無料APIキー。2026-09-21 オペレーション実在確認)
- `korea-trail` - 韓国観光公社 Durunubi API で歩行コース(コリアぐるれ道等)の距離・所要時間・難易度を照会。`courseList` / `routeList` を使用。データは韓国語(無料APIキー。2026-09-21 オペレーション実在確認)
- `korea-camping` - 韓国観光公社 GoCamping API で全国のキャンプ場を照会。`basedList` / `searchList` を使用。データは韓国語(無料APIキー。2026-09-21 オペレーション実在確認)
- `kr-city-bus` - TAGOバス情報API(1613000)で地方都市の市内バス到着予測を照会。`getCtyCodeList` / `getSttnNoList` / `getSttnAcctoArvlPrearngeInfoList` / `getRouteNoList` を使用(無料APIキー。2026-09-21 オペレーション実在確認)
- `korea-disaster-alert` - 行政安全部の災難文字API(safetydata.go.kr, DSSP-IF-00247)で緊急メッセージと対象地域を照会。データは韓国語(無料APIキー。2026-09-21 キーエラー応答で実在確認)
- `korea-beach` - 海洋水産部の海水浴場情報API(1192000)で全国の海水浴場を照会(無料APIキー。2026-09-21 オペレーション実在確認)
- `korea-uv-index` - 気象庁の生活気象指数 照会サービス(4.0) `getUVIdxV5` で地域別紫外線指数を照会(無料APIキー。2026-09-21 オペレーション実在確認)

- `korea-public-toilet` - 全国公衆トイレ標準データAPIで住所・開放時間・設備を照会(2026-09-21 操作実在確認、実キー未検証)
- `korea-parking` - 全国駐車場情報標準データAPIで台数・料金・営業時間を照会(2026-09-21 操作実在確認、実キー未検証)
- `korea-museum` - 全国博物館美術館情報標準データAPIで開館時間・休館日・料金を照会(2026-09-21 操作実在確認、実キー未検証)
- `korea-tourist-site` - 全国観光地情報標準データAPIで営業時間・料金・駐車情報を照会(2026-09-21 操作実在確認、実キー未検証)
- `korea-cultural-festival` - 全国文化祭標準データAPIで開催期間・場所・主催者を照会(2026-09-21 操作実在確認、実キー未検証)

### Changed
- `check-urls.py`: WARN/オープンAPIゲートウェイのホスト一覧に `www.safetydata.go.kr` / `safetydata.go.kr` / `api.data.go.kr` を追加(korea-disaster-alert のベースURL。HTTP 200 + resultCode 30 のキーエラーを「実在」と判定するため)
- 緊急連絡先を現行公式情報へ更新(1339廃止、1330受付時間、大使館領事番号)
- READMEをスキル別検証マトリクスへ変更し、検証レベルの過大表現を修正
- seoul-subway / incheon-airport の検証状態、seoul-eventsの変動件数、用語、運用例の日付を修正
- 静的データに出典・検証日・再確認周期を追加

## [0.2.0] - 2026-09-14

### Added
- `korea-holidays` - 韓国天文研究院(KASI)特日情報APIで祝日・国慶日・記念日を照会(無料APIキー。2026-09-14 エンドポイント実在確認)
- `korea-air-quality` - エアコリア(AirKorea)APIで都市別PM2.5/PM10/統合大気環境指数を照会(無料APIキー。2026-09-14 エンドポイント実在確認)
- `seoul-bike` - タルンイ(따릉이)リアルタイム貸出台数をソウルオープンデータ広場APIで照会(無料APIキー。2026-09-14 サンプルキーで実データ取得を実測)
- `seoul-events` - ソウル市の文化イベントを月・ジャンル・タイトルで検索(無料APIキー。2026-09-14 サンプルキーで実データ取得・各フィルタを実測)
- `korea-weather-warning` - 気象庁(KMA)気象特報APIで発表中の注意報・警報と通報文を照会(無料APIキー。2026-09-10 エンドポイント実在確認)
- `seoul-crowd` - ソウル市リアルタイム都市データAPIで主要スポットの混雑度を照会(無料APIキー。2026-09-14 サンプルキーで実データ取得を実測。サンプルキーは地点固定の挙動も確認)
- `korea-weather-midterm` - 気象庁(KMA)中期予報APIで3〜10日先の見通しを照会(無料APIキー。2026-09-14 エンドポイント実在確認)
- `kr-intercity-bus` - TAGO市外バス(시외버스)APIでターミナル間の時刻・運賃を照会(無料APIキー。2026-09-14 オペレーション実在確認)
- `kr-metro` - TAGO地下鉄情報APIで釜山・大邱・大田・光州の駅検索と時刻表を照会(無料APIキー。2026-09-14 オペレーション実在確認)
- 全API系スキルに `examples/` のレスポンス例を追加。krw-jpy-rate のECOS例は実測取得、他は「記述例」と明記した構造再現
- `seoul-subway`: 主要観光駅44件の日本語→韓国語対応CSV(`data/stations-ja-ko.csv`)を同梱
- `korea-weather`: 格子座標表を12都市に拡張(仁川・水原・大田・大邱・慶州・全州・光州・江陵・西帰浦を追加)

### Changed
- `check-urls.sh`: オープンAPIゲートウェイのホスト一覧に `openapi.seoul.go.kr` を追加(seoul-bike / seoul-events のベースURLがキーなし・パラメータなしで 4xx を返しても「実在」と判定するため)
- `check-urls.sh`: geo-restricted WARN 対象に `*data.go.kr*` / `*ecos.bok.or.kr*` / `*openapi.seoul.go.kr*` を追加。2026-09-12 以降 GitHub Actions ランナーからこれらの韓国政府系ホストへの接続が 000 となり health-check が連続失敗していた(issue #2)のに対応
- README: 市外バス未収録の注記を更新(kr-intercity-bus 収録)し、SRT(公開APIなし)を対象外として明記

### Fixed
- `check-urls.sh`: apis.data.go.kr などオープンAPIゲートウェイの 400/401/403 を「エンドポイント実在」として扱うように。ベースURL無パラメータ呼び出しでの誤検知(issue #1)を解消
- `lint-skills.sh`: CONTRIBUTING.md が必須とする metadata(category, locale) のチェックを追加
- `kr-train` 他: 「verified live」表記を「エンドポイント実在の確認」に修正(実キーでの応答検証は未実施と明記)
- `seoul-subway`: curl例の生の韓国語駅名をパーセントエンコード化し、エンコード方法を追記

## [0.1.0] - 2026-09-09

初回リリース。日本から韓国への旅行者を助ける照会系スキル9件を収録。全エンドポイントは公開当日に実測検証済み(キー必要なAPIは認証エラーでの実在確認、ECOS・ソウル地下鉄は実データ取得)。

### Added
- `krw-jpy-rate` - ウォン・円の為替レートを韓国輸出入銀行API / 韓国銀行ECOSから取得(無料APIキー)
- `seoul-subway` - ソウル地下鉄のリアルタイム到着情報をソウルオープンデータ広場APIで取得。日本語駅名データつき(無料APIキー)
- `kr-train` - KTXなど列車の時刻・運賃を国土交通部TAGO列車APIで取得(無料APIキー)
- `kr-bus` - 高速バスの時刻・運賃をTAGO高速バスAPIで取得(無料APIキー)
- `korea-weather` - 気象庁(KMA)公共データ短期予報APIで韓国各地の天気を取得(無料APIキー)
- `kto-tour` - 韓国観光公社 TourAPI 4.0 の日本語サービス(JpnService2)で観光地・祭り・宿を検索(無料APIキー)
- `incheon-airport` - 仁川空港の旅客便到着・出発情報を仁川国際空港公社APIで取得。空港鉄道データつき(無料APIキー)
- `korea-emergency` - 緊急連絡先・在韓日本国大使館・観光案内1330などの静的データ(API不要)
- `korea-etiquette` - コンセント・チップ・交通マナーなどのチートシート(API不要)

[Unreleased]: https://github.com/tahodev/tabi-skill/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/tahodev/tabi-skill/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/tahodev/tabi-skill/releases/tag/v0.1.0
