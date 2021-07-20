import requests
import json
from bs4 import BeautifulSoup
data = list()
headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
for num in range(0000, 10000):
  cos_num = "\n".join(['{0:04}'.format(num) ])
  url = 'https://timetable.nctu.edu.tw/?r=main/crsoutline&Acy=109&Sem=2&CrsNo='+cos_num+'&lang=zh-tw'
  html = requests.get(url,headers=headers).text
  soup = BeautifulSoup(html, 'html.parser')
  tag1 = soup.find_all('input')
  for x in tag1:
    try:
      if x['name'] == 'cos_id': 
        if x['value'] == '':
          break
        else:
          data.append(cos_num)
    except:
      continue

with open("cos_id.json", "w") as f:
  json.dump(data, f,  indent = 4)
