# coding=utf-8
# @Time  :2019-03-06 16:13
# @Author:AndyMing
# @File  :1.py

N = 10
M = 3
M = M % N
D = [M - 1]
res = M - 1
num = 0
while True:
    num += (res + N) // M
    res = (res + N) % M
    if res in D:
        break
print(num)
