# korea-weather-midterm ガイド

気象庁(KMA)の中期予報APIで、3〜10日先の天気の見通し(午前/午後の天気・降水確率・気温の範囲)を照会するスキル。無料APIキーが必要(2026-09-14 オペレーション実在確認)。

**正本は [`korea-weather-midterm/SKILL.md`](../../korea-weather-midterm/SKILL.md)。** パラメータ、エラー時の対応はすべてそちら。このガイドは概要のみ。

- データ: KMA MidFcstInfoService(apis.data.go.kr/1360000)
- できること: 「来週のソウル旅行、傘いる?」に3〜10日先の見通しで答える
- 注意: あくまで見通し。直前には korea-weather(短期予報)で再確認する
