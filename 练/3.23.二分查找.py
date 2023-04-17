# -*- coding:utf-8 -*-
"""
@author:李丹
@file:3.23.二分查找.py
@time:2023/3/23 18:03
"""   
array = [1, 3, 4, 4, 4, 6, 10, 20, 21, 22]
# array =set(1, 3, 4, 4, 4, 6, 10, 20, 21, 22)

low = 0
hight = len(array)-1
a = 4
c = []
while True:
    mid = int((low + hight) // 2)
    if array[mid] > a:
        hight = mid - 1
    elif array[mid] < a:
        low = mid + 1
    elif array[mid] == a:
        print(mid+1)
        break

# b = 5
# while True:
#     min = int((low+hight)//2)
#     if mid > b:
#         hight = mid - 1
#     elif mid < b:
#         low = mid + 1
#     elif mid == b:
#         print(array[mid])
#         break
n = list(map(int, input().split()))
b = int(input())
ans = 0
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if abs(int(n[i]-n[j])) == b:
            ans += 1
print(ans)


