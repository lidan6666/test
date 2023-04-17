# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.2.2.第几个幸运号.py
@time:2023/3/2 18:33
"""   
'''
2004年起，国际ISBN中心出版了《13位国际标准书号指南》。
原有10位书号前加978作为商品分类标识；校验规则也改变。
校验位的加权算法与10位ISBN的算法不同，具体算法是：
用1分别乘ISBN的前12位中的奇数位（从左边开始数起），用3乘以偶数位，
乘积之和以10为模，10与模值的差值再对10取模（即取个位的数字）即可得到校验位的值，
其值范围应该为0~9。
)
'''
def f(x):
    m = []
    h = '123456789'
    res1 = 0
    res2 = 0
    for i in x:
        if i in h:
            m.append(int(i))
    for i in range(0,len(m)-1, 2):
        res1 += m[i]
    for i in range(1, len(m)-1, 2):
        res2 = res2 + 3*m[i]
    res = (10-(res1 + res2) % 10) % 10
    if x[res] in h:
        return 1
    return 0
x = input().strip()
print(f(x))