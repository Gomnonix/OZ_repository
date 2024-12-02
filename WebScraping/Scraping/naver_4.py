import requests
from bs4 import BeautifulSoup

header_user = {"User=Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
keyword = input("검색어를 하나만 입력해주세요 ")

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")