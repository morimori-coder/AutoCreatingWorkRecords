from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time

# LoginInfo.txtからログイン情報を取得
jsonData = open('LoginInfo.json', 'r', encoding='utf=8')
loginInfo = json.load(jsonData)

# LoginInfo.txtはクローズ
jsonData.close()

# chrome driverでGoogle Chromeを開く
driver = webdriver.Chrome(executable_path = loginInfo["chromeDriver"])

# ログインしたいページのURLを入力する
driver.get(loginInfo["url"])
time.sleep(3)

# ID,パスワードを入力する
loginID = driver.find_element_by_id("username")
loginID.send_keys(loginInfo["id"])
loginPass = driver.find_element_by_id("password")
loginPass.send_keys(loginInfo["password"])

# seleniumで対象のページへログインする
loginButton = driver.find_element_by_id('Login')
loginButton.click()

time.sleep(4)
# 勤務表タブをクリック
# 前月リンクをクリック
# 月次サマリーをクリック
# Ctrl + Sを実行
# 勤務表.html としてローカルに保存
# 勤務表.htmlをbeautifulsoupで開く
# 勤務表の要素を取得する
# 取得した要素の値を利用し、Excelを作成する（この辺りは今後やり方を調べる）
