import requests
from bs4 import BeautifulSoup

header_user = {"User=Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "http://naver.com"

req = requests.get(url, headers=header_user)
# print(req.raise_for_status)
print(req.request)

# print(req)
html = req.text
# print(html)
soup = BeautifulSoup(html, "html.parser")

