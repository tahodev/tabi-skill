---
name: seoul-wifi
description: ソウル市の公共Wi-Fi設置場所を住所・施設名・座標から探す。公開サンプルキーで動作確認でき、無料APIキーで全件取得できる。
license: MIT
metadata:
  category: travel
  locale: ja-JP
---

# seoul-wifi

ソウルオープンデータ広場の `TbPublicWifiInfo` APIで公共Wi-Fiの設置場所を調べる。2026-09-19 に公開 `sample` キーで実データを取得し、`INFO-000` と総件数26,286件を確認した。総件数は変動する観測値。

公式データ: https://data.seoul.go.kr/dataList/OA-20883/A/1/datasetView.do

## 基本の流れ

```bash
# 公開サンプル(最大5件)
curl -s -m 30 "http://openapi.seoul.go.kr:8088/sample/json/TbPublicWifiInfo/1/5/"

# 無料発行キーでページング
curl -s -m 30 "http://openapi.seoul.go.kr:8088/{SEOUL_KEY}/json/TbPublicWifiInfo/1/1000/"
```

主な項目:
- `X_SWIFI_MAIN_NM`: 設置場所名
- `X_SWIFI_ADRES1`, `X_SWIFI_ADRES2`: 道路名住所・詳細
- `X_SWIFI_WRDOFC`: 区
- `LAT`, `LNT`: 緯度・経度
- `X_SWIFI_INSTL_FLOOR`, `X_SWIFI_INSTL_TY`: 階・設置種別
- `WORK_DTTM`: データ更新時刻

API側の名称検索はないため、ページング後に場所名・住所で部分一致する。現在地から探す場合は座標距離を計算する。

## 注意

掲載されていても電波停止・移設の場合がある。接続には端末のWi-Fi設定を使い、個人情報を扱う通信では暗号化されていないネットワークを避ける。

## エラー・失敗時の対応

- `INFO-000` 以外はキーとURL順序を確認する。
- サンプルキーは5件まで。全件は実キーで1,000件ずつ取得する。
- 座標や稼働状態を推測しない。

## English summary

Looks up official Seoul public Wi-Fi locations via TbPublicWifiInfo. Verified with the public sample key on 2026-09-19 (INFO-000, real rows; observed total 26,286). Filter locally by place/address or distance. Availability can change.
