---
name: japan-customs-allowance
description: 韓国旅行から日本に帰国する際の税関の免税範囲(酒類・たばこ・その他20万円枠)の静的データ。「お土産はいくらまで免税?」に対応。API不要。
license: MIT
metadata:
  category: customs
  locale: ja-JP
---

# japan-customs-allowance

韓国での買い物(korea-tax-refund)の帰り道に対になる、**日本入国時の税関の免税範囲**の静的データ。日本の税関公式ページ「海外旅行者の免税範囲」を2026-10-28に照合した。API不要。

## 免税の範囲(入国者1人あたり)

| 品目 | 免税範囲 | 備考 |
| --- | --- | --- |
| 酒類 | 3本 | 1本760mlのもの |
| たばこ(紙巻) | 200本 | 居住者・非居住者、日本製・外国製の区別なし(2018-10-01変更) |
| たばこ(加熱式) | 個装等10個 | 1箱あたり紙巻20本相当量(IQOSなら200本、gloなら200本、withなら50個が目安) |
| たばこ(葉巻) | 50本 | |
| その他の品目 | 海外市価の合計20万円 | 超えた場合は20万円以内に収まる品物が免税になり、残りに課税(税関が旅行者に有利なように免税品目を選択) |

## 旅行者に伝えるべき前提

- **20歳未満は酒類・たばこの免税がない**。6歳未満はおもちゃなど本人使用と認められるもの以外は免税にならない。
- **1個で20万円を超える品物**(例: 25万円のバッグ)は20万円枠に収まらず、**全額に課税**される。高額品を買う前に必ず伝える。
- **1品目ごとの海外市価の合計が1万円以下のもの**は原則免税(例: 1個1,000円のチョコレート9個)。
- 携帯品と別送品は**合算**で計算する。別送品は帰国後6か月以内に輸入するものに限る。
- 「海外市価」は外国での通常の小売購入価格。円換算は税関の公示レートで行う。
- 免税範囲を超える場合は申告が必要。品目ごとの税率は税関の公式案内で確認する。

## 韓国側の還付との関係

- 韓国での事後免税(タックスリファンド)は**韓国の消費税の還付**で、日本側の免税範囲とは別の制度。韓国で還付を受けても、日本入国時の免税範囲(上表)は変わらない。両方を混同しないよう伝える。

## データの鮮度について

出典: 税関「海外旅行者の免税範囲」( https://www.customs.go.jp/kaigairyoko/menzei.htm )。照合日: 2026-10-28。免税範囲・税率は改正されうるので、利用時は税関の公式案内での再確認を添える。

## English summary

Static data on Japan Customs' duty-free allowance for travelers returning from Korea: alcohol 3 bottles (760ml each), tobacco 200 cigarettes / 10 packs of heated tobacco / 50 cigars, and other goods up to a combined overseas market value of 200,000 yen (items worth 10,000 yen or less per category are exempt; a single item over 200,000 yen is taxed in full). Under-20s get no alcohol or tobacco allowance. Accompanied and unaccompanied goods are combined; unaccompanied goods must arrive within 6 months. Korea's tax refund and Japan's duty-free allowance are separate systems - do not conflate them. No API needed. Cross-checked with the official Japan Customs page on 2026-10-28; advise reconfirmation against the official page.
