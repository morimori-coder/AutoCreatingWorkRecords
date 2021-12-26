from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import GetJson
import time
import const
import bs4 
import pyautogui
import datetime
import re
import openpyxl

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

pyautogui.hotkey('ctrl','s')
time.sleep(2)
fine_name = datetime.datetime.now().strftime('%Y%m%d') + 'wordRecord.html'
pyautogui.typewrite(fine_name)
pyautogui.press("enter")
time.sleep(3)

#ローカルに保存した勤務表を開く
savePath = GetJson.get_json_data(const.SAVE_PATH)
soup = bs4.BeautifulSoup(open(savePath["folderPath"] + fine_name, encoding = 'utf-8'), 'html.parser')
#勤務表の要素を取得する
element = soup.find_all('tr', attrs = {'class' : re.compile('prtv.*')})

#B2にyyyy年mm月
#C5にyyyy年
#C6にmm月度
for row in element:
    print(row)
    #C14～には有給(全休)、有給(阪急)、欠勤、遅刻、早退のいずれか
    #Dは始業時間hh:mm
    #Eは退勤時間hh:mm
    #Fは休憩h:mm

driver.quit()




# Ctrl + Sを実行
# 勤務表.html としてローカルに保存
# 勤務表.htmlをbeautifulsoupで開く
# 勤務表の要素を取得する
# 取得した要素の値を利用し、Excelを作成する（この辺りは今後やり方を調べる）
