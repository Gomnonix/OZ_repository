from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)
base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="

keyword = input("검색어를 하나만 입력해주세요 :  ")

url = base_url + keyword

driver.get(url)
time.sleep(3)

# 스크롤 코드
# driver.execute_script("window.scrollTo(0, 10000)")
# time.sleep(2)

# 스크롤 페이지 끝까지 내리는 코드
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")  

results = soup.select(".title_link")
name = soup.select(".name")

for i in zip(results, name):
     print(i[0].text) #text가 없으면 링크(href)도 같이 온다
     print(i[1].text)
     print(i[0]['href'])
     print()

print(len(results))
    

