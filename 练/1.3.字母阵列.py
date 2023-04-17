# -*- coding:utf-8 -*-
"""
@author:李丹
@file:1.3.字母阵列.py
@time:2023/2/28 18:33
"""   
'''
仔细寻找，会发现：在下面的8x8的方阵中，隐藏着字母序列：“LANQIAO”。
SLANQIAO
ZOEXCCGB
MOAYWKHI
BCCIPLJQ
SLANQIAO
RSFWFNYA
XIFZVWAL
COAIQNAL
我们约定: 序列可以水平，垂直，或者是斜向；
并且走向不限（实际上就是有一共8种方向）。
上图中一共有4个满足要求的串。

下面有一个更大的（100x100）的字母方阵。
你能算出其中隐藏了多少个“LANQIAO”吗？
'''
a = [input() for i in range(100)]
count = 0
# 横着找
for i in range(100):
     for j in range(94):
         if a[i][j:j + 7] == "LANQIAO" or a[i][j:j + 7] == "OAIQNAL":
            count += 1
# 竖着找
for i in range(94):
     for j in range(100):
         if a[i][j] == "L" and a[i+1][j] == "A" and a[i+2][j] == "N" and a[i + 3][j] == "Q" and a[i + 4][
            j] == "I" and a[i + 5][j] == "A" and a[i + 6][j] == "O":
            count += 1
         elif a[i][j] == "O" and a[i + 1][j] == "A" and a[i + 2][j] == "I" and a[i + 3][j] == "Q" and a[i + 4][j] == "N" and a[i + 5][j] == "A" and a[i + 6][j] == "L":
            count += 1
# 斜着找(↖ or ↘)
for i in range(94):
     for j in range(94):
         if a[i][j] == "L" and a[i + 1][j + 1] == "A" and a[i + 2][j + 2] == "N" and a[i + 3][j + 3] == "Q" and a[i+4][
            j + 4] == "I" and a[i + 5][j + 5] == "A" and a[i + 6][j + 6] == "O":
            count += 1
         elif a[i][j] == "O" and a[i + 1][j + 1] == "A" and a[i + 2][j + 2] == "I" and a[i + 3][j + 3] == "Q" and a[i + 4][j + 4] == "N" and a[i + 5][j + 5] == "A" and a[i + 6][j + 6] == "L":
            count += 1
# 斜着找(↗ or ↙)
a = [i[::-1] for i in a]  # 将每一行的str逆序
for i in range(94):
     for j in range(94):
         if a[i][j] == "L" and a[i + 1][j + 1] == "A" and a[i + 2][j + 2] == "N" and a[i + 3][j + 3] == "Q" and a[i + 4][j + 4] == "I" and a[i + 5][j + 5] == "A" and a[i + 6][j + 6] == "O":
            count += 1
         elif a[i][j] == "O" and a[i + 1][j + 1] == "A" and a[i + 2][j + 2] == "I" and a[i + 3][j + 3] == "Q" and a[i + 4][j + 4] == "N" and a[i + 5][j + 5] == "A" and a[i + 6][j + 6] == "L":
            count += 1
print(count)