# インストールガイド

## 前提条件

- Node.js 18 以上 (`npx` が使えること)
- `npx skills add` に対応したコーディングエージェント (Claude Code、Codex、OpenCode など)

## インストール

```bash
# すべてのスキルをグローバルにインストール
npx --yes skills add tahodev/tabi-skill --all -g

# 特定のスキルだけインストール
npx --yes skills add tahodev/tabi-skill --skill kto-tour -g
npx --yes skills add tahodev/tabi-skill --skill seoul-subway -g
npx --yes skills add tahodev/tabi-skill --skill korea-emergency -g
```

`-g` を外すと、カレントのプロジェクトだけにインストールされます。

## スキルの構成

各スキルはリポジトリ直下のディレクトリにある `SKILL.md` 1ファイルだけで動きます。追加のランタイムやプロキシサーバーは不要です。照会はすべて `curl` など一般的なHTTPクライアントで完結します。

```
tabi-skill/
  krw-jpy-rate/SKILL.md
  seoul-subway/SKILL.md
  kr-train/SKILL.md
  kr-bus/SKILL.md
  korea-weather/SKILL.md
  kto-tour/SKILL.md
  incheon-airport/SKILL.md
  korea-emergency/SKILL.md
  korea-etiquette/SKILL.md
  docs/
    install.md
    features/<skill>.md   # スキルごとの概要ガイド(正本は各 SKILL.md)
```

## APIキーについて

多くのスキルは韓国の公共データポータル(data.go.kr)やソウルオープンデータ広場の**無料キー**を使います。発行はどれも無料・即時(または自動承認)で、課金契約は不要です。各スキルの SKILL.md にキーの取り方を書いています。キーはリポジトリにコミットしないでください。
