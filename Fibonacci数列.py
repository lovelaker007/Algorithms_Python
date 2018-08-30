# -*- coding:utf-8 -*-

result = {}
def fibo1(n):
    if n < 1:
        raise ValueError('invalid n')
    if not result[n]:
        if n <= 2:
            result[n] = n
        else:
            result[n] = fibo1(n-1) + fibo1(n-2)
    return result[n]


