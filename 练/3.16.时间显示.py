# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.16.时间显示.py
@time:2023/3/16 18:00
"""
'''
小蓝要和朋友合作开发一个时间显示的网站。
在服务器上，朋友已经获取了当前的时间，用一个整数表示，值为从 1970 年 1月1日 00:00:00 到当前时刻经过的毫秒数。
现在，小蓝要在客户端显示出这个时间。小蓝不用显示出年月日，只需要显示出时分秒即可，毫秒也不用显示，直接舍去即可。
给定一个用整数表示的时间，请将这个时间对应的时分秒输出。
'''
import os
import sys
import datetime
# 请在此输入您的代码
start = datetime.datetime(1970, 1, 1, 00, 00, 00)
print(start)
a = int(input())
b = int(a//1000)  # 去掉毫秒
start = start+datetime.timedelta(seconds=b)
print(start)
d = str(start).split()
print(d)
print(d[1])