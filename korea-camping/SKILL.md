---
name: korea-camping
description: 韓国観光公社のコキャンピング(고캠핑)APIで、全国のキャンプ場を検索する。無料APIキーが必要。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# korea-camping

韓国観光公社のコキャンピング(GoCamping)APIで全国のキャンプ場を検索する。2026-09-21 に検証環境から接続し、`basedList` と `searchList` の両方で `SERVICE_KEY_IS_NULL` を確認した。実キーでの実データ取得は未検証。

データは韓国語。旅行者に伝えるときはエージェントが日本語に訳して渡す。

## キーと公式資料

無料の serviceKey を申請する: https://www.data.go.kr/data/15101933/openapi.do

## 基本の流れ

一覧:

```bash
curl -s -m 30 "http://apis.data.go.kr/B551011/GoCamping/basedList?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&numOfRows=20"
```

キーワード検索(韓国語キーワードをURLエンコード。例は 설악=雪岳):

```bash
curl -s -m 30 "http://apis.data.go.kr/B551011/GoCamping/searchList?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&keyword=%EC%84%A4%EC%95%85"
```

## レスポンスの読み方

各 item の `facltNm`(施設名), `addr1`, `doNm` / `sigunguNm`(道・市郡区), `induty`(業態: 一般キャンプ場・オートキャンプ場・グランピング等), `tel`, `mapX`, `mapY` を読む。

## 注意

このAPIは照会のみ。予約は各キャンプ場の公式窓口で行う。夏場と週末はすぐ満室になる。施設の営業状態(休業・台風被害など)は公式告知で最終確認する。

## エラー・失敗時の対応

- `SERVICE_KEY_IS_NULL`: キー未指定または無効。
- 空の `items`: キーワードは韓国語で入れる。日本語やローマ字ではヒットしない。
- `searchList` のキーワードはパーセントエンコード必須。

## English summary

Searches campsites across Korea through the official GoCamping API (list and Korean keyword search). Endpoint existence was confirmed by the expected auth error on 2026-09-21; real-key data was not exercised. Lookups only; booking happens at each campsite's official channel.
