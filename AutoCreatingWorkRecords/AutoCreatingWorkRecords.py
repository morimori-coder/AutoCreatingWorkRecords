from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import GetJson
import time
import const

loginInfo = GetJson.get_json_data(const.LOGIN_INFO)

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

elementsNames = GetJson.get_json_data(const.ELEMENTS_NAME)

# 勤務表を開く
workRecordTab = driver.find_element_by_id(elementsNames["workedRecord"])
workRecordTab.click()
time.sleep(2)

# 月次サマリーをクリック
monthSummery = driver.find_element_by_class_name(elementsNames['monthlySum'])
monthSummery.click()
time.sleep(2)

driver.quit()




# Ctrl + Sを実行
# 勤務表.html としてローカルに保存
# 勤務表.htmlをbeautifulsoupで開く
# 勤務表の要素を取得する
# 取得した要素の値を利用し、Excelを作成する（この辺りは今後やり方を調べる）
