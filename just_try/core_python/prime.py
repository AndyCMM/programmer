# coding=utf-8
def findprime(m):
    if m == 1:
        return 1
    a = m ** 0.5
    num = 2
    i = 2
    while i * i < m:
        if m % i == 0:
            num += 2
        i += 1
    if i * i == m:
        num += 1
    return num


def solution(N):
    # write your code in Python 3.6
    a = N ** 0.5
    a = int(a)
    while a > 1:
        if N % a == 0:
            return 2 * (a + N / a)
    return 2 * (1 + N)


print(solution(30))
# for i in range(10):
#     print(findprime(i))
