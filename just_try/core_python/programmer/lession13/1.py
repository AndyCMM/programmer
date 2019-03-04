# coding=utf-8
A = [0] * 11
A[3] = A[4] = A[6] = 1
L = len(A) + 1
n = len(A)
F = [0, 1]
i = 2
while True:
    F.append(F[i - 1] + F[i - 2])
    i += 1
    if F[-1] >= L:
        break
print(F)


