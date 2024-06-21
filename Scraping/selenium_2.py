from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

url = "https://www.naver.com/"

driver.get(url)
time.sleep(3)
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
query = soup.select_one(".search_input_box") #class . | ID #
print(query)
