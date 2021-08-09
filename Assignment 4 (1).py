#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1


# In[2]:


# Importing Libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

#send get request to the webpage server to get the source code of the page
page = requests.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")

# page content
soup=BeautifulSoup(page.content)

# page content
soup=BeautifulSoup(page.content)

header_tags = [] # empty list
for header in soup.find_all(["td","td","td","td","td","td"]):
    header_tags.append(header.name+" "+header.text.strip())
    
# print all header_tags
header_tags


# In[ ]:


2


# In[3]:


# lets now import all the required libraries
from bs4 import BeautifulSoup
import selenium
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from PIL import Image
from math import ceil
import io
import hashlib
import pandas as pd
import numpy as np
import json
from selenium.common.exceptions import NoSuchElementException           # Importing Exceptions
#Importing requests
import requests
# importing regex
import re


# In[4]:


# Lets first connect to the web driver
driver = webdriver.Chrome("chromedriver.exe") 


# In[5]:


url = 'https://www.bcci.tv/'
driver.get(url)


# In[7]:


international = driver.find_element_by_xpath("//div[@class='navigation__drop-down drop-down drop-down--reveal-on-hover']")
international.click()
time.sleep(1)

titles_tags=driver.find_elements_by_xpath("//div[@class='event-list__list']")
titles_tags


# In[8]:


# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
fixturemonth_titles=[]
for i in titles_tags:
    fixturemonth_titles.append(i.text)
fixturemonth_titles 


# In[ ]:


4


# In[9]:


# Activating the chrome browser
driver=webdriver.Chrome("chromedriver.exe") 
time.sleep(3)

# Opening the homepage of statisticstimes.com
url = "http://statisticstimes.com/"
driver.get(url)


# In[11]:


search_button = driver.find_element_by_xpath('//div[@class="cc-window cc-banner cc-type-info cc-theme-block cc-bottom cc-color-override-688238583 "]')     
search_button.click()  

titles_tags=driver.find_elements_by_xpath("//a[@class='ec']")
titles_tags


# In[12]:


# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
gdp_titles=[]
for i in titles_tags:

    gdp_titles.append(i.text)
gdp_titles 


# In[ ]:


9


# In[1]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'https://www.imdb.com/list/ls095964455/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

tv_series = soup.select('td.titleColumn')
names = [a.attrs.get('href') for a in soup.select('lister-item-header h3')]
year_span = [a.attrs.get('title') for a in soup.select('lister-item-header span')]
genre = [a.attrs.get('genre') for a in soup.select('text-muted text-small span')]
runtime = [b.atters.get('runtime') for b in soup.select('text-muted text-small span')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]


list = []

for index in range(0, len(tv_series)):
    tv_series_string = tv_series[index].get_text()
    tv_series = (' '.join(tv_series_string.split()).replace('.', ''))
    tv_series_title = movie[len(str(index))+1:-7]
    year_span = re.search('\((.*?)\)', tv_series_string).group(1)
    genre = tv_series[:len(str(index))-(len(tv_series))]
    
    data = pd.DataFrame({"tv_series_title": tv_series_title,
            "year_span": year_span,
            "genre": genre,
            "runtime": runtime[index],
            "ratings": ratings[index],
            "votes": votes[index],})
    list.append(data)
    
    for tv_series in list:
        print(tv_series['place'], '-', tv_series['tv_series_title'], '('+tv_series['year_span'] +
          ') -', 'genre:', tv_series['runtime'], tv_series['rating'])
    


# In[ ]:





# In[ ]:




