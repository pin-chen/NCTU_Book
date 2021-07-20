# -*- coding: UTF-8 -*-
import json
import re
data = 'data.json'
new_data = dict()
with open(data, 'r') as fp:
  book = json.load(fp)

for x, y in book.items():
  if type(y) == list:
    new_data[x] = y
  else:
    if y.isdigit() :
      new_data[x] = [y]
'''
for x, y in book.items():
  if type(y) == list:
    continue
  if y.find('ISBN') != -1 or y.find('isbn') != -1:
    pattern = re.findall(r'ISBN: ([0-9]*?)(?:.+)',y)
    new_data[x] = pattern
for x, y in book.items():
  if y == '' or y[0] == '無':
    continue
  else:
    new_data[x] = y
'''
with open("isbn.json", "w", encoding='UTF-8') as f:
  json.dump(new_data, f,  indent = 4, ensure_ascii = False)