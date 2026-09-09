# korea-weather-warning ガイド

気象庁(KMA)の気象特報APIで、発表中の注意報・警報と通報文を照会するスキル。無料APIキーが必要(2026-09-10 オペレーション実在確認)。

**正本は [`korea-weather-warning/SKILL.md`](../../korea-weather-warning/SKILL.md)。** パラメータ、特報の種類、エラー時の対応はすべてそちら。このガイドは概要のみ。

- データ: KMA WthrWrnInfoService(apis.data.go.kr/1360000)
- できること: 「いま韓国で警報出てる?」に発表中の特報リストと通報文で答える
- 注意: 特報は韓国語で返る。台風・豪雨シーズンの移動前チェック向け
