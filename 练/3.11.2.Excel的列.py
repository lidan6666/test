# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.11.2.Excel的列.py
@time:2023/3/11 23:01
"""   
'''
在 Excel 中，列的名称使用英文字母的组合。前 26 列用一个字母，依次为 A 到 Z，接下来 26*26 列使用两个字母的组合，依次为 AA 到 ZZ。

请问第 2022 列的名称是什么？

'''
def to_base_26(num):
    if num==0:
        return 'A'  #如果为0
    letters = []
    while num > 0:
        num, rem = divmod(num, 26)
        letters.append(chr(ord('A')+rem-1))
    return ''.join(reversed(letters))  # 进行翻转
print(to_base_26(2022))
# for i in range(7):
#     a = []
#     a.append(str(i))
#     print(','.join(reversed(a)))


def get(x,y,z):
    return x*26*26+y*26+z # 三字母
def ans(x,y,z):
    s = ''
    s += chr(ord('A')+x-1)
    s += chr(ord('A')+y-1)
    s += chr(ord('A')+z-1)
    return s
n = 2022
for i in range(1, 27):
    for j in range(1, 27):
        for d in range(1, 27):
            if get(i, j, d) == n:
                print(ans(i, j, d))
                exit()
