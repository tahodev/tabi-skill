---
name: korea-disaster-alert
description: 行政安全部の災難文字(재난문자)APIで、韓国国内で発令された緊急メッセージ(豪雨・台風・地震など)を照会する。無料APIキーが必要。
license: MIT
metadata:
  category: safety
  locale: ja-JP
---

# korea-disaster-alert

行政安全部(행정안전부)の再難安全データ共有プラットフォーム(재난안전데이터공유플랫폼)が出す災難文字メッセージを照会する。携帯に届く緊急速報と同じ系統のメッセージで、豪雨・台風・地震・土砂崩れなどの警報内容と対象地域が取れる。2026-09-21 に検証環境から接続し、キーなしで `resultCode 30`(SERVICE KEY IS NOT REGISTERED ERROR)が返ることを確認した。実キーでの実データ取得は未検証。

メッセージ本文は韓国語。旅行者に伝えるときはエージェントが日本語に訳して渡す。

## キーと公式資料

無料の serviceKey を申請する(データ番号228): https://www.safetydata.go.kr/disaster-data/view?dataSn=228

## 基本の流れ

```bash
curl -s -m 30 "https://www.safetydata.go.kr/V2/api/DSSP-IF-00247?serviceKey={KEY}&returnType=JSON&pageNo=1&numOfRows=10"
```

発令が新しい順に返る。`pageNo` と `numOfRows` でページングする。

## レスポンスの読み方

各 item の発令日時(`CRT_DT`)、対象地域(地域名を含むフィールド)、メッセージ本文(`MSG_CN`)を読む。本文には災害の種類と行動指針(避難・立入禁止など)が書かれている。旅行中の地域が対象に含まれるかを優先して確認する。

## 注意

災難文字は市区町村単位で出る。滞在先の行政区名(韓国語表記)を控えておくと照合しやすい。気象の注意報・警報そのものは `korea-weather-warning` を見る。このAPIは照会のみで、避難指示の最終判断は現地の案内に従う。

## エラー・失敗時の対応

- `resultCode 30`(SERVICE KEY IS NOT REGISTERED ERROR): キー未指定または無効。HTTP 200 で返るので本文の resultCode も確認する。
- 空の `body`: 発令中のメッセージがない平常時は空になりうる。`pageNo` を戻して履歴を見る。

## English summary

Reads Korea's official emergency cell-broadcast messages (typhoon, heavy rain, earthquake and similar alerts) via the Ministry of the Interior and Safety disaster-data platform. Endpoint existence was confirmed by the expected key error on 2026-09-21; real-key data was not exercised. Message bodies are Korean; translate before relaying to a traveler.
