---
name: kr-bus
description: 韓国の高速バス(고속버스)の時刻・運賃を国土交通部(TAGO)高速バスAPIで調べる。「ソウルから釜山までバスは?」のような質問に対応。無料APIキーが必要。予約は扱わない。
license: MIT
metadata:
  category: transit
  locale: ja-JP
---

# kr-bus

TAGOの高速バス情報オープンAPIで、高速バスターミナル間の時刻・運賃を照会するスキル。2026-09-09 に2オペレーションの実在を確認済み。

## キーの取得

公共データポータル(data.go.kr)でTAGO高速バスAPIに活用申請し、共通認証キー(serviceKey)を取得する(無料)。ポータル: https://www.data.go.kr/

## 基本の流れ

1. ターミナルIDを調べる
2. 区間の時刻を照会する

```bash
# ターミナル一覧
curl -s "http://openapi.tago.go.kr/openapi/service/ExpBusInfoService/getExpBusTrminlList?serviceKey={KEY}"

# 時刻照会(例: ソウル京釜 → 釜山総合)
curl -s "http://openapi.tago.go.kr/openapi/service/ExpBusInfoService/getStrtpntAlocFndExpbusInfo?serviceKey={KEY}&depTerminalId=NAEK010&arrTerminalId=NAEK300&depPlandTime=${TRAVEL_DATE}"
```

- レスポンスの各item: `depPlandTime`/`arrPlandTime`(発着)、`charge`(運賃・ウォン)、`gradeNm`(等級名: 一般/優等/プレミアムなど)。
- 主なターミナル名: ソウルは「서울경부」(江南の高速バスターミナル)と「동서울」(東ソウル)、他に釜山総合、大田複合など。IDは一覧で確認する。

**レスポンス例**: `examples/getStrtpntAlocFndExpbusInfo.sample.xml`(構造を再現した記述例。実キーでの実測取得ではない)。

## 対象外(2026-09-09時点)

- **市外バス(시외버스)**: TAGOに市外バスサービス自体は存在するが(公共データポータル 15098516)、オペレーションの実在を実測で確認できなかったため未収録。2026-09-10 にも `openapi.tago.go.kr/openapi/service/SuburbsBusInfoService/*` を再検証したが 404(パス不明)で、認証エラーすら返らなかった。確認でき次第、別スキルとして追加する。
- ソウル市内バス: 別のAPI(ソウル市)が必要。未収録。

## 注意

- 照会のみ。予約は高速バス統合予約サイト等で行う。エージェントが代行しない。
- 高速バスはKTXより安く、深夜便もある。所要時間は道路状況で大きく変わると旅行者に伝える。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **`지원하지 않는 인증방식입니다`**: serviceKey 不正。
- **`NO_OPENAPI_SERVICE_ERROR`**: URLミス。ベースは `openapi.tago.go.kr`。
- **空のitems**: その区間・日付の便なし、またはターミナルIDの組み合わせ違い(同じ都市に複数ターミナルがある)。ターミナル一覧で確認する。

## English summary

Queries Korean express bus (고속버스) times and fares via the TAGO express bus API (endpoint existence verified on 2026-09-09; not yet exercised with a real key). Free data.go.kr serviceKey required. Look up terminal IDs first, then query schedules between terminals. Intercity (시외버스) buses are documented as out of scope because their TAGO operations could not be verified. Read-only: no booking.
