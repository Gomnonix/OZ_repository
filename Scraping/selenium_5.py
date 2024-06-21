from selenium import webdriver #selenium 자체가 테스트가 목적
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True) #브라우저가 닫히지 않는다.

#화면 자동 설정 옵션
#options.add_argument("--start-maximized")
#options.add_argument("--start-fullscreen")
options.add_argument("window-size=500, 500")

#브라우저 창이 바로 나오지 않도록 설정하는 옵션(기능은 정상 작동함)
#options.add_argument("--headless")

#음소거 옵션 추가
#options.add_argument("--mute-audio")

#시크릿 모드
#options.add_argument("incognito")

#거슬리는 브라우저 상단 메세지 삭제(Web)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

#거슬리는 브랑우저 상단 메시지 삭제(터미널)
#options.add_experimental_option("excludeSwiches", ["enable-logging"]) #이거 왜 안되냐??

#브라우저 자동으로 종료되지 않는 옵션
driver = webdriver.Chrome(options=options)

url = "https://google.com"
driver.get(url)
time.sleep(3)

driver.quit()

