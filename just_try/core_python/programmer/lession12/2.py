# coding=utf-8
# @Time  :2019-03-06 18:59
# @Author:AndyMing
# @File  :2.py


def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)


def divise(a, c):
    while True:
        if a == 1:
            return True
        res = gcd(a,c)
        if res == 1:
            return False
        a = a / res


A = [15, 10, 25]
B = [75, 30, 5]
n = len(A)
num = 0
for i in range(n):
    a = A[i]
    b = B[i]
    c = gcd(a, b)
    if divise(a / c, c) and divise(b / c, c):
        num += 1

print(num)
