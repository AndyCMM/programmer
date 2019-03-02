# coding=utf-8
def solution(l):
    l = [1, 3, 2, 1]
    n = len(l)
    k = []
    for i in range(1, n-1):
        if l[i-1] < l[i] and l[i] > l[i+1]:
            k.append(i)
    for i in range(len(k), 1, -1):
        m = len(l)//i
        b = 1
        for j in range(len(k)):
            if k[j] <= b*m - 1:
                b += 1
            if b == i and k[-1] > (b - 1) * m - 1:
                return i
    if len(k) > 0:
        return 1
    return 0


print(solution([]))
