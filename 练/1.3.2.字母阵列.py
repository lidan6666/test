# -*- coding:utf-8 -*-
"""
@author:李丹
@file:1.3.2.字母阵列.py
@time:2023/3/2 21:22
"""   
N = 100
src = 'LANQIAO'
data = []
ans = 0
# 8个方向横纵坐标的增量
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def check(i, j):
    ans = 0
    # 8个方向
    for d in range(8):
        ok = True
        # 延伸7次
        for k in range(1, 7):
            new_i = i + k * dx[d]
            new_j = j + k * dy[d]
            if (not 0 <= new_i < N) or (not 0 <= new_j < N) or data[new_i][new_j] != src[k]:
                ok = False
                break
        if ok:
            ans += 1
    return ans


if __name__ == '__main__':
    for i in range(N):
        data.append(input())
    for i in range(N):
        for j in range(N):
            if data[i][j] == 'L':
                ans += check(i, j)
    print(ans)
