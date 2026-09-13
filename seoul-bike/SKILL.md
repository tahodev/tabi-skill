---
name: seoul-bike
description: ソウル市の公共自転車「タリョンイ(따릉이)」のリアルタイム貸出台数をソウルオープンデータ広場APIで照会する。「ホンデの駅近くでいま借りられる自転車はある?」に対応。無料APIキー(サンプルキーで即動作確認できる)。
license: MIT
metadata:
  category: transit
  locale: ja-JP
---

# seoul-bike

ソウルオープンデータ広場(서울 열린데이터광장)の公共自転車リアルタイム貸出情報APIで、タリョンイ(따릉이, ソウル市のシェアサイクル)各ステーションの「いま停まっている自転車の台数」を照会するスキル。2026-09-14 にサンプルキーで**実データ取得を実測確認**済み(INFO-000 で麻浦区の実ステーションが返った)。

照会だけのスキル。実際のレンタル(アプリ登録・決済)は扱わない。

## キーの取得

ソウルオープンデータ広場(data.seoul.go.kr)で利用申請すると即時発行される(無料)。動作確認だけならサンプルキー `sample` がそのまま使える(1〜5件まで)。

## 基本の流れ

### 1. サンプルキーで動作確認(実測済み)

```bash
curl -s -m 30 "http://openapi.seoul.go.kr:8088/sample/json/bikeList/1/5/"
```

- サンプルキーは1回に5件まで。6件以上を要求すると `ERROR-335`(「샘플키는 한번에 최대 5건」)が返る。実キーでは1回最大1,000件。

### 2. 実キーで全件ページング

```bash
curl -s -m 30 "http://openapi.seoul.go.kr:8088/{SEOUL_KEY}/json/bikeList/1/1000/"
```

- 返ってきた `list_total_count` を見て、1,000件刻みで `{START}/{END}` をずらして全ステーションを取る。ステーション名で絞るAPIフィルタはないので、取得側で `stationName` の部分一致(例: 「홍대입구역」)で探す。

## 読み方

- `stationName`: 「102. 망원역 1번출구 앞」のように「番号. 名前」。駅名・出口名を含むので日本語話者にも説明しやすい。
- `parkingBikeTotCnt`: **いま借りられる台数**。これが主役。
- `rackTotCnt`: ラック(駐輪枠)数。`shared`: 稼働率(%)。
- `stationLatitude` / `stationLongitude`: 緯度経度。現在地からの距離計算に使う。
- `stationId`: ST-から始まる内部ID。

## 実レスポンス例(2026-09-14 サンプルキーで実測取得)

```json
{"rentBikeStatus":{"list_total_count":5,"RESULT":{"CODE":"INFO-000","MESSAGE":"정상 처리되었습니다."},"row":[
{"rackTotCnt":"15","stationName":"102. 망원역 1번출구 앞","parkingBikeTotCnt":"6","shared":"40","stationLatitude":"37.55564880","stationLongitude":"126.91062927","stationId":"ST-4"}]}}
```

## 注意

- `parkingBikeTotCnt` が 0 のステーションでは借りられない。返却したい場合は逆にラックの空きが必要なので、空きは `rackTotCnt - parkingBikeTotCnt` で計算する。
- 深夜〜早朝は台数が偏る(回送で再配置される)。「いま」の照会であることを伝える。
- 実際の利用にはタリョンイ公式アプリ(決済方法の登録が必要)が要る。旅行者向けの1日券(일일권)はアプリ内で買う。照会はこのAPI、レンタル操作はアプリ、と分けて案内する。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **`RESULT.CODE` が `INFO-000` 以外**: `INFO-200` は認証エラー(キー未指定・無効)。`ERROR-335` はサンプルキーで5件超を要求した。`ERROR-500/600` はキーやURL形式のミス。
- **XMLの `<RESULT>` だけ返る**: URLのパス(キー・フォーマット・サービス名の順)を見直す。
- 台数を推測で答えない。APIが返さなければ「取れなかった」と言う。

## English summary

Fetches realtime availability for Seoul's public bike-share "Ttareungyi" (따릉이) from the Seoul Open Data Plaza bikeList API - verified live with the public `sample` key on 2026-09-14 (INFO-000, real Mapo-gu stations returned). Free instantly-issued key from data.seoul.go.kr; the sample key returns up to 5 rows (ERROR-335 beyond that), a real key pages 1,000 rows per call. `parkingBikeTotCnt` is the rentable count; free docks = rackTotCnt - parkingBikeTotCnt. Lookups only - actual rental needs the official Ttareungyi app with a payment method. Never invent availability numbers.
