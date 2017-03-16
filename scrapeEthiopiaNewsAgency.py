# scrape ethiopia news agency
# march 8, 2017
# archives: 
# need to scrape this website by sections.
# 3 language options: english, arabic, amharic. choosing english.

import urllib, urllib2, re, os, time, codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from numpy import random


writepath = '/Users/erinbaggott/Dropbox/Autocratic Press Paper/Data/NewspapersScraped/EthiopiaNewsAgency/'
writefile = 'ethiopiaRaw.txt'
driver = webdriver.Firefox()
driver.implicitly_wait(30)

f = open(writepath+writefile,'a')

# testing 
url = 'http://www.ena.gov.et/en/index.php/economy'
driver.get(url)
# 0 13 26 39 52 # 13 articles per page. that makes tons of sense. 

# scrape by section

section = 'economy' # 780 page == 60 resultPages
resultPages = 60

section = 'politics' # 780 page == 60 resultPages
resultPages = 60

section = 'social' # 390 page == 30 resultPages
resultPages = 30

section = 'environment' # 91 page == 7 resultPages
resultPages = 7

section = 'technology' # 52 page == 4 resultPages
resultPages = 4

section = 'sport' # 26 page == 2 resultPages
resultPages = 2

page = 0
for page in range(page,(resultPages+1)):  
    print 'On page',str(page),'of',str(resultPages)
    index = int(page*13)
    url = 'http://www.ena.gov.et/en/index.php/'+section+'?start='+str(index)
    driver.get(url)
    time.sleep(random.uniform(1,2))
    div = driver.find_element_by_class_name('itemList')
    links = div.find_elements_by_tag_name('a')
    links = links[0::2]
    links = [l.get_attribute('href') for l in links]
    for link in links:
        driver.get(link)
        time.sleep(random.uniform(1,2))
        title = driver.find_element_by_class_name('itemTitle').text
        date = driver.find_element_by_class_name('itemDateCreated').text
        content = driver.find_element_by_class_name('itemFullText').text
        out = codecs.encode(date,'utf-8')+'\n\n'+codecs.encode(title,'utf-8')+'\n\n'+codecs.encode(content,'utf-8')+'\r\n\r\n____________________________________________________________\r\n\r\n'
        f.write(out)

f.close()
