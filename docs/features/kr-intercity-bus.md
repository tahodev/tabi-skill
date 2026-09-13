# kr-intercity-bus ガイド

国土交通部TAGOの市外バス(시외버스)APIで、ターミナル間の便・時刻・運賃を照会するスキル。無料APIキーが必要(2026-09-14 オペレーション実在確認)。

**正本は [`kr-intercity-bus/SKILL.md`](../../kr-intercity-bus/SKILL.md)。** パラメータ、エラー時の対応はすべてそちら。このガイドは概要のみ。

- データ: TAGO SuburbsBusInfoService(openapi.tago.go.kr)
- できること: 「ソウルから江陵までバスある?」に市外バスの時刻・運賃で答える。地方都市への便が豊富
- 注意: 高速バスは kr-bus。照会のみで予約は扱わない
