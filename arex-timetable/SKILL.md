---
name: arex-timetable
description: 空港鉄道AREX公式サイトの公開時刻表で、ソウル駅と仁川空港T1/T2間の直通列車時刻を調べる。APIキー不要。
license: MIT
metadata:
  category: transit
  locale: ja-JP
---

# arex-timetable

空港鉄道(AREX)公式サイトが公開する直通列車の時刻表を照会する。公式ページは2026-09-19 に検証環境から取得でき、平日・休日の時刻表データを確認した。キー不要。公式ページをその都度読む方式なので、固定時刻をこのスキルに複製しない。

公式時刻表: https://www.arex.or.kr/express/info.do?menuNo=MN201503300000000002&langCd=en_US&device=Normal

## 基本の流れ

1. 公式ページを取得する。
2. 利用日が平日か休日かを確認する。
3. 方向(ソウル駅発 / 空港T2発)と乗降駅(T1/T2)に合う列を読む。
4. 出発時刻だけでなく到着時刻も伝える。

ページの表は概ね「ソウル駅発 → T1 → T2」と「T2発 → T1 → ソウル駅」の組で並ぶ。取得時点の例を答えに固定せず、毎回現行表を確認する。

## 注意

運休・臨時変更はリアルタイム列車情報と駅掲示を優先する。一般列車は全駅停車で、直通列車とは時刻・運賃が異なる。予約や発券は扱わない。

## エラー・失敗時の対応

- 公式ページを取れない場合は時刻を推測しない。駅掲示かAREX案内(1599-7788)を案内する。
- 曜日区分と方向を取り違えない。
- `odp.airport.kr` の空港鉄道APIは検証環境から接続タイムアウトしたため、このスキルでは使わない。

## English summary

Reads the current official AREX Express timetable page for Seoul Station and Incheon Airport T1/T2. The page and weekday/holiday table data were reachable on 2026-09-19. No key required; do not hard-code times. The separate odp.airport.kr API was unreachable from the verification environment.
