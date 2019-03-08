# coding=utf-8
def rollback(stac):
    if len(stack) == 0:
        return 0, 0
    start, bushu = stac.pop()
    step = start - bushu
    start -= 1
    if start == step:
        return rollback(stac)
    return step, start


A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
L = len(A) + 1
n = len(A)
d = []
D = 0
for i in range(len(A)):
    if A[i] == 1:
        d.append(i + 1)
d.append(L)
A.append(1)
F = [0] * (L + 1)
a = 0
b = 1
while True:
    a, b = b, a + b
    if a > L:
        break
    F[a] = 1
res = L
step = 0
stack = []
num = []
start = L
while True:
    if A[start - 1] == 1 and F[start - step] == 1:
        stack.append((start, start - step))
        step = start
        start = L

    else:
        start -= 1
        if start - step == 0:
            step, start = rollback(stack)
    if step == L:
        num.append(len(stack))
        step, start = rollback(stack)
    if start == 0:
        break


print(min(num))







