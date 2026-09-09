# krw-jpy-rate ガイド

ウォン・円の為替レートを、韓国輸出入銀行APIと韓国銀行ECOS APIの2ソースから取得するスキル。無料APIキーが必要。

**正本は [`krw-jpy-rate/SKILL.md`](../../krw-jpy-rate/SKILL.md)。** キーの取り方、パラメータ、2ソースの使い分け、エラー時の対応はすべてそちら。このガイドは概要のみ。

- データ: KEXIM 現在환율API(data.go.kr 3068846) / ECOS KeyStatisticList(2026-09-09 実データ取得確認)
- できること: 「1万ウォンは何円?」「両替の相場は?」に仲値(deal_bas_r / 매매기준율)で答える
- 注意: 日次データ。KEXIMは海外IPを遮断することがあり、その場合はECOSに切り替える
