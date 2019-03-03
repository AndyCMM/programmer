# coding=utf-8
A = [3,1,2,3,6]
n = len(A)
l = [n - 1] * n
for i in range(n):
    for j in range(i +1,n):
        if A[i] % A[j] == 0:
            l[i] -= 1
        if A[j] % A[i] == 0:
            l[j] -= 1
print(l)