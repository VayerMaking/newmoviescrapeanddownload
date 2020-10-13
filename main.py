import requests
from requests import Session
from lxml import etree
from bs4 import BeautifulSoup
import lxml.html as lh
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
import config
from selenium.common.exceptions import NoSuchElementException
import os
import subprocess

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=r'/usr/bin/chromedriver')
movie_name = "man in black"
movie_name = movie_name.replace(' ', '+').lower()
url = "https://zamunda.net/catalogs/movies?letter=&t=movie&search=" + movie_name + "&field=name&comb=yes"
driver.get(url)

username = driver.find_element_by_name("username")
username.clear()
username.send_keys(config.username)

password = driver.find_element_by_name("password")
password.clear()
password.send_keys(config.password)

driver.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/form/table/tbody/tr[3]/td/input").click()

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def newest_movies():
    movies_page = requests.get("https://www.moviefone.com/movies/")
    soup_title = BeautifulSoup(movies_page.content, 'html.parser')
    titles = soup_title.find_all('a',attrs={'class' :  'hub-movie-title'},limit=3)
    first_movie, second_movie, third_movie = titles[0].text, titles[1].text, titles[2].text
    newest_movies_ = [first_movie, second_movie, third_movie]

    return newest_movies_

def seach_if_those_movies_are_avaible(movie_name):
    movie_name = movie_name.replace(' ', '+').lower()
    url = "https://zamunda.net/catalogs/movies?letter=&t=movie&search=" + movie_name + "&field=name&comb=yes"
    driver.get(url)
    movie_dict = {}
    movie_tables = ["2","3","4","5","6"]
    i = 2
    i = str(i)

    for i in movie_tables:
        xpath_size = "/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[" + i + "]/td[2]/table[2]/tbody/tr[2]/td[5]"                        #/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td[5]/font
        is_there_movie = check_exists_by_xpath(xpath_size)
        if is_there_movie == True:
            size = driver.find_element_by_xpath(xpath_size)
            print(size.text)
            a = str(size.text)
            a = a[:-3]
            i = int(i)
            a = float(a)
            movie_dict.update({i : a})
            i=i+1

            print(movie_dict)
            sorted_movies = sorted(movie_dict.items(), key=lambda x: x[1])
            print(sorted_movies[0][1])
            k = str(sorted_movies[0][0])
            print(k)
            xpath_index = "/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[" + k + "]/td[1]/a"
            index = driver.find_element_by_xpath(xpath_index)
            index.click()
            xpath_title = "/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[" + k + "]/td[2]/table[1]/tbody/tr/td[1]/a"
            title = driver.find_element_by_xpath(xpath_title)
            title2 = title.text
            title2 = str(title2)
            print(title2)
        else:
            print("the movie isn`t avaiable in zamunda")

j = newest_movies()
print(j)
for i in j:
    print(i)
    seach_if_those_movies_are_avaible(i)
#seach_if_those_movies_are_avaible("Hard Kill")
p = subprocess.Popen(['./torrent_send.sh'])
sts = os.waitpid(p.pid, 0)
driver.quit()
