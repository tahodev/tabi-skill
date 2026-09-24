# 検証ポリシー

tabi-skill の各スキルは、どこまで実測したかを3段階の等級で表す。等級とスキル別の検証日は [verification.json](verification.json) に記録し、CI(`scripts/check-verification.py`)がREADMEの検証マトリクスとの一致と鮮度を毎日チェックする。

## 等級

| 等級 | 条件 | 鮮度期限 |
| --- | --- | --- |
| `live-data-verified` | APIスキル: 実キーまたはサンプルキーで、実際のレスポンス行を取得して確認した。静的スキル: 公式出典の掲載内容と照合した。 | 90日(`review_days` で短縮可) |
| `endpoint-confirmed` | オペレーションの実在だけを確認した。キーなしで叩いて認証エラー(`SERVICE_KEY_IS_NULL` など)が返る、または `NO_OPENAPI_SERVICE_ERROR` 以外の想定内エラーが返る。実データは未確認。 | 180日 |
| `experimental` | 出典・実測のどちらかが未整備。`note` に何が足りないかを書く。 | なし |

- 認証エラーだけの確認を `live-data-verified` と書かない。空配列や `INFO-200`(データなし)も実データ確認には数えない。
- 昇格: 実データを取得したら `status` を上げ、`verified_on` を実測日にする。READMEの該当行も同じコミットで移す。
- 降格: 期限までに再実測できない、またはAPIが実データを返さなくなったら、等級を下げてCHANGELOGの `Changed` に記録する。

## verification.json の書き方

```json
"seoul-subway": {
  "status": "live-data-verified",
  "kind": "api",
  "verified_on": "2026-09-22",
  "note": "realtimePosition / realtimeStationArrival をサンプルキーで実測",
  "fixtures": [
    { "path": "seoul-subway/examples/realtime-station-arrival.sample.json", "origin": "illustrative" }
  ]
}
```

- `kind`: `api` または `static`。
- `verified_on`: `experimental` 以外は必須(YYYY-MM-DD)。
- `review_days`: 等級の標準期限より短く再確認したいときだけ書く(例: 電話番号を毎月確認する `korea-emergency` は30)。
- `fixtures`: `examples/` 以下のレスポンス例。`origin` は実測で取得したものが `captured`、構造だけを再現したものが `illustrative`。

## CIチェック

| スクリプト | 内容 |
| --- | --- |
| `scripts/check-verification.py` | 全スキルが登録されているか、等級・日付の形式、鮮度期限(残り14日で WARN、超過で FAIL)、READMEの等級別の行と登録内容の一致 |
| `scripts/check-fixtures.py` | `examples/` の全ファイルが登録済みか、JSON/XMLとして読めるか、成功ステータス(`00` / `0000` / `INFO-000` など)と1件以上のレコードがあるか、SKILL.md の説明(`構造を再現した記述例` の有無)と `origin` が一致するか |

push と pull request では鮮度切れを WARN にとどめる(`TABI_FRESHNESS=warn`)。毎日の定期実行と手動実行では FAIL になり、health-check の issue が自動で立つ。

ローカルで将来の日付を試すときは `TABI_TODAY=2026-12-31 python3 scripts/check-verification.py` のように日付を指定する。
