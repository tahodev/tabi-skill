---
name: incheon-airport
description: 仁川国際空港の旅客便の到着・出発状況(遅延・ゲート・ターミナル)を仁川国際空港公社のAPIで調べる。空港鉄道(AREX)のデータも併記。「成田からの便、何時に着く?」に対応。無料APIキーが必要。
license: MIT
metadata:
  category: transit
  locale: ja-JP
---

# incheon-airport

仁川国際空港公社(인천국제공항공사)の旅客便運航情報APIで、到着・出発便の状況を照会するスキル。2026-09-09 に2オペレーションの実在を確認済み。

## キーの取得

公共データポータル(data.go.kr)で仁川国際空港公社の旅客便API(B551177)に活用申請し、serviceKey を取得する(無料)。空港公式サイト(日本語あり): https://www.airport.kr/ap/ja/index.do

## 基本の流れ

```bash
# 到着便(時間帯指定・HHMM)
curl -s "http://apis.data.go.kr/B551177/StatusOfPassengerFlightsDSOdp/getPassengerArrivalsDSOdp?serviceKey={KEY}&from_time=0900&to_time=1200&airport=NRT&type=json"

# 出発便
curl -s "http://apis.data.go.kr/B551177/StatusOfPassengerFlightsDSOdp/getPassengerDeparturesDSOdp?serviceKey={KEY}&from_time=1500&to_time=1800&airport=NRT&type=json"
```

- `airport`: 相手空港のコード。成田 `NRT`、羽田 `HND`、関西 `KIX`、福岡 `FUK`、中部 `NGO`、新千歳 `CTS` など。
- `from_time`/`to_time`: 調べたい時間帯(HHMM)。

## レスポンスの読み方

各itemの主な項目:

- `flightId`: 便名、`airline`: 航空会社名
- `airport`: 相手空港コード
- `scheduleDateTime` / `estimatedDateTime`: 予定時刻 / 変更後時刻(HHMM)。遅延はこの差で分かる。
- `gatenumber`: ゲート番号、`terminalid`: ターミナル(T1/T2)
- `remark`: 状況(到着・遅延・欠航など、韓国語)

**レスポンス例**: `examples/getPassengerArrivalsDSOdp.sample.json`(構造を再現した記述例。実キーでの実測取得ではない)。

## 空港鉄道(AREX)のデータ

空港鉄道の運行データも公共データポータルにある(仁川国際空港公社「인천공항 공항철도 운행 정보」、data.go.kr 15098226、要serviceKey): https://www.data.go.kr/data/15098226/openapi.do

旅行者向けの基本(2026-09-09時点、公式案内ベース):

- **直通列車(직통열차)**: ソウル駅 ⇄ 仁川空港T1 約43分、T2 約51分。ノンストップ。
- **一般列車(일반열차)**: 各駅停車。弘大入口・孔徳・デジタルメディアシティなどにも停まる。
- 時刻表・運賃は公式サイトで確認する: https://www.arex.or.kr/

## 注意

- 便データは空港公社の提供データそのまま。最終案内は航空会社・空港の掲示で確認するよう旅行者に伝える。
- コードシェア便は運航会社の便名で出ることがある。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **HTTP 401 `SERVICE_KEY_IS_NULL`**: serviceKey 未指定・不正。
- **`NO_OPENAPI_SERVICE_ERROR`**: サービス名ミス。旅客便は `StatusOfPassengerFlightsDSOdp`。
- **空のitems**: その時間帯・相手空港の便なし。時間帯を広げる。
- 遅延理由や到着時刻を推測で言わない。

## English summary

Checks Incheon Airport passenger flight arrivals/departures (delays, gates, terminals) via the Incheon International Airport Corporation API - endpoint existence verified on 2026-09-09; not yet exercised with a real key. Free data.go.kr serviceKey required. Filter by time window and counterpart airport code (NRT/HND/KIX/...). Also documents the AREX airport-railroad dataset (data.go.kr 15098226) and baseline travel times (direct train Seoul Station to T1 ~43 min, T2 ~51 min). Read-only.
