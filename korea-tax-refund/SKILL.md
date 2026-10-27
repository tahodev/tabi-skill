---
name: korea-tax-refund
description: 韓国旅行の税金還付(タックスリファンド)の静的データ。事後免税の条件・即時還付と空港/市内カウンター還付の違い・仁川空港の手続き場所。「いくらから還付される?」「空港で何をすればいい?」に対応。API不要。
license: MIT
metadata:
  category: shopping
  locale: ja-JP
---

# korea-tax-refund

韓国での買い物で消費税の還付を受けるための静的ガイド。API不要。韓国観光公社の公式案内「免税制度と税金還付」(最終更新2025-10-21)を2026-10-28に照合した。

## 2つの免税制度

| 区分 | Duty Free(免税) | Tax Refund(事後免税) |
| --- | --- | --- |
| 店の表示 | 「Duty Free」ロゴの免税店 | 「Tax Free」「Tax Refund」ロゴの事後免税店 |
| 価格 | 関税・消費税抜きの価格 | 消費税込みで支払い、あとで還付 |
| 代表的な場所 | 空港・市内のロッテ/新羅/新世界などの免税店 | 百貨店・大型スーパー・一部コンビニなどの加盟店 |

## 事後免税の対象条件

- 韓国滞在期間 **6ヶ月未満の外国人**(海外居住2年以上または海外永住権を持ち、韓国滞在3ヶ月未満の在外同胞も対象)。
- **1回の会計が15,000ウォン以上**。
- 購入品は **未開封・未使用** のまま持ち出す。
- **購入日から3ヶ月以内** に韓国を出国する。
- 会計時に **パスポートを提示** し、「事後免税(Tax Refund)」と記載された還付領収書を受け取る。

## 還付の受け方は2通り

### 1. 即時還付(その場で税抜き)

- 一部加盟店(百貨店・大型スーパー・コンビニなど)で、会計時にその場で消費税抜きの価格で買える。別途の還付請求手続きは不要。
- 条件: **1回の会計が15,000ウォン以上100万ウォン未満**、かつ **滞在中の総購入額が500万ウォン以下**。

### 2. 事後還付(あとで還付を受け取る)

1. 店でパスポートを提示して還付領収書を受け取る。
2. 出国時、空港で **購入品と還付領収書を税関職員に見せて輸出通関の承認** を受ける(預け荷物にする前に手続きする)。
3. 還付カウンターまたはKIOSKで還付を受け取る。

- **空港・港湾の共通カウンター**: 還付代行業者に関係なく利用可。総購入金額の上限なし。
- **市内還付カウンター**: その場で現金還付も可能だが、**還付領収書の購入金額が600万ウォン以下** の場合のみ利用可。その業者の商品しか還付できない。市内で還付を受けた場合でも、出国時に必ず空港の税関で持ち出し確認を受け、領収書を提出する。
- 還付方法: 現金(KIOSK)、クレジットカード、Alipay、WeChat Pay など。
- 還付代行業者のロゴ例: Global Blue、GLOBAL TAX FREE、Easy Tax Refund、CubeRefund。

## 仁川空港での還付場所(公式案内より)

- **第1旅客ターミナル**: 免税エリア3階 28番ゲート付近。
- **第2旅客ターミナル**: 一般エリア3階 チェックインカウンターG&F付近 / 免税エリア3階 253番ゲート付近。
- カウンターが閉まっている場合: 還付領収書に必要事項を記入して指定ボックスに投函。申請が通れば **1〜2ヶ月ほどで** 決済したクレジットカードやAlipay、WeChat Payに還付される。

## エラー・失敗時の対応

- 還付領収書をもらい忘れた・「Tax Refund」表示の有無が分からない: その場では還付対象にできないことが多い。会計前にロゴの有無を確認させる。
- 金額条件・対象外品目など判断が付かない場合: 韓国観光案内電話 **1330(日本語・07:00〜24:00 KST、海外からは+82-2-1330)** か、各還付代行業者のサイトで確認する。
- このスキルの数値は2025-10-21時点の公式案内が基準。制度改正の可能性があるため、高額な買い物の前には公式案内での再確認を促す。

## データの鮮度について

出典: 韓国観光公社「免税制度と税金還付」( https://japanese.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=140928 、ページ最終更新2025-10-21)。照合日: 2026-10-28。金額条件や対象範囲は改正されうるので、利用時は公式案内での再確認を添える。

## English summary

Static guide to Korea's tax-refund system for travelers: the difference between Duty Free and Tax Refund stores, eligibility (foreign visitors staying under 6 months, single receipt of 15,000 KRW or more, unused goods, departure within 3 months), instant in-store refunds (15,000 KRW to under 1,000,000 KRW per receipt, up to 5,000,000 KRW total per trip), and airport/city-counter refunds (customs export confirmation before checking luggage; city counters only accept receipts of 6,000,000 KRW or less). Includes the Incheon Airport refund-counter locations (T1 near Gate 28 on the departures level; T2 near check-in G&F and Gate 253). No API needed. Cross-checked against the Korea Tourism Organization page (updated 2025-10-21) on 2026-10-28; advise reconfirmation via 1330 or the refund operators for large purchases.
