# coding=utf-8
from random import randint


def lead(l):
    n = len(l)
    stack = []
    len_stack = 0
    for i in range(n):
        if len_stack == 0:
            len_stack += 1
            stack.append(l[i])
        else:
            if stack[-1] == l[i]:
                len_stack += 1
            else:
                len_stack -= 1


    #print(stack)
    if len_stack > 0:
        count = 0
        count = l.count(stack[-1])
       # print(count)
        if count > n/2:
            return stack[-1]
    return None


def solution(A):
    le = lead(A)

    n = len(A)
    if le is not None:
        return 0
    count = 0
    num = 0
    print('le', le)
    all_num = A.count(le)
    for i in range(n):
        if le == A[i]:
            num += 1
        print('num:', num)
        if (i+1)/2 < num and n - i - 1 < 2*(all_num - num):
            count += 1
            print('i:', i, 'count:', count)
    return count


if __name__ == '__main__':
    # for i in range(10):
    #     a = []
    #     for j in range(10):
    #         a.append(randint(1, 3))
    #     print(a, ':', lead(a))
    # a = [1, 2, 2, 2, 1, 1, 1, 1, 1, 1]
    # lead(a)
    a = [1, 2, 2, 2, 1, 1, 1, 1, 1, 1]
    print(a, ':', lead(a))
