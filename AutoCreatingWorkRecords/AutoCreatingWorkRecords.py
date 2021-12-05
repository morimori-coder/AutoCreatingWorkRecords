import json

# LoginInfo.txtからログイン情報を取得
jsonData = open('LoginInfo.json', 'r', encoding='utf=8')
loginInfo = json.load(jsonData)

# LoginInfo.txtはクローズ
jsonData.close()

# chrome driverでGoogle Chromeを開く
# ログインしたいページのURLを入力する
# ID,パスワードを入力する
# seleniumで対象のページへログインする
# 勤務表タブをクリック
# 前月リンクをクリック
# 月次サマリーをクリック
# Ctrl + Sを実行
# 勤務表.html としてローカルに保存
# 勤務表.htmlをbeautifulsoupで開く
# 勤務表の要素を取得する
# 取得した要素の値を利用し、Excelを作成する（この辺りは今後やり方を調べる）
