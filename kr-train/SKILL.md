---
name: kr-train
description: KTX・ITXなど韓国の列車の時刻・運賃を国土交通部(TAGO)列車情報APIで調べる。「ソウルから釜山までKTXは何時?」のような質問に対応。無料APIキーが必要。予約は扱わない。
license: MIT
metadata:
  category: transit
  locale: ja-JP
---

# kr-train

韓国の国土交通部 国家大衆交通情報センター(TAGO)の列車情報オープンAPIで、KTXなどの列車時刻・運賃を照会するスキル。2026-09-09 に3オペレーションの実在を確認済み(キーなしで叩いて認証エラーが返ることを確認)。

## キーの取得

公共データポータル(data.go.kr)で「TAGO 열차정보」に活用申請し、共通認証キー(serviceKey)を取得する(無料・通常は自動承認)。ポータル: https://www.data.go.kr/

## 基本の流れ

1. 出発・到着の駅IDを調べる(都市コード → 駅リスト)
2. 区間の列車時刻を照会する

### 1. 駅IDを調べる

```bash
# 都市コード一覧
curl -s "http://openapi.tago.go.kr/openapi/service/TrainInfoService/getCtyCodeList?serviceKey={KEY}"

# 都市コードから駅一覧(例: ソウル=11)
curl -s "http://openapi.tago.go.kr/openapi/service/TrainInfoService/getCtyAcctoTrainSttnList?serviceKey={KEY}&cityCode=11"
```

駅名の一部でも絞り込める。返ってくる `nodeid` が駅ID。

### 2. 列車時刻を照会する

```bash
curl -s "http://openapi.tago.go.kr/openapi/service/TrainInfoService/getStrtpntAlocFndTrainInfo?serviceKey={KEY}&depPlaceId=NAT010000&arrPlaceId=NAT050445&depPlandTime=20260910&trainGradeCode=00"
```

- `depPlandTime`: 出発日(yyyyMMdd)。時刻まで付けるとその時刻以降。
- `trainGradeCode`: 車種。`00`=KTX。`01`=セマウル、`02`=ムグンファ、`08`=ITX-セマウル、`09`=ITX-チュンチュン(TAGOの公開資料のコード体系)。
- レスポンス(XMLデフォルト)の各item: `depplandtime`/`arrplandtime`(発着時刻)、`traingradename`(車種名)、`trainno`(列車番号)、`adultcharge`(大人運賃・ウォン)。
- ソウル駅 `NAT010000`、釜山駅 `NAT050445` は主要例。他は駅一覧で確認する。

## 注意

- 照会のみ。予約・発券はKORAIL公式(コレイルトークアプリ等)で行う。エージェントが代行しない。
- 時刻・運賃は提供データそのまま。臨時ダイヤは反映されないことがある。
- 短時間に連続リクエストしない。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **`resultMsg` が `지원하지 않는 인증방식입니다`**: serviceKey が空か形式違い。キーを確認する。
- **`NO_OPENAPI_SERVICE_ERROR`**: URLのスペルミス。ベースは `openapi.tago.go.kr` であり、`apis.data.go.kr/1613000` ではない(2026-09-09時点)。
- **空のitems**: その日付・区間・車種の運行なし。車種指定を外して再照会する。
- 時刻を推測で作らない。

## English summary

Queries KTX and other Korean train times and fares via the Ministry of Land TAGO train API (3 operations verified live on 2026-09-09). Needs a free data.go.kr serviceKey. Look up station IDs by city code first, then query schedules between station IDs with an optional train-grade filter (00 = KTX). Read-only: no booking. The API host is openapi.tago.go.kr, not apis.data.go.kr.
