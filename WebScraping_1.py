import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요 : ")

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".title_link")
authors = soup.select(".name")
adposts = soup.select(".view_wrap")

for item in adposts:
    isAd = item.select_one(".link_ad")

    if isAd == None:
        title = item.select(".title_link")
        name = item.select(".name")
        print("검색 키워드 : ", keyword)
        print("블로그 제목 : ", title[0].text)
        print("블로그 작성자 : ", name[0].text)
        print()

print(len(results))