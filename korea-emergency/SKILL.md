---
name: korea-emergency
description: 韓国旅行中の緊急連絡先の静的データ。警察112・救急119・観光案内1330(日本語可)・在韓日本国大使館など。「韓国で警察は何番?」「日本語で相談できる窓口は?」に対応。API不要・オフラインでも使える。
license: MIT
metadata:
  category: safety
  locale: ja-JP
---

# korea-emergency

韓国旅行中に必要になる連絡先の静的データ集。API不要。ネットが不安定な状況でもエージェントが即答できるようにするためのスキル。公式情報を2026-09-19に再確認した。電話番号は毎月、住所と受付時間は四半期ごとに公式ページで見直す。

## 緊急電話番号(韓国国内から)

| 用途 | 番号 | メモ |
| --- | --- | --- |
| 警察(경찰) | 112 | 通訳サポートあり |
| 救急・消防(소방) | 119 | 通訳サポートあり |
| 観光案内・苦情(관광안내) | 1330 | **日本語対応あり・07:00〜24:00(KST)**。道案内、観光通訳、旅行トラブルの相談窓口 |
| 出入国(출입국) | 1345 | ビザ・滞在関連 |


- 海外からかける場合は国番号(+82)と市外局番(ソウル=2)を付ける(例: +82-2-1330)。
- 1330は韓国観光公社の公式窓口(07:00〜24:00 KST): https://japanese.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=140632
- 旧1339は2013年に廃止され119へ統合済み: https://www.mohw.go.kr/board.es?act=view&bid=0027&cg_code=&list_no=287774&mid=a10503010100&tag=

## 在韓日本国大使館(주한 일본대사관)

- 所在地: ソウル特別市 鍾路区 栗谷路6(서울특별시 종로구 율곡로 6)、ツインツリータワーA棟
- 領事・旅券紛失: +82-2-739-7400(時間外も緊急連絡に接続)
- 旅券紛失・事件事故・邦人援護の窓口。釜山・済州には総領事館/総領事館分室がある。最新の住所・電話番号・開館時間は外務省・大使館の公式案内で必ず確認する。

## 旅行者に伝えるべき前提

- 112/119は韓国語が基本。英語・日本語は通訳センター経由になることが多い。焦らず英語で「Japanese interpreter, please」と伝える。
- 医療機関は大学病院の国際診療センターが日本語・英語に強い。119または大使館に相談する。
- クレジットカード紛失はカード会社の海外デスクに即連絡(カード裏面の番号)。このスキルは個社の番号を持たない。

## データの鮮度について

出典: 韓国観光公社、韓国保健福祉部、在韓日本国大使館領事部(https://www.kr.emb-japan.go.jp/itpr_ja/consulate.html)。検証日: 2026-09-19。電話番号は毎月、住所・受付時間は四半期ごとに再確認する。

電話番号や住所は変わることがある。**人命に関わる場面では、このデータをそのまま鵜呑みにせず、1330や大使館の公式案内で再確認する**よう必ず添える。

## English summary

Static emergency-contact data for travelers in Korea: police 112, fire/ambulance 119, the 1330 tourist hotline (Japanese-speaking, 07:00-24:00 KST), immigration 1345, and the Embassy of Japan consular line (+82-2-739-7400, with after-hours emergency routing). The former 1339 line was abolished and merged into 119. No API needed. Data rechecked 2026-09-19; always tell the traveler to reconfirm via official channels in a real emergency.
