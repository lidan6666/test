# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.2.3.打印大X.py
@time:2023/3/7 18:49
"""   
x = int(input()) # 高度
y = int(input()) # 宽度

z = x + y - 1  # 遍布图布

for i in range(0, x):
    for j in range(0, z):
        # j < y + i and j >= i(y,x)
        if (j < y + i and j >= i) or (j >= z - y - i and j < z - i): # 左上到右下 右上到左下
            print(end="*")
        else:
            print(end=" ")
    print()