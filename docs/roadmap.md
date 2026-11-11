# ロードマップ / ROADMAP

更新日: 2026-11-11。v0.4.0(2026-11-04)時点で41スキルを収録。

## 収録済み / Shipped

- 41スキルの一覧と正本への入口は [README](../README.md) を参照。各スキルの正本は `<skill>/SKILL.md`。
- 検証等級(`live-data-verified` / `endpoint-confirmed` / `experimental`)と鮮度期限は [検証ポリシー](verification.md) と [verification.json](verification.json) で管理し、CIが期限切れを検出する。

## 現在の優先順位 / Maintenance first

1. 検証の鮮度期限をCIで監視し、古い値で回答しない。
2. 実測できないソースは収録しない(実測主義)。認証エラー応答しか取れないスキルは `endpoint-confirmed` と明示する。
3. README・SKILL.md・ガイド・Pagesを同期し、検証していない機能を宣伝しない。

## 対象外・不採用 / Out of scope

- SRT(수서발 고속철도): 公開APIがないため対象外。KTXはTAGO経由で `kr-train` が対応。
- 乗換検索アプリ・予約サイトのスクレイピング: 収録しない。公式APIと公開データのみ。
- 予約・購入・発券など状態を変更する操作: スキルの役割は照会と計算のみ。
- 新しい候補は、公式ソースの実測に通ってからSKILL.mdを出す。日付や実装を約束する表は置かない。

## English summary

41 skills shipped as of v0.4.0 (2026-11-04); see the README for the canonical list.
Maintenance comes first: verification freshness is enforced in CI, unverifiable sources are not shipped, and docs stay in sync.
Out of scope: SRT (no public API), scraping transfer-search or booking sites, and any state-changing action (reservations, purchases, ticketing). New candidates ship only after the official source is verified live.
