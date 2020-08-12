import requests
from bs4 import BeautifulSoup


def start_crawling():
    res = requests.get()
    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.find('title')
    print(title.get_text())
