import requests
from bs4 import BeautifulSoup

url = "http://naver.com"

req = requests.get(url)
print(req)

html = req.text
# print(html)

soup = BeautifulSoup(html, "html.parser") #클래스 형식으로 사용, 트리 구조를 만드는데 사용
# print(soup)

query = soup.select_one(".search_input_box") #class . | ID #
print(query)