import requests
from requests import Session
from lxml import etree
from bs4 import BeautifulSoup
import lxml.html as lh

def newest_movies():

    movies_page = requests.get("https://www.moviefone.com/movies/")

    soup_title = BeautifulSoup(movies_page.content, 'html.parser')
    titles = soup_title.find_all('a',attrs={'class' :  'hub-movie-title'},limit=3)
    print(titles)
    first_movie, second_movie, third_movie = titles[0].text, titles[1].text, titles[2].text

    print(first_movie)
    print(second_movie)
    print(third_movie)

    return first_movie, second_movie, third_movie

def seach_if_those_movies_are_avaible(movie_name):
    movie_name = movie_name.replace(' ', '+').lower()
    url = "https://zamunda.net/catalogs/movies?letter=&t=movie&search=" + movie_name + "&field=name&comb=yes"
    print(url)
    zamunda_page = requests.get(url)

    soup = BeautifulSoup(zamunda_page.content, 'html.parser')
    #titles = soup_title.find("body").find_all("div", limit = 4).find("div").find("table").find("tbody").find("tr").find("td").find("table").find("tbody").find("tr").find("td").find("center").find("b").find("b").find_all("table", limit = 4).find("tbody").find_all("tr", limit = 2)
    with Session() as s:
        site = s.get("https://zamunda.net/")
        bs_content = BeautifulSoup(site.content, "html.parser")
        #token = bs_content.find("input", {"name":"csrf_token"})["value"]
        login_data = {"username":"mvayer","password":"ju4kaku4ka"}
        s.post("https://zamunda.net/",login_data)
        home_page = s.get("https://zamunda.net/")
        #print(home_page.content)
        table = bs_content.find_all('table',attrs={'class' :  'mainouter'})[0].find_all('table',attrs={'class' :  'bottom'})[0]#.find_all('table')
        print(table)



    #table2 = table.find('table',attrs={'class' :  'bottom'})
    #table3 = table2.find('table',attrs={'cellpadding' :  '3'})
    #table_rows = table3.find_all('tr')
    #for tr in table_rows:
        #td = tr.find_all('td')

        #print(td,"\n")
    #print(titles)


    #https://zamunda.net/catalogs/movies?letter=&t=movie&search=gemini+man&field=name&comb=yes


seach_if_those_movies_are_avaible("Gemini man")
#/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[2]
