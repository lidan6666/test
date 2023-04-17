# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.22.等差数列.py
@time:2023/3/22 11:15
"""   
n = int(input())
a = list(map(int, input().split()))
a.sort()
d = 999
for i in range(0, len(a)-1):
  d = min(d, a[i+1]-a[i])
if d == 0:
  print(n)
else:
  print(int(a[-1] - a[0]/d+1))