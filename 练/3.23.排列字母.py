# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.23.排列字母.py
@time:2023/3/23 13:10
"""   
a = "WHERETHEREISAWILLTHEREISAWAY"
b = []
for i in a:
    b.append(i)
    b.sort()
for j in b:
    print(j,end= "")
