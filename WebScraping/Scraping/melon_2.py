from bs4 import BeautifulSoup
import requests

# 사이트 접속 -> F12 -> 네트워크 -> 헤더에서 User-Agent 정보 볼 수 있음
header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

base_url = "https://www.melon.com/chart/index.htm"
html = requests.get(url=base_url, headers=header_user).text

req = requests.get(base_url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

#print(soup.title)
#print(soup.h1)

#find 방식
# h1 = soup.find("h1")
# print(h1)

# logo = soup.find(class_="page_header")
# logo2 = soup.select_one(".page_header")
# print(logo)
# print(logo2)

nav = soup.find(class_ = "button_rbox", text="담기")
print(nav)

navs = soup.find_all(class_="button_rbox")
print(len(navs))

for i in navs:
    print(i.text)