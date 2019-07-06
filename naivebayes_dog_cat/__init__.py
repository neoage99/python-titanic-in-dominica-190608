from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
context = './data/'
driver = webdriver.Chrome(context+'chromedriver')
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)