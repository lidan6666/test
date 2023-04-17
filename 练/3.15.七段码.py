# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.15.七段码.py
@time:2023/3/15 23:36
"""
'''
小蓝要选择一部分二极管（至少要有一个）发光来表达字符。在设计字符 的表达时，要求所有发光的二极管是连成一片的。
例如：b 发光，其他二极管不发光可以用来表达一种字符。
例如c 发光，其他二极管不发光可以用来表达一种字符。这种方案与上 一行的方案可以用来表示不同的字符，尽管看上去比较相似
例如：a,b,c,d,e 发光，f,g 不发光可以用来表达一种字符。
例如：b,f 发光，其他二极管不发光则不能用来表达一种字符，因为发光 的二极管没有连成一片。
请问，小蓝可以用七段码数码管表达多少种不同的字符？
'''
import os
import sys
import itertools
# 请在此输入您的代码
# 表示相邻元素
dict = {'a': ['f', 'b'], 'b': ['a', 'c', 'g'], 'c': ['b', 'd', 'g'],
        'd': ['e', 'c'], 'e': ['d', 'f', 'g'], 'f': ['a', 'e', 'g'],
        'g': ['b', 'c', 'e', 'f']}
s = 'abcdefg'
ans = []
cnt = 0
# 先找出全排列 在去全排列里筛选
for i in range(1, 8):
    for x in itertools.combinations(s, i):
        ans.append("".join(x))
for str1 in ans:
    if len(str1) == 1:
        cnt += 1
        continue
    for situation in itertools.permutations(str1):
        for c in range(1, len(situation)):
            if situation[c - 1] not in dict[situation[c]]:
                break
        else:
            cnt += 1
            break
print(cnt)