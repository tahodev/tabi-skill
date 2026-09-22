---
name: korea-beach
description: 海洋水産部の海水浴場情報APIで、韓国全国の海水浴場の住所・規模などを照会する。無料APIキーが必要。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# korea-beach

海洋水産部(해양수산부)の海水浴場情報APIで、全国の海水浴場を照会する。2026-09-21 に検証環境から接続し、キーなしで `SERVICE_KEY_IS_NULL`、無効キーで `SERVICE_KEY_IS_NOT_REGISTERED_ERROR` が返ることを確認した。実キーでの実データ取得は未検証。

データは韓国語。旅行者に伝えるときはエージェントが日本語に訳して渡す。

## キーと公式資料

無料の serviceKey を申請する: https://www.data.go.kr/data/15058519/openapi.do

## 基本の流れ

```bash
curl -s -m 30 "http://apis.data.go.kr/1192000/service/OceansBeachInfoService1/getOceansBeachInfo1?serviceKey={KEY}&pageNo=1&numOfRows=20&type=json"
```

`pageNo` と `numOfRows` で全件をページングする。

## レスポンスの読み方

各 item の海水浴場名・住所(시도/구군 などの行政区域)を読み、釜山(海雲台・広安里)や江陵など滞在先の近い海岸を拾う。開場期間やシャワー・駐車の有無など、項目の有無は年度データによって差がある。

## 注意

海水浴場の「開場」は夏期限定。開場期間外は監視員や施設がなく、遊泳は自己責任になる。台風シーズン(7〜9月)は `korea-weather-warning` で警報を確認してから向かう。水母(クラゲ)注意報などは別途現地案内を見る。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- `SERVICE_KEY_IS_NOT_REGISTERED_ERROR`: キーは有効だがこのサービスへの利用申請が済んでいない。data.go.kr で当該サービスの 활용신청 を行う。
- 空の `items`: `pageNo` を戻す。検索系の絞り込みパラメータはないので全件から選ぶ。

## English summary

Looks up beaches across Korea (name, address, administrative area) via the official Ministry of Oceans and Fisheries beach-info API. Endpoint existence was confirmed by the expected auth errors on 2026-09-21; real-key data was not exercised. Opening season is summer-only; check weather warnings before swimming.
