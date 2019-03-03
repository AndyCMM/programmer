# coding=utf-8
l = [1,5,3,4,3]
n = len(l)
k = []
for i in range(1, n - 1):
    if l[i - 1] < l[i] and l[i] > l[i + 1]:
        k.append(i)
gap_max = k[-1] - k[0]
m = len(k)
s = []
conS = []
for i in range(m-1):
    s.append(k[i+1]-k[i])
    conS.append(k[-i-1]-k[-i-2])
a = int(gap_max ** 0.5 + 1)
if len(k) < a:
    a = len(k)
#print(a)
for i in range(a, 0, -1):
    num_a = 1
    num_b = 1
    bg = 0
    bg1 = - 1
    for j in range(1, len(k)):
        if k[j]-k[bg] >= i:
            num_a += 1
            bg = j
        if k[bg1]-k[len(k)-j-1] >= i:
            num_b += 1
            bg1 = len(k)-j-1
    if num_a >= i or num_b >= i:
        break
print(i)



