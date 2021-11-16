# -*- coding: utf-8 -*-
import os
import time
from telethon import TelegramClient, events, sync

api_id = input() # api_id
api_hash = input()	# 输入api_hash
path = r'./telegram.log'
client = TelegramClient('telegram', api_id, api_hash)
client.connect()
#发送消息
def sendMessage(message):
  try:
    client.send_message('@guan_v2p_bot', message)
    time.sleep(10)
    # client.send_message("@guan_v2p_bot", '/farm 1234567890123456')
  except Exception as e:
      print(e)
#获取消息   
def getMessage():
  arr = ['bean', 'farm']
  myArr = ['MyBean', 'MyFruit1']
  for line in open(path, encoding = 'utf-8'):
    for index, item in list(enumerate(arr)):
      newItem = myArr[index]
      if (line.find(newItem) == 0):
        print(item, line.split('\'')[-2])
        message = '/{} {}'.format(item, line.split('\'')[-2])
        sendMessage(message)
  #关闭连接
  client.disconnect()

if __name__ ==  "__main__":
  getMessage()



