import datetime
import requests
import os

# 20211209
# 元旦
# 春节
# 清明
# 劳动
# 端午
# 中秋
# 国庆

title = '\n\n【摸鱼办】提醒您\n\n'
today = datetime.datetime.now()

if today.hour >= 8 and today.hour <= 10:
    v = '上午'
elif today.hour >= 11 and today.hour <= 12:
    v = '中午'
elif today.hour >= 13 and today.hour <= 18:
    v = '下午'
else:
    v = '你'
sayhello = v + '好，打工人！\n'

weekday = today.weekday() + 1
if weekday == 5:
    isFriday = '是！o(*￣▽￣*)ブ'
elif weekday == 6 or weekday == 7:
    isFriday = '不是，但是今天是周末！！！ヾ(≧▽≦*)o'
else:
    isFriday = '不是/(ㄒoㄒ)/~~'
Friday = '今天是周五吗？' + isFriday + '\n'


str1 = '无论工作再忙，一定不要忘记摸鱼哦！\n'
str2 = '有事没事起身去茶水间，去厕所，去走廊走走！\n'
str3 = '别老在工位上坐着，钱是老板的, 但命是自己的！\n'
str4 = '上班是在帮老板赚钱，摸鱼是在赚老板的钱！\n'
str5 = '祝愿天下所有摸鱼人，都能愉快渡过每一天!'

td = datetime.datetime(today.year, today.month, today.day)
# tm = datetime.datetime(2021, 12, 21)

dongzhi = datetime.datetime(2021, 12, 21) #冬至
shengdan = datetime.datetime(2021, 12, 25) #圣诞
yuandan = datetime.datetime(2022, 1, 1)
chunjie = datetime.datetime(2022, 2, 1)
qingming = datetime.datetime(2022, 4, 5)
laodong = datetime.datetime(2022, 5, 1)
duanwu = datetime.datetime(2022, 6, 3)
zhongqiu = datetime.datetime(2022, 9, 10)
guoqing = datetime.datetime(2022, 10, 1)


Today = "今天是" + str(today.year) + "年" + str(today.month) + \
    "月" + str(today.day) + "日。\n"
Weekday = "距离本周周末还有" + str(6 - today.weekday()-1) + "天！\n"
dongzhi_days = "距离冬至还有" + str(abs((td - dongzhi).days)) + "天！\n"
shengdan_days = "距离圣诞还有" + str(abs((td - shengdan).days)) + "天！\n"
yuandan_days = "距离元旦节还有" + str(abs((td - yuandan).days)) + "天！\n"
chunjie_days = "距离春节还有" + str(abs((td - chunjie).days)) + "天！\n"
qingming_days = "距离清明节还有" + str(abs((td - qingming).days)) + "天！\n"
laodong_days = "距离劳动节还有" + str(abs((td - laodong).days)) + "天！\n"
duanwu_days = "距离端午节还有" + str(abs((td - duanwu).days)) + "天！\n"
zhongqiu_days = "距离中秋节还有" + str(abs((td - zhongqiu).days)) + "天！\n"
guoqing_days = "距离国庆节还有" + str(abs((td - guoqing).days)) + "天！\n"


HappyContent = title + Today + sayhello + Friday + str1 + str2 + str3 + Weekday + \
    dongzhi_days + shengdan_days + \
    yuandan_days + chunjie_days + qingming_days + \
    laodong_days + duanwu_days + zhongqiu_days + guoqing_days + \
    str4 + str5

print(HappyContent)

form = {
    'title': '摸鱼办',
    'desp': HappyContent
}
send_key = os.environ.get('SEND_KEY')
print(send_key)
resp = requests.post('https://sctapi.ftqq.com/{}.send'.format(send_key), form)
print(resp)
if resp.status_code == 200:
    print('发送成功！')
