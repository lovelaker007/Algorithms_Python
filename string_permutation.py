# -*- coding:utf-8 -*-

    
# 下面的计算不正确
def func1():
    count = 0
    for m in range(-2, -(len(s)+1), -1):
        # print m
        for n in range((m+1), 0, 1):
            # print m, n
            l[m], l[n] = l[n], l[m]
            count += 1
            print ''.join(l)
            l[m], l[n] = l[n], l[m]
    print count

'''
递归求出排列
对于字符串abcde
    将字符串中的字符，依次放到第一个位置(比如将a放到第一个位置)，再对后面的字符(bcde)求排列
    对bcde求排列，也是依次将b c d e放到第一个位置，对剩下的字符求排列，实际上是一个递归的过程
'''
def permutation(s):
    if not s:
        return
    l = []
    for i in s:
        l.append(i)
    permutation_t(l, 0, len(l)-1)

def permutation_t(l, start, end):
    if start == end:
        print ''.join(l)
        global count
        count += 1

    for i in range(start, end+1):
        l[start], l[i] = l[i], l[start]
        permutation_t(l, start+1, end)
        l[start], l[i] = l[i], l[start] 


if __name__ == '__main__':
    s = 'abcde'
    count = 0
    permutation(s)
    print count



