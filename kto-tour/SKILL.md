---
name: kto-tour
description: 韓国観光公社 TourAPI 4.0 の日本語サービス(JpnService2)で観光地・祭り・宿・飲食店を日本語のまま検索する。「明洞の近くの観光地は?」「ソウルの祭りは?」に対応。無料APIキーが必要。
license: MIT
metadata:
  category: tourism
  locale: ja-JP
---

# kto-tour

韓国観光公社(한국관광공사)の TourAPI 4.0 は**日本語版サービス(JpnService2)がある**のが最大の特徴で、観光スポットの名前も説明も日本語で返ってくる。このリポジトリの目玉スキル。2026-09-09 に6オペレーションの実在を確認済み。

## キーの取得

公共データポータル(data.go.kr)で「한국관광공사 관광정보」(B551011)に活用申請し、serviceKey を取得する(無料・通常は自動承認)。登録ページ: https://www.data.go.kr/data/15101578/openapi.do

## ベースURL

```
http://apis.data.go.kr/B551011/JpnService2
```

`JpnService2` が日本語。他に `KorService2`(韓国語)、`EngService2`(英語)などがある。共通パラメータ: `serviceKey`, `MobileOS=ETC`, `MobileApp=tabi`, `_type=json`。

## よく使うオペレーション

```bash
# 地域コード一覧(シド別)
curl -s "http://apis.data.go.kr/B551011/JpnService2/areaCode2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json"

# 地域×ジャンルの観光地リスト(例: ソウル=1, 観光地=12)
curl -s "http://apis.data.go.kr/B551011/JpnService2/areaBasedList2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&areaCode=1&contentTypeId=12&numOfRows=10"

# キーワード検索(日本語キーワード可)
curl -s "http://apis.data.go.kr/B551011/JpnService2/searchKeyword2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&keyword=明洞"

# 開催中の祭り(例: 2026年9月)
curl -s "http://apis.data.go.kr/B551011/JpnService2/searchFestival2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&eventStartDate=20260901"

# 詳細(contentIdは検索結果から)
curl -s "http://apis.data.go.kr/B551011/JpnService2/detailCommon2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&contentId=126508"
curl -s "http://apis.data.go.kr/B551011/JpnService2/detailIntro2?serviceKey={KEY}&MobileOS=ETC&MobileApp=tabi&_type=json&contentId=126508&contentTypeId=12"
```

## コード早見

- **地域コード(areaCode)**: 1=ソウル, 2=仁川, 6=釜山, 39=済州。一覧は `areaCode2` で。
- **ジャンル(contentTypeId)**: 12=観光地, 14=文化施設, 15=祭り・イベント, 28=レポーツ, 32=宿泊, 38=ショッピング, 39=飲食店。

## レスポンスの読み方

`response.body.items.item[]` の各要素に `title`(日本語名), `addr1`(住所), `contentid`, `contenttypeid`, `firstimage`(画像URL)などが入る。検索結果の `contentId` を `detailCommon2` / `detailIntro2` に渡して詳細(概要・営業時間・休みなど)を取る。住所や名称は日本語で返るが、翻訳品質はまちまちなので原文ママと伝える。

## 注意

- データは韓国観光公社の登録情報そのまま。古い施設情報(閉店・休業)が残っていることがある。営業時間など重要情報は施設の公式案内で再確認するよう旅行者に伝える。
- 祭りの開催期間は `eventstartdate`/`eventenddate` で確認する。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **HTTP 401 `SERVICE_KEY_IS_NULL`**: serviceKey 未指定・不正。
- **`NO_OPENAPI_SERVICE_ERROR`**: サービス名のミス。日本語は `JpnService2`。
- **空のitems**: キーワードがヒットしない。日本語でダメなら韓国語キーワードでも試す(KorService2に切り替える手もある)。
- 施設情報を推測で補わない。

## English summary

Searches Korean tourism data (attractions, festivals, lodging, restaurants) in Japanese via the Korea Tourism Organization TourAPI 4.0 Japanese service, JpnService2 - 6 operations verified live on 2026-09-09. Free data.go.kr serviceKey required. Key codes: areaCode 1=Seoul, 2=Incheon, 6=Busan, 39=Jeju; contentTypeId 12=attraction, 14=culture, 15=festival, 32=lodging, 38=shopping, 39=restaurant. Names and descriptions come back in Japanese. Read-only lookup.
