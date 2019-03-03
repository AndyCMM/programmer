# coding=utf-8
def fromStartMax(l):
    l_max = 0
    print(l)
    m = 0
    for i in range(len(l)):
        m += l[i]
        if m > l_max:
            l_max = m
    print(l_max)
    return l_max


A = [6, 1, 5, 6, 4, 2, 9, 4]
A_max = 0
n = len(A)
for i in range(1,2):#(1, n-1):
    temp = fromStartMax(A[(i + 1):(n - 1)]) + fromStartMax(A[i-1:0:-1])
    if A_max < temp:
        A_max = temp

print(A_max)

# l = [-2,-3]
# n = len(l)
# r = []
# candidate = float('-inf')
# suma = float('-inf')
# for i in range(n):
#     if suma > candidate:
#         candidate = suma
#     if suma < 0:
#         suma = l[i]
#     else:
#         suma += l[i]
#
# if suma > candidate:
#     candidate = suma
# print(candidate)
