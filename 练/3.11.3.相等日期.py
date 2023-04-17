# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.11.3.相等日期.py
@time:2023/3/11 23:24
"""   
'''
对于一个日期，我们可以计算出年份的各个数位上的数字之和，也可以分别计算月和日的各位数字之和。请问从 1900 年 1 月 1 日至 9999 年 12 月 31 日，总共有多少天，年份的数位数字之和等于月的数位数字之和加日的数位数字之和。

例如，2022年11月13日满足要求，因为 2+0+2+2=(1+1)+(1+3) 。
请提交满足条件的日期的总数量。
'''
import datetime
start = datetime.date(1900, 1, 1)
end = datetime.date(9999, 12, 31)
# 把字符串转换为数字,
def get_num(n):
    return sum([int(i) for i in str(n)])
count = 0
while start < end:
    y, m, d = start.year, start.month, start.day
    if get_num(y) == get_num(m)+get_num(d):
        count += 1
    start +=datetime.timedelta(days=1)
print(count)