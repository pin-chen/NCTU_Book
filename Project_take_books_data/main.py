# -*- coding: UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
path = 'D:/geckodriver.exe'
driver = webdriver.Firefox(executable_path=path,) 
data = dict()
cos_id = json.loads("".join(x for x in open('D:/cos_id.json') ) )
for cos_num in cos_id:
  url = 'https://timetable.nctu.edu.tw/?r=main/crsoutline&Acy=109&Sem=2&CrsNo='+cos_num+'&lang=zh-tw'
  driver.get(url)
  time.sleep(1)
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(3)
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')
  tag1 = soup.find_all('span')
  for x in tag1:
    try:
      if x['name'] == 'col_textbook': 
        data[cos_num] = x.get_text()
        break
    except:
      continue

driver.close()
with open("D:/data.json", "w", encoding='UTF-8') as f:
  json.dump(data, f,  indent = 4, ensure_ascii = False)