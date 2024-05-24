from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])


Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service, options=options)

url = "https://kream.co.kr/"
driver.get(url)

driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

# for i in range(5):
#     driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.3)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(0.3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner") #리스트 형태로 만들어진다 ex) [item1, item2. item3. ...]

for item in items:
    product_name = item.select_one(".translated_name")
    if "후드" in product_name:
        product_price = item.select_one(".amount").text
        print(product_name.text)
        print(product_price)

#driver.quit()
