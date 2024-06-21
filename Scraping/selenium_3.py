from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests

# Service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=Service)
url = "https://section.cafe.naver.com/ca-fe/home"

# driver.get(url)
# time.sleep(3)
# html = driver.page_source #driver에 pag_source를 가져와줘

req = requests.get(url)
html = req.text
print(html)


