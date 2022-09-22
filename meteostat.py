from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import datetime
import shutil

# 날짜
current = datetime.datetime.now()
three_days_later = current + datetime.timedelta(days=3)
one_day_ago = current - datetime.timedelta(days=1)
current = str(current)[0:10]
three_days_later = str(three_days_later)[0:10]
one_day_ago = str(one_day_ago)[0:10]
print(f'current={current}')
print(f'three_days_later={three_days_later}')
print(f'one_day_ago={one_day_ago}')

# 폴더 삭제
def deleteFolder(directory):
  try:
    if os.path.exists(directory):
      shutil.rmtree(directory)
  except OSError:
      print('Error: Deleting directory.' + directory)

# 폴더 생성
def createFolder(directory):
  try:
    if not os.path.exists(directory):
      os.makedirs(directory)
  except OSError:
      print('Error: Creating directory.' + directory)

# 다운로드받을 경로에 맞게 설정 one_day_ago, current는 놔두고 앞에 경로에 맞게 수정
# one_day_ago, current는 날짜에 맞게 폴더가 생성됨
deleteFolder(f'C:/Users/Sun/Desktop/selenium_/csv/{one_day_ago}')
createFolder(f'C:/Users/Sun/Desktop/selenium_/csv/{current}')

# 다운로드받는 csv파일 원하는 경로에 맞게 설정 current는 놔두고 앞에 경로만 수정, 경로 뒤에 '\\' 이거 붙이고
# current 오늘 날짜에 맞는 폴더에 다운로드 함
download_path = 'C:\\Users\\Sun\\Desktop\\selenium_\\csv\\' + current

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", download_path)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

driver = webdriver.Firefox(options=options)
driver.implicitly_wait(3)
driver.get(f"https://meteostat.net/en/place/de/berlin-treptow?s=10389&t={current}/{three_days_later}")

notice_elem = "/html/body/div[1]/div[2]/div/div/div[3]/button[2]"
accept = driver.find_element_by_xpath(notice_elem)
if accept: 
  print(accept.text)
  accept.click()

export_elem = "/html/body/div/div/main/div/div/div/div[1]/div[1]/div[1]/button[1]"
export = driver.find_element_by_xpath(export_elem)
export.click()

select_elem = 'formatSelect'
select = driver.find_element_by_id(select_elem)
select.click()

csv_option_elem = '/html/body/div[1]/div/main/div/div/div/div[1]/div[3]/div[5]/div/div/div[2]/form/div/select/option[4]'
csv_option = driver.find_element_by_xpath(csv_option_elem)
csv_option.click()

save_button_elem = '/html/body/div[1]/div/main/div/div/div/div[1]/div[3]/div[5]/div/div/div[3]/button'
save_button = driver.find_element_by_xpath(save_button_elem)
print(f'Save={save_button.text}')
save_button.click()
