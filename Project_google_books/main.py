# -*- coding: UTF-8 -*-
import requests
import json
file = 'isbn.json'
new_data = dict()
with open(file, 'r') as fp:
  book = json.load(fp)
APIkey = 'Your Google books API key'
for x, y in book.items():
  new_list = list()
  for isbn in y:
    url = 'https://www.googleapis.com/books/v1/volumes?maxResults=1&q='+isbn+'+isbn&key='+APIkey
    html = json.loads(requests.get(url).text)
    new_list.append([isbn,html])
  new_data[x] = new_list
with open("books_data.json", "w", encoding='UTF-8') as f:
  json.dump(new_data, f,  indent = 4, ensure_ascii = False)
