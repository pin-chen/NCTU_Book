import telepot
import json
from telepot.loop import MessageLoop
with open('books_data.json', 'r') as fp:
  books = json.load(fp)
API = 'Your telegram API key'
bot = telepot.Bot(API)
def help(ID):
  bot.sendMessage(int(ID), '輸入當期課號以取得參考書資訊\n須輸入四位數字\n部分課號暫無資料')
def infor(ID,TEXT):
  book = books[TEXT]
  for data in book:
    try:
      name = data[1]["items"][0]["volumeInfo"]["title"]
      photo_url = data[1]["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
      link =  data[1]["items"][0]["volumeInfo"]["infoLink"]
    except:
      continue
    letter = '書名'+name+'\n'+'ISBN: '+data[0]+'\n'+photo_url+'\n'+'書籍資料:'+link
    bot.sendMessage(int(ID), letter)
def error(ID):
  bot.sendMessage(int(ID), '無法辨識訊息\n或課程書籍暫無資料\n有任何問題請聯繫 @pinshao\nEmail: hardymike.cs09@nctu.edu.tw')
def handle(msg):
  ID = msg['from']['id']
  TEXT = msg['text']
  if TEXT == '/help':
    help(ID)
  elif TEXT.isdigit() and TEXT in books:
    infor(ID,TEXT)
  else:
    error(ID) 
MessageLoop(bot, handle).run_as_thread()