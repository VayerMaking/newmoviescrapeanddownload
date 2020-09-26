import requests
from lxml import etree

page = requests.get("https://www.moviefone.com/movies/")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')



soup_title = BeautifulSoup(page.content, 'html.parser')
titles = soup_title.find_all('a',attrs={'class' :  'hub-movie-title'},limit=3)
print(titles)
first_movie, second_movie, third_movie = titles[0].text, titles[1].text, titles[2].text

print(first_movie)
print(second_movie)
print(third_movie)
