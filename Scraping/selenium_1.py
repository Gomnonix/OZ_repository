from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

url = "https://www.naver.com/"

driver.get(url)
time.sleep(3)

title = driver.title
#print(title) 
#selenium 브라우저를 켜야만 코드를 진행하기 때문에 느리다.
#Beatufulsoup과 함께 적절히 사용해야한다.

html = driver.page_source 
print(html)