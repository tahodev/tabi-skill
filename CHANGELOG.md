# Changelog

このファイルは [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) の形式にしたがう。バージョン付けは [SemVer](https://semver.org/lang/ja/) ベース。

## 更新ルール(メンテナ向け)

- **スキルを追加・削除したとき**: 対象バージョンの `Added` / `Removed` にスキル名と概要を1行で記録する。
- **スキルが使うエンドポイント・データソースを変えたとき**: `Changed` に新旧のURLや式を記録する。外部データの仕様変更への追従もここ。
- CHANGELOG を更新したら、リリース時に git tag と GitHub Release を同じバージョンで切る(現状は手動)。

## [Unreleased]

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

[Unreleased]: https://github.com/tahodev/tabi-skill/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/tahodev/tabi-skill/releases/tag/v0.1.0
