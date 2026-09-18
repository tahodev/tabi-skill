---
name: kr-intercity-bus
description: 国土交通部TAGOの市外バス(시외버스)APIで、ターミナル間の便・時刻・運賃を照会する。「ソウルから江陵までバスある?」に対応。無料APIキーが必要。
license: MIT
metadata:
  category: transit
  locale: ja-JP
---

# kr-intercity-bus

国土交通部(TAGO)の市外バス情報サービス(SuburbsBusInfoService)で、市外バス(시외버스)ターミナル間の便を照会するスキル。高速バス(고속버스)は [kr-bus](../kr-bus/SKILL.md) 参照。2026-09-14 に2オペレーションの**エンドポイント実在**を確認済み(キーなしで叩き、404ではなく認証系エラー resultCode 99 が返ることを確認。実キーでのデータ応答はまだ未検証)。

地方都市(江陵・慶州・全州など)への移動は高速バスより市外バスの方が便数が多いことがある。

## キーの取得

公共データポータル(data.go.kr)で「국토교통부_(TAGO)_시외버스정보」(SuburbsBusInfoService)に活用申請し、serviceKey を取得する(無料)。ポータル: https://www.data.go.kr/

## 基本の流れ

### 1. ターミナル一覧(getSuberbsBusTrminlList)

```bash
curl -s "http://openapi.tago.go.kr/openapi/service/SuburbsBusInfoService/getSuberbsBusTrminlList?serviceKey={KEY}&_type=json"
```

- 市外バスターミナルのID(`terminalId`)と名称の一覧が返る。オペレーション名の `Suberbs` はTAGO公式の表記(スペルミスに見えるが正しい)。

### 2. ターミナル間の便(getStrtpntAlocFndSuberbsBusInfo)

```bash
curl -s "http://openapi.tago.go.kr/openapi/service/SuburbsBusInfoService/getStrtpntAlocFndSuberbsBusInfo?serviceKey={KEY}&_type=json&depTerminalId={DEP_ID}&arrTerminalId={ARR_ID}&depPlandTime=${TRAVEL_DATE}"
```

- `depTerminalId` / `arrTerminalId` は一覧で取ったID。`depPlandTime` は出発日(YYYYMMDD)。
- 出発時刻・到着時刻・運賃・等級(일반/우등 など)が返る。

## 注意

- 時刻表と運賃の照会のみ。予約は各バス会社のサイト(시외버스 예매는 t-money 앱 등)なので、このスキルでは扱わない。
- 高速バス(kr-bus)とターミナルID体系が別。同じ都市でもターミナルが違うことがある(例: ソウルは高速=セントラルシティ系、市外=東ソウルなど)。
- 応答は韓国語。ターミナル名には日本語読みを添える(동서울 = 東ソウル, 강릉 = 江陵)。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **resultCode 99「지원하지 않는 인증방식입니다」/ HTTP 401**: serviceKey 未指定・不正。
- **HTTP 404**: オペレーション名のミス。綴りは `getSuberbsBusTrminlList` / `getStrtpntAlocFndSuberbsBusInfo`。
- **`NO_DATA` / 空のitems**: その区間・日付の便がない。隣接ターミナルや高速バス(kr-bus)を案内する。
- 便の有無・時刻を推測で答えない。

## English summary

Fetches intercity bus (시외버스) schedules and fares between Korean terminals from the MOLIT TAGO SuburbsBusInfoService - endpoint existence verified on 2026-09-14 (unauthenticated probes return resultCode 99 auth errors, not 404; not yet exercised with a real key). Free data.go.kr serviceKey required. Look up terminal IDs with getSuberbsBusTrminlList (the "Suberbs" spelling is official), then query schedules with getStrtpntAlocFndSuberbsBusInfo (depTerminalId/arrTerminalId/depPlandTime). Express buses (고속버스) are a separate service - see kr-bus. Lookups only, no booking. Never invent schedules.
