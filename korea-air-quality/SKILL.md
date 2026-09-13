---
name: korea-air-quality
description: 韓国環境公団のエアコリア(AirKorea)大気汚染情報APIで、都市別のリアルタイムPM2.5/PM10/統合大気環境指数を照会する。「今日ソウルの空気は悪い?」に対応。無料APIキーが必要。
license: MIT
metadata:
  category: weather
  locale: ja-JP
---

# korea-air-quality

韓国環境公団(한국환경공단)のエアコリア大気汚染情報サービス(ArpltnInforInqireSvc)で、PM2.5(초미세먼지)・PM10(미세먼지)・統合大気環境指数(khai)のリアルタイム値を照会するスキル。2026-09-14 に2オペレーションの**エンドポイント実在**を確認済み(キーなしで叩き、404ではなく認証エラーが返ることを確認。実キーでのデータ応答はまだ未検証)。

黄砂・微小粒子状物質が出やすい春先や、屋外観光の計画時に使う。天気そのものは [korea-weather](../korea-weather/SKILL.md) 参照。

## キーの取得

公共データポータル(data.go.kr)で「한국환경공단_에어코리아_대기오염정보」(ArpltnInforInqireSvc)に活用申請し、serviceKey を取得する(無料)。ポータル: https://www.data.go.kr/

## 基本の流れ

### 1. 都市(시도)ごとのリアルタイム測定(getCtprvnRltmMesureDnsty)

```bash
curl -s "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&returnType=json&numOfRows=100&sidoName=%EC%84%9C%EC%9A%B8"
```

- `sidoName` は韓国語の都市名(서울=ソウル, 부산=釜山, 인천=仁川, 대구=大邱, 대전=大田, 광주=光州, 울산=蔚山, 세종=世宗, 경기=京畿, 강원=江原, 충북/충남, 전북/전남, 경북/경남, 제주=済州)。URLエンコードする(ソウルは `%EC%84%9C%EC%9A%B8`)。
- 指定した都市の全測定所(stationName)の現在値が返る。

### 2. 測定所ごとの時系列(getMsrstnAcctoRltmMesureDnsty)

```bash
curl -s "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey={KEY}&returnType=json&numOfRows=24&stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=DAILY"
```

- `stationName` は測定所名(例: 종로구=鍾路区)。`dataTerm` は `DAILY`(24時間)など。

## 読み方

- `pm10Value` / `pm25Value`: それぞれPM10・PM2.5の濃度(µg/m³)。`pm10ValueFlag` などのフラグ列は機器状態(점검 등)を示す。
- `pm10Grade` / `pm25Grade` / `khaiGrade`: 1=좋음(良い), 2=보통(普通), 3=나쁨(悪い), 4=매우나쁨(非常に悪い)。
- `khaiValue`: 統合大気環境指数。`dataTime`: 測定時刻(「2026-09-14 13:00」形式)。

## 注意

- 旅行者には値そのものより等級(좋음/보통/나쁨/매우나쁨)で伝える。「나쁨」以上なら屋外予定の見直しやマスク(KF94)を勧める。
- 測定値は韓国国内基準。日本の基準や感覚と換算しない。
- 明日以降の予報は別サービス(미세먼지 예보, MinuDustFrcstDspthSvc)。このスキルはリアルタイム測定のみ。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **HTTP 401 `SERVICE_KEY_IS_NULL` / 認証エラー**: serviceKey 未指定・不正。
- **`NO_OPENAPI_SERVICE_ERROR`**: サービス名のミス。ベースは `apis.data.go.kr/B552584/ArpltnInforInqireSvc`。
- **`NO_DATA` / 空のitems**: 都市名・測定所名のミス(韓国語表記を見直す)。機器点検で値が空のこともある。その場合は隣の測定所を見る。
- 値や等級を推測で補わない。

## レスポンス例(構造)

```json
{"response":{"body":{"items":[{"stationName":"종로구","dataTime":"2026-09-14 13:00","pm10Value":"32","pm10Grade":"2","pm25Value":"15","pm25Grade":"1","khaiValue":"58","khaiGrade":"2"}],"totalCount":40}}}
```

## English summary

Fetches realtime air-quality readings (PM10, PM2.5, and the composite KHAI index) for Korean cities from the Korea Environment Corporation AirKorea API (ArpltnInforInqireSvc) - endpoint existence verified on 2026-09-14 (unauthenticated probes return auth errors, not 404; not yet exercised with a real key). Free data.go.kr serviceKey required. getCtprvnRltmMesureDnsty returns all monitoring stations for a sidoName (URL-encoded Korean city name); grades map 1=좋음, 2=보통, 3=나쁨, 4=매우나쁨 - report grades to travelers, and suggest indoor plans or a KF94 mask at 나쁨 or worse. Forecasts live in a separate service (MinuDustFrcstDspthSvc) and are out of scope here.
