# スターターガイド

tabi-skill を初めて使う人向けに、旅行の目的別に4つのスキルパックと、5分で試せる手順、APIキーの発行ページをまとめました。各スキルの検証状態は [README の検証マトリクス](../README.md) と [検証ポリシー](verification.md) を参照してください。

## 5分クイックスタート

1. **インストール(1分)**: Node.js 18 以上と `npx` が使える環境で、まず「初めての韓国」パックを入れます。

   ```bash
   npx --yes skills add tahodev/tabi-skill --skill krw-jpy-rate --skill korea-weather --skill korea-holidays --skill incheon-airport --skill arex-timetable --skill kto-tour --skill korea-etiquette --skill korea-emergency -g
   ```

2. **キーなしで試す(1分)**: 次のスキルはAPIキーがなくても動きます。エージェントにそのまま聞いてみてください。
   - `arex-timetable`: 「仁川空港T1からソウル駅への直通列車、次は何時?」
   - `korea-emergency`: 「韓国で救急車を呼ぶ番号と、日本語で相談できる窓口は?」
   - `korea-etiquette`: 「韓国の食事で気をつけるマナーは?」

3. **サンプルキーで試す(1分)**: ソウル地下鉄とタルンイ(公共自転車)はサンプルキー `sample` で数件だけ実データが返ります。
   - `seoul-subway`: 「弘大入口駅の次の電車は?」
   - 本番利用は、下の表から無料キーを発行してください。

4. **公共データポータルのキーを取る(2分)**: 多くのスキルは公共データポータル(data.go.kr)の無料キー1つで動きます。会員登録して、使いたいAPIのページで「활용신청」(利用申請)を押すと、マイページに認証キー(serviceKey)が表示されます。APIごとに利用申請が必要ですが、キー自体は共通です。発行直後は反映まで時間がかかることがあります。

5. **キーを渡して聞く**: キーはエージェントとの会話で渡すか、自分の環境に置いてください。リポジトリやスクリーンショットに載せないでください。

## 目的別スキルパック

### 初めての韓国

出発前の準備と空港からの移動。

| スキル | 使いどころ | キー |
| --- | --- | --- |
| `krw-jpy-rate` | ウォンと円のレート確認 | ECOS / 韓国輸出入銀行 |
| `korea-weather` | 行き先の天気予報 | 公共データポータル |
| `korea-holidays` | 旅行日程と祝日・連休の重なり | 公共データポータル |
| `incheon-airport` | 仁川空港の発着便 | 公共データポータル |
| `arex-timetable` | 空港鉄道AREXの時刻表 | 不要 |
| `kto-tour` | 観光地を日本語で検索 | 公共データポータル |
| `korea-etiquette` | マナー・習慣 | 不要 |
| `korea-emergency` | 緊急連絡先 | 不要 |

```bash
npx --yes skills add tahodev/tabi-skill --skill krw-jpy-rate --skill korea-weather --skill korea-holidays --skill incheon-airport --skill arex-timetable --skill kto-tour --skill korea-etiquette --skill korea-emergency -g
```

### ソウル週末

ソウル市内の移動、混雑、グルメ、イベント。

| スキル | 使いどころ | キー |
| --- | --- | --- |
| `seoul-subway` | 地下鉄のリアルタイム到着 | ソウルオープンデータ広場 |
| `seoul-crowd` | 主要スポットのリアルタイム混雑 | ソウルオープンデータ広場 |
| `seoul-events` | ソウル市の文化イベント | ソウルオープンデータ広場 |
| `seoul-bike` | タルンイの貸出台数 | ソウルオープンデータ広場 |
| `seoul-wifi` | 公共Wi-Fiの場所 | ソウルオープンデータ広場 |
| `kto-food` | 飲食店を日本語で検索 | 公共データポータル |
| `kto-nearby` | 現在地周辺の観光スポット | 公共データポータル |
| `korea-weather` | 当日の天気 | 公共データポータル |

```bash
npx --yes skills add tahodev/tabi-skill --skill seoul-subway --skill seoul-crowd --skill seoul-events --skill seoul-bike --skill seoul-wifi --skill kto-food --skill kto-nearby --skill korea-weather -g
```

### 地方都市

釜山・慶州・全州など、ソウル以外への移動と観光。

| スキル | 使いどころ | キー |
| --- | --- | --- |
| `kr-train` | KTXなど列車の時刻・運賃 | 公共データポータル |
| `kr-bus` | 高速バスの時刻・運賃 | 公共データポータル |
| `kr-intercity-bus` | 市外バスの時刻・運賃 | 公共データポータル |
| `kr-city-bus` | 地方都市の市内バス到着 | 公共データポータル |
| `kr-metro` | 釜山・大邱などの地下鉄 | 公共データポータル |
| `kto-course` | 旅行コース | 公共データポータル |
| `kto-festival` | 地域の祭り | 公共データポータル |
| `kto-stay-detail` | 宿の設備・チェックイン時刻 | 公共データポータル |
| `korea-tourist-site` | 観光地の営業時間・料金 | 公共データポータル |

```bash
npx --yes skills add tahodev/tabi-skill --skill kr-train --skill kr-bus --skill kr-intercity-bus --skill kr-city-bus --skill kr-metro --skill kto-course --skill kto-festival --skill kto-stay-detail --skill korea-tourist-site -g
```

### 緊急・安全

体調不良、災害、天候の急変に備える。

| スキル | 使いどころ | キー |
| --- | --- | --- |
| `korea-emergency` | 救急・警察・大使館の連絡先 | 不要 |
| `korea-disaster-alert` | 発令中の災難文字(緊急メッセージ) | 行政安全部 災害安全データ |
| `korea-weather-warning` | 注意報・警報 | 公共データポータル |
| `korea-pharmacy` | 近くの薬局 | 公共データポータル |
| `korea-hospital` | 近くの病院 | 公共データポータル |
| `korea-air-quality` | PM2.5・大気質 | 公共データポータル |
| `korea-uv-index` | 紫外線指数 | 公共データポータル |

```bash
npx --yes skills add tahodev/tabi-skill --skill korea-emergency --skill korea-disaster-alert --skill korea-weather-warning --skill korea-pharmacy --skill korea-hospital --skill korea-air-quality --skill korea-uv-index -g
```

## APIキー発行ページ

発行はどれも無料です。キーはリポジトリにコミットしないでください。

| 発行元 | 発行ページ | 使うスキル |
| --- | --- | --- |
| 公共データポータル(data.go.kr) | https://www.data.go.kr/ (APIごとのページで「활용신청」。例: TourAPI日本語サービス https://www.data.go.kr/data/15101578/openapi.do ) | kto-*、kr-train、kr-bus、kr-intercity-bus、kr-city-bus、kr-metro、korea-weather、korea-weather-midterm、korea-weather-warning、korea-holidays、korea-air-quality、korea-uv-index、korea-pharmacy、korea-hospital、korea-beach、korea-camping、korea-trail、incheon-airport、全国標準データ系(korea-public-toilet、korea-parking、korea-museum、korea-tourist-site、korea-cultural-festival) |
| ソウルオープンデータ広場 | https://data.seoul.go.kr/ (動作確認はサンプルキー `sample`) | seoul-subway、seoul-bike、seoul-events、seoul-crowd、seoul-wifi |
| 行政安全部 災害安全データ共有プラットフォーム | https://www.safetydata.go.kr/disaster-data/view?dataSn=228 | korea-disaster-alert |
| 韓国銀行 ECOS | https://ecos.bok.or.kr/ (動作確認はサンプルキー `sample`) | krw-jpy-rate |
| 韓国輸出入銀行 | https://www.data.go.kr/data/3068846/openapi.do (海外IPからは接続が遮断される場合あり) | krw-jpy-rate |
| 不要 | - | arex-timetable、korea-emergency、korea-etiquette |

各APIの正確な申請名は、それぞれの SKILL.md の「キーの取得」を参照してください。
