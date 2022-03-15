from bs4 import BeautifulSoup
import requests
import urllib.parse as urlparser

def naver_related(keyword):
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="+urlparser.quote(keyword)
    response = requests.get(url)
    dom = BeautifulSoup(response.text, "html.parser")
    elements = dom.select("#nx_related_keywords li > a")
    data = [
        element.text.strip()
        for element in elements
    ]
    return data

    while True:
        keyword = input('검색어 입력 : ')
        if keyword.lower()=='quit' : break
        print(naver_related(keyword))
