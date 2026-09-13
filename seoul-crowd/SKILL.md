---
name: seoul-crowd
description: ソウル市のリアルタイム都市データAPIで、主要スポット(明洞・弘大・光化門など)の現在の混雑度を照会する。「いま明洞は混んでる?」に対応。混雑レベル・人口推計・予測に加え、同じ地点の天気・地下鉄・バス状況も取れる。無料APIキー(サンプルキーで即動作確認できる)。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# seoul-crowd

ソウルオープンデータ広場の「ソウル市リアルタイム都市データ」API(citydata)で、ソウル市内の主要スポット(핫스팟)の**リアルタイム混雑状況**を照会するスキル。2026-09-14 にサンプルキーで**実データ取得を実測確認**済み(INFO-000、광화문·덕수궁 の実データが返った)。

週末・イベント時の「あそこ混んでる?」に答える用途。過去・将来の混雑は扱わない。

## キーの取得

ソウルオープンデータ広場(data.seoul.go.kr)で利用申請すると即時発行される(無料)。サービス案内: https://data.seoul.go.kr/SeoulRtd/

## 基本の流れ

### 1. サンプルキーで動作確認(実測済み)

```bash
curl -s -m 30 "http://openapi.seoul.go.kr:8088/sample/json/citydata/1/1/%EA%B4%91%ED%99%94%EB%AC%B8%EA%B4%91%EC%9E%A5"
```

- **注意(実測済み)**: サンプルキーは地点名を変えても常に同じサンプル地点(광화문·덕수궁, POI009)が返る。別の地点の確認には実キーが必要。

### 2. 実キーで地点指定

```bash
curl -s -m 30 "http://openapi.seoul.go.kr:8088/{SEOUL_KEY}/json/citydata/1/5/{AREA_NM}"
```

- パスの末尾 `{AREA_NM}` に地点名(韓国語、URLエンコード)。実キーではソウル市が公開する主要地点(明洞・弘大・江南駅・光化門など)が取れる。地点名はソウル市のサービス案内ページ(上記)で確認する。

## 読み方

- `CITYDATA.AREA_NM` / `AREA_CD`: 地点名とコード(例: POI009)。
- `CITYDATA.LIVE_PPLTN_STTS[0]`: 混雑の主役。
  - `AREA_CONGEST_LVL`: 混雑レベル(여유=余裕, 보통=普通, 약간 붐빔=やや混雑, 붐빔=混雑)。旅行者にはこの4段階で伝える。
  - `AREA_CONGEST_MSG`: 状況の一文説明(韓国語)。翻訳してそのまま伝えてよい。
  - `AREA_PPLTN_MIN` / `AREA_PPLTN_MAX`: 推定滞在人口のレンジ。`PPLTN_TIME`: データ時刻。
  - `FCST_PPLTN`: 時間帯別の混雑予測(FCST_YN が Y のとき)。
- 同じ地点の周辺データも一緒に返る: `WEATHER_STTS`(天気), `SUB_STTS` / `LIVE_SUB_PPLTN`(最寄り地下鉄), `BUS_STN_STTS` / `LIVE_BUS_PPLTN`(バス), `PRK_STTS`(駐車場), `ROAD_TRAFFIC_STTS`(道路), `CHARGER_STTS`(EV充電), `EVENT_STTS`(イベント)。混雑の文脈で一緒に答えられる。

## 実レスポンス例(2026-09-14 サンプルキーで実測取得、抜粋)

```json
{"CITYDATA":{"AREA_NM":"광화문·덕수궁","AREA_CD":"POI009","LIVE_PPLTN_STTS":[{"AREA_CONGEST_LVL":"여유","AREA_CONGEST_MSG":"사람이 몰려있을 가능성이 낮고 붐빔은 거의 느껴지지 않아요. 도보 이동이 자유로워요."}]}}
```

## 注意

- 混雑レベルはソウル市の推計モデルの出力。実際の体感とずれることがある。特にイベント直後は `EVENT_STTS` も確認する。
- サンプルキーの地点固定(광화문·덕수궁)に注意。「명동을 조회했다」つもりで 광화문·덕수궁 のデータを答えない。応答の `AREA_NM` を必ず確認する。
- 数値・レベルを推測で答えない。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **`RESULT.CODE` が `INFO-000` 以外**: `INFO-200` は認証エラー(キー未指定・無効)。`ERROR-335` はサンプルキーで5件超を要求した。
- **該当地点が返らない**: 地点名の表記ゆれ。ソウル市の案内ページの正式名称で再試行する。
- 応答の `PPLTN_TIME` が古い(数時間前)場合は「データが古い」可能性を伝える。

## English summary

Fetches realtime crowd conditions for Seoul's major hotspots (Myeongdong, Hongdae, Gwanghwamun, ...) from the Seoul Open Data Plaza "Seoul realtime city data" API (citydata) - verified live with the public `sample` key on 2026-09-14 (INFO-000, real Gwanghwamun data). The sample key is pinned to one sample area (광화문·덕수궁) regardless of the area name you pass - always check AREA_NM in the response; a real instantly-issued key from data.seoul.go.kr unlocks all hotspots. Report the 4-level congestion scale (여유/보통/약간 붐빔/붐빔) and AREA_CONGEST_MSG; the same response also carries weather, subway, bus, parking, and event status for the area. Never invent congestion levels.
