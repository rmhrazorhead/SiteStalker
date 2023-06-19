import requests

url = 'https://www.warhammer-community.com/warhammer-40000-downloads/'
# url = 'https://google.com'
r = requests.get(url)
# print(r.text)



# import urllib.request as r
# page = r.urlopen(url)
# print(page.read())

acceptButtonId = "onetrust-accept-btn-handler"


from bs4 import BeautifulSoup
from selenium import webdriver
import lxml

# dr = webdriver.Chrome()
# dr.get(url)
# # dr.get("https://www.mobile.de/?lang=en")
# bs = BeautifulSoup(dr.page_source,"lxml")
# print(bs.prettify())

# print(bs.title.string)

import dryscrape

sess = dryscrape.Session()
# sess.visit('https://pythonprogramming.net/parsememcparseface/')
sess.visit(url)
source = sess.body()

soup = BeautifulSoup(source,'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)