# encoding:UTF-8
from selenium import webdriver
import time

driver = webdriver.Chrome(
    '/Users/oxxo/Documents/oxxo/practice/python/chromedriver')  # 設定 chromedriver 路徑
driver.get('https://www.dinbendon.net/do/login')  # 前往這個網址

# 輸入使用者 id
user = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[1]/td[2]/input')
user.send_keys('XXXXX')

# 輸入使用者密碼
pwd = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[2]/td[2]/input')
pwd.send_keys('XXXXX')

# 取得驗證碼訊息
checkquestion = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[1]')
check = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[2]/input')

# 計算驗證碼
checktext = checkquestion.text
if('加' in checktext):
    checktext = checktext.replace('等於', '')
    checktext = checktext.replace(' ', '')
    arr = checktext.split('加')
elif('＋' in checktext):
    checktext = checktext.replace('＝', '')
    checktext = checktext.replace(' ', '')
    arr = checktext.split('＋')
elif('+' in checktext):
    checktext = checktext.replace('=', '')
    checktext = checktext.replace(' ', '')
    arr = checktext.split('+')
result = int(arr[0])+int(arr[1])
print(checkquestion.text)
print(result)
check.send_keys(result) # 輸入驗證碼

# 點擊按鈕
btn = driver.find_element_by_xpath(
    ' //*[@id="signInPanel_signInForm"]/table/tbody/tr[5]/td[2]/input[1]')
btn.click()
# driver.close()
