---
name: korea-weather-midterm
description: 韓国気象庁(KMA)の中期予報APIで、3〜10日先の天気の見通し(曇り/雨の予報と気温の範囲)を照会する。「来週のソウル旅行、傘いる?」に対応。無料APIキーが必要。
license: MIT
metadata:
  category: weather
  locale: ja-JP
---

# korea-weather-midterm

気象庁(기상청, KMA)の中期予報照会サービス(MidFcstInfoService)で、発表から3〜10日先の天気の見通しを照会するスキル。2026-09-14 に2オペレーションの**エンドポイント実在**を確認済み(キーなしで叩き、404ではなく認証エラーが返ることを確認。実キーでのデータ応答はまだ未検証)。

短期(当日〜2日)は [korea-weather](../korea-weather/SKILL.md)、注意報・警報は [korea-weather-warning](../korea-weather-warning/SKILL.md) 参照。

## キーの取得

公共データポータル(data.go.kr)で「기상청_중기예보 조회서비스」(MidFcstInfoService)に活用申請し、serviceKey を取得する(無料)。ポータル: https://www.data.go.kr/

## 基本の流れ

### 1. 陸上天気の見通し(getMidLandFcst)

```bash
curl -s "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst?serviceKey={KEY}&pageNo=1&numOfRows=10&dataType=JSON&regId=11B00000&tmFc=${TM_FC}"
```

- `regId` は中期予報区画コード。ソウル·仁川·京畿は `11B00000`。他の区画コードは気象庁の活用ガイドの別表参照。
- `tmFc` は発表時刻(YYYYMMDDHHMM)。1日2回(06時・18時)発表。直近の発表時刻を使う。
- 3日後〜10日後の午前/午後の天気(맑음, 구름많음, 흐리고 비 など)と降水確率(%)が返る。

### 2. 気温の見通し(getMidTa)

```bash
curl -s "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidTa?serviceKey={KEY}&pageNo=1&numOfRows=10&dataType=JSON&regId=11B10101&tmFc=${TM_FC}"
```

- `regId` は都市コード(ソウルは `11B10101`)。3〜10日後の最低/最高気温の予報値が返る。

## 注意

- 中期予報は「見通し」。短期予報より精度が落ちる。旅行の服装・傘の目安には使えるが、直前には korea-weather(短期)で再確認するよう伝える。
- `tmFc` を古いままにすると空応答になる。発表時刻は毎日06時・18時。
- 応答の天気表現(韓国語)は日本語に訳して伝える(흐리고 비 = 曇り時々雨 など)。

## エラー・失敗時の対応

- `curl` には必ず `-m 30` を付ける。
- **HTTP 401 / 認証エラー**: serviceKey 未指定・不正。
- **`NO_DATA` / 空のitems**: `tmFc` が発表時刻とずれている。直近の06時か18時に合わせる。
- 予報内容を推測で補わない。

## English summary

Fetches the KMA mid-range outlook (3-10 days out) from the MidFcstInfoService - endpoint existence verified on 2026-09-14 (unauthenticated probes return auth errors, not 404; not yet exercised with a real key). Free data.go.kr serviceKey required. getMidLandFcst gives AM/PM sky conditions and precipitation probability by region code (Seoul/Incheon/Gyeonggi = 11B00000), getMidTa gives forecast min/max temperatures by city code (Seoul = 11B10101); both need a recent tmFc issue time (daily at 06:00 and 18:00). Use for trip packing guidance; re-check with korea-weather (short-term) close to the date. Never invent forecast content.
