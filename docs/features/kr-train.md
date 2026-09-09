# kr-train ガイド

KTXなど韓国の列車の時刻・運賃を、国土交通部TAGO列車APIで照会するスキル。無料APIキーが必要(2026-09-09 オペレーション実在確認)。

**正本は [`kr-train/SKILL.md`](../../kr-train/SKILL.md)。** 駅IDの調べ方、車種コード、エラー時の対応はすべてそちら。このガイドは概要のみ。

- データ: TAGO TrainInfoService(openapi.tago.go.kr)
- できること: 「ソウル→釜山のKTXは?」に発着時刻・大人運賃つきで答える
- 注意: 照会のみ。予約・発券はKORAIL公式で
