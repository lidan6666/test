# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.8.最短路径.py
@time:2023/3/8 8:25
"""   
'''
小蓝学习了最短路径之后特别高兴，他定义了一个特别的图，希望找到图
中的最短路径。
小蓝的图由 2021 个结点组成，依次编号 1 至 2021。
对于两个不同的结点 a, b，如果 a 和 b 的差的绝对值大于 21，则两个结点之间没有边相连；如果 a 和 b 的差的绝对值小于等于 21，则两个点之间有一条长度为 a 和 b 的最小公倍数的无向边相连。
例如：结点 1 和结点 23 之间没有边相连；结点 3 和结点 24 之间有一条无向边，长度为 24；结点 15 和结点 25 之间有一条无向边，长度为 75。
请计算，结点 1 和结点 2021 之间的最短路径长度是多少。
提示：建议使用计算机编程解决问题。

'''
'''
INF = 0x3f3f3f3ff3ff  # 定义一个较大的值
N = 2025  # 点的个数，总多取一些
d = [INF for i in range(N)]  # 下标i表示第i个点到第一个点的最小的情况的值
d[1] = 0
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def lcm(a, b):
    return int(a * b / gcd(a, b))  # 经典最小公倍数
for i in range(1, N):  # 从第一个点遍历
    for j in range(i + 1, min(N, i + 22)):  # i每跟新一下 后面21个点就开始跟新保留最小的情况 妙呀绝了
        d[j] = min(d[j], lcm(i, j) + d[i])  
print(d[2021])

'''

import math
dp = [float('inf')] * 2022
dp[1] = 0
def func(x, y):
    return (x * y) // math.gcd(x, y)
for i in range(1, 2022):
    for j in range(i + 1, i + 22):
        if j > 2021:
            break
        dp[j] = min(dp[j], dp[i] + func(i, j))
# 1 到第j个点的距离总是取小的，然后每个
print(dp[2021])

# print(min(dp[35],dp[1]+24))