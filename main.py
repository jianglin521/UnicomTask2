# -*- coding: utf-8 -*-
import requests
import json
import time
import random
import re
import os
from datetime import datetime

class TiantianSpider():
    def __init__(self):
      self.url = 'https://api.doctorxiong.club/v1/fund?code={}'
      self.headers = {
          'Host': 'api.doctorxiong.club',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
      }

      # self.code = '160222,501057,161005,005827,001938,003096,161725'
      # self.num = [2452.91, 692.48, 1141.89, 789.84, 800.94, 225.91, 0]

      self.code = '160222,501057,161005,005827,001938,003096,161725'
      self.num = [3078.55, 678.93, 1370.06, 959.49, 800.94, 376.78, 0]

    def get_content(self):
        url = self.url.format(self.code)
        response = requests.get(url=url,headers=self.headers)
        data = json.loads(response.text)['data']
        # with open('test.json',"w",encoding='utf-8') as f:
        #     f.write(str(data))
        codeList = self.code.split(',')
        sum = 0
        send_msg = ''
        #  遍历结果
        for index, item in enumerate(data):
            todayEarnings = round((float(item['expectWorth']) - float(item['netWorth'])) * self.num[index], 2)
            print("基金: {},涨幅: {}%, 今日收益: {}, 时间: {}".format(item['name'], item['expectGrowth'], todayEarnings, item['expectWorthDate']))
            send_msg += "基金: {}  \n涨幅: {}%, 收益: {}, {}  \n".format(item['name'], item['expectGrowth'], todayEarnings, item['expectWorthDate'])
            sum += todayEarnings
        print('今日收益：{} 时间：{}'.format(round(sum, 2), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))) 
        send_msg += '今日收益：{} 时间：{}'.format(round(sum, 2), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        form = {
            'title': '基金收益',
            'desp': send_msg
        }
        send_key = os.environ.get('SEND_KEY')
        # print(send_key)
        resp = requests.post('https://sctapi.ftqq.com/{}.send'.format(send_key), form)
        print(resp)
        if resp.status_code == 200:
            print('发送成功！')
    def run(self):
        # while True:
        data = self.get_content()
        # self.save_items(data, url_list.index(url) + 1)
        # time_sleep = random.randint(300, 350)
        # # print('暂停{}秒'.format(time_sleep))
        # time.sleep(time_sleep0)

if __name__ == '__main__':
    spider = TiantianSpider()
    spider.run()
