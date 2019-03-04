# coding=utf-8
A = [0] * 11
A[2] = A[3] = A[5] = 1
A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
L = len(A) + 1
n = len(A)
d = []
D = 0
for i in range(len(A)):
    if A[i] == 1:
        d.append(i + 1)
d.append(L)
F = [0] * (L +1)
a = 0
b = 1
while True:
    a , b = b, a + b
    if a > L:
        break
    F[a] = 1
for i in range(len(d)):
    pass
print(d)
d.reverse()
i = 0
res = 12
while True:
    break




print(A)
print(F)


