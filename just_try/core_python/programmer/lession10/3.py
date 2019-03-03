def solution(A):
    # write your code in Python 3.6
    l = A

    n = len(l)
    k = []
    for i in range(1, n - 1):
        if l[i - 1] < l[i] and l[i] > l[i + 1]:
            k.append(i)
    len_k = len(k)
    for i in Solution(n):
        if i > len_k:
            continue
        m = n / i
        b = 1
        for j in range(len(k)):
            if (b - 1) * m <= k[j] <= b * m - 1:
                b += 1
            if b == i + 1:
                return i

    return 0


def Solution(N):
    # write your code in Python 3.6
    a = N
    l = []
    while a >= 1:
        if N % a == 0:
            l.append(a)
        a -= 1
    return l