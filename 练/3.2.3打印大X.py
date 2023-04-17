# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.2.3打印大X.py
@time:2023/3/2 18:54
"""   
'''
小明希望用星号拼凑，打印出一个大X，他要求能够控制笔画的宽度和整个字的高度。
为了便于比对空格，所有的空白位置都以句点符来代替。
要求输入两个整数m n，表示笔的宽度，X的高度。用空格分开(0<m<n, 3<n<1000, 保证n是奇数)
要求输出一个大X
'''
'''
使用多个for循环，第一个for循环表示先输出点，将x所在的图布大小先表示出来，第二个for循环表示写的x的第一步（从左上到右下），第三个for循环表示写的x的第二步（从右上到左下），第四个for循环就是输出图像即可。
'''
m, n = map(int,input().split(" "))
li = []
# 将.遍布在X整个图布上
for i in range(n):
    res = []
    for j in range(n+m-1):
        res.append('.')
    li.append(res)
#      左上到右下
for i in range(len(li)):
    for j in range(i, i+m):
        li[i][j] = '*'
#     右上到左下
for i in range(len(li)):
    for j in range(len(li[i])-i-m, len(li[i])-i):
        li[i][j] = '*'
#         整体打印
for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j],end="")
    print()
