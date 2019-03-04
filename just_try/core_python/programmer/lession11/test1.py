# coding=utf-8
def foo():
    print('Im test1')
N = 26
P = [1,4,16]
Q = [26,10,20]
l = [1] * (N + 1)
for i in range(2, N + 1):
    if l[i] > 3:
        continue
    temp = i + i
    while temp <= N:

        l[temp] += l[i]
        temp += i
a = 0
print(l)
for i in range(N + 1):
    if l[i] == 2 or l[i] == 3:
        a += 1
    l[i] = a

for i in range(3):
    print(l[Q[i]] - l[P[i]-1])
#print(l)
#print([i for i in range(N + 1) if l[i] == 2 or l[i] == 3])


