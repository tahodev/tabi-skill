# セキュリティポリシー / Security Policy

## 脆弱性の報告 / Reporting a vulnerability

公開issueやPRに脆弱性の詳細や秘密情報を貼らないでください。GitHubの非公開脆弱性報告(このリポジトリの Security タブの "Report a vulnerability")を使ってください。
Do not post vulnerability details or secrets in public issues or pull requests. Use GitHub private vulnerability reporting (the Security tab's "Report a vulnerability").

## APIキー / API keys

- 多くのスキル(TourAPI・TAGO・気象庁・ソウルオープンデータ広場・ECOS など)は、利用者自身が発行する無料APIキーが必要です。キーは環境変数か安全なストレージに置き、リポジトリ・issue・PR・CIログ・回答に含めないでください。
  Many skills (TourAPI, TAGO, KMA, Seoul Open Data Plaza, ECOS) require the user's own free API key. Keep keys in environment variables or secure storage - never in the repo, issues, PRs, CI logs or replies.
- commit・issue・CIログにキー文字列を見つけた場合は、報告のうえ発行元で失効・再発行してください。
  If you find a key string in any commit, issue or CI log, report it, then revoke and reissue it at the issuer.
- 本リポジトリのスキルは照会と計算だけを行い、外部の状態を変更せず、ログインも要求しません。
  The skills here only look up and compute. They change no external state and require no login.

## 範囲 / Scope

ドキュメントやスクリプト中の脆弱性(キーを漏洩させる例、予期しないコマンドを実行する例など)が対象です。第三者の政府データソース自体の問題は、提供機関に報告してください。災害・医療・税に関する結果を、唯一の判断根拠にしないでください。
Vulnerabilities in this repo's documents and scripts (examples that leak keys or run unexpected commands) are in scope. Report problems in third-party government data sources to the providing agency. Do not use disaster, medical or tax results as the sole basis for decisions.
