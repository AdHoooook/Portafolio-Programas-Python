
# Librerias necesarias

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import codecs
import os
import hashlib
import pandas as pd

url = 'http://web.mta.info/developers/turnstile.html'

response = requests.get(url)

print(response)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup)

for i in range(36,len(soup.findAll('a'))+1):


    one_a_tag = soup.findAll('a')[i]

    print(one_a_tag)
    
    link = one_a_tag['href']

    print(link)
    
    download_url = 'http://web.mta.info/developers/'+ link

    print(download_url)

    
    urllib.request.urlretrieve(download_url,'/'+link[link.find('/turnstile_')+1:])



    time.sleep(1) 






