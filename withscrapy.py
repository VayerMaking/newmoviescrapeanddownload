from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
import config

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=r'/usr/bin/chromedriver')
driver.get("https://zamunda.net/catalogs/movies?letter=&t=movie&search=gemini+man&field=name&comb=yes")

username = driver.find_element_by_name("username")
username.clear()
username.send_keys(config.username)

password = driver.find_element_by_name("password")
password.clear()
password.send_keys(config.password)

driver.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/form/table/tbody/tr[3]/td/input").click()

movie_dict = {}
movie_tables = ["2","3","4","5","6"]
i = 2
i = str(i)
for i in movie_tables:
    xpath_size = "/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[" + i + "]/td[2]/table[2]/tbody/tr[2]/td[5]"
    size = driver.find_element_by_xpath(xpath_size)
    #/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td[5]/font
    #/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[2]/td[2]/table[1]/tbody/tr/td[1]/a
    #/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[3]/td[2]/table[2]/tbody/tr[2]/td[5]/font
    #/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[3]/td[2]/table[1]/tbody/tr/td[1]/a
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

#movie_link = index.get_attribute("href")
#print(movie_link)

xpath_title = "/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[" + k + "]/td[2]/table[1]/tbody/tr/td[1]/a"
title = driver.find_element_by_xpath(xpath_title)
title2 = title.text
title2 = str(title2)
print(title2)


driver.quit()
