---
name: kr-metro
description: 国土交通部TAGOの地下鉄情報APIで、釜山・大邱・大田・光州など地方都市の地下鉄の駅検索と時刻表を照会する。「釜山で西面→海雲台の電車は?」に対応。無料APIキーが必要。
license: MIT
metadata:
  category: transit
  locale: ja-JP
---

# kr-metro

国土交通部(TAGO)の地下鉄情報サービス(SubwayInfoService)で、韓国の地方都市(釜山・大邱・大田・光州)の都市鉄道の駅と時刻表を照会するスキル。ソウルのリアルタイム到着情報は [seoul-subway](../seoul-subway/SKILL.md) 参照(ソウルは別API)。2026-09-14 に2オペレーションの**エンドポイント実在**を確認済み(キーなしで叩き、404ではなく認証系エラー resultCode 99 が返ることを確認。実キーでのデータ応答はまだ未検証)。

## キーの取得

公共データポータル(data.go.kr)で「국토교통부_(TAGO)_지하철정보」(SubwayInfoService)に活用申請し、serviceKey を取得する(無料)。ポータル: https://www.data.go.kr/

## 基本の流れ

### 1. 駅名で検索(getKwrdFndSubwaySttnList)

```bash
curl -s "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getKwrdFndSubwaySttnList?serviceKey={KEY}&_type=json&subwayStationName=%ED%95%B4%EC%9A%B4%EB%8C%80"
```

- `subwayStationName` に駅名(韓国語、URLエンコード。例の `%ED%95%B4%EC%9A%B4%EB%8C%80` = 해운대 = 海雲台)。
- 駅ID(`subwayStationId`)と駅名のリストが返る。

### 2. 駅の時刻表(getSubwaySttnAcctoSchdulList)

```bash
curl -s "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnAcctoSchdulList?serviceKey={KEY}&_type=json&subwayStationId={STATION_ID}&dailyTypeCode=01&upDownTypeCode=U"
```

- `subwayStationId` は検索で取ったID。`dailyTypeCode` は曜日区分(01=平日 など)、`upDownTypeCode` は上り/下り(U/D)。詳細のコード体系はTAGOの活用ガイドが正本。

## 注意

- **リアルタイムの到着予測ではない**(時刻表データ)。「いま何分で来る?」には答えられない。ソウル市内なら seoul-subway を使う。
- 釜山・大邱・大田・光州の都市鉄道が対象。ソウル首都圏(1〜9号線)は含まないことがある。
- 時刻表どおりに運行するとは限らない。最終確認は各社の公式案内で。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **resultCode 99「지원하지 않는 인증방식입니다」/ HTTP 401**: serviceKey 未指定・不正。
- **HTTP 404**: オペレーション名のミス。綴りは `getKwrdFndSubwaySttnList` / `getSubwaySttnAcctoSchdulList`。
- **空のリスト**: 駅名の表記ゆれ。「역」を付けない(해운대、해운대역 ではなく)。
- 時刻を推測で答えない。

## English summary

Fetches subway station lookups and timetables for Korea's regional metro systems (Busan, Daegu, Daejeon, Gwangju) from the MOLIT TAGO SubwayInfoService - endpoint existence verified on 2026-09-14 (unauthenticated probes return resultCode 99 auth errors, not 404; not yet exercised with a real key). Free data.go.kr serviceKey required. Search stations with getKwrdFndSubwaySttnList (Korean name, no "역" suffix), then pull the timetable with getSubwaySttnAcctoSchdulList (subwayStationId + dailyTypeCode + upDownTypeCode). These are timetables, not realtime arrivals - for Seoul realtime use seoul-subway. Never invent times.
