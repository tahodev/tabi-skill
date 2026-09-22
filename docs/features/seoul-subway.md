# seoul-subway ガイド

ソウル地下鉄のリアルタイム到着予測を、ソウルオープンデータ広場APIで取得するスキル。到着予測API(realtimeStationArrival)と列車位置API(realtimePosition)はサンプルキーで実データ確認済み(2026-09-22)。本番利用には無料APIキーを推奨。

**正本は [`seoul-subway/SKILL.md`](../../seoul-subway/SKILL.md)。** 駅名対応表、路線コード、エラー時の対応はすべてそちら。このガイドは概要のみ。

- データ: ソウル交通公社 実시간 지하철 도착정보(swopenapi.seoul.go.kr)
- できること: 「弘大入口から次の電車は?」に方面・路線つきで答える
- 注意: API入力は韓国語駅名(「역」なし)。日本語駅名の全対応表は公共データポータル 15044232
