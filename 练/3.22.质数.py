# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.22.质数.py
@time:2023/3/22 11:40
"""   
# count = 0
# for i in range(100000):
#   if i == 2:
#     count += 1
#   if i > 2:
#     for j in range(2, i):
#       if i % j == 0:
#         break
#     if i == j + 1:
#       count += 1
#   if count == 2019:
#     break
# print(i)
count = 0
for i in range(100000):
    if i == 2:
        count += 1
    for j in range(2, i+1):
        if i % j != 0:
            count += 1

    if count == 2019:
        break
print(i)
