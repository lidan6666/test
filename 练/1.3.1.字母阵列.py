# -*- coding:utf-8 -*-
"""
@author:李丹
@file:1.3.1.字母阵列.py
@time:2023/3/2 17:44
"""   
a = [input() for i in range(100)]
count = 0
for i in range(100):
    for j in range(94):
        if a[i][j:j+7] == 'LANQIAO' and a[i][j:j-7] =='OAIQNAL':
            count += 1
for i in range(94):
     for j in range(100):
         if a[i][j] == "L" and a[i+1][j] == "A" and a[i+2][j] == "N" and a[i + 3][j] == "Q" and a[i + 4][
            j] == "I" and a[i + 5][j] == "A" and a[i + 6][j] == "O":
            count += 1
         elif a[i][j] == "O" and a[i + 1][j] == "A" and a[i + 2][j] == "I" and a[i + 3][j] == "Q" and a[i + 4][j] == "N" and a[i + 5][j] == "A" and a[i + 6][j] == "L":
            count += 1
print(count)