# -*- coding:utf-8 -*-

'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
'''

'''
方法一

'''
def partition(array, begin, end):
    key = array[end]
    m = begin
    for n in range(begin, end):
        if array[n] < key:
            array[m], array[n] = array[n], array[m]
            m += 1
    array[m], array[end] = array[end], array[m]
    return m

def get1(array, k):
    if not array:
        return
    if k<= 0 or k > len(array):
        return

    begin = 0
    end = len(array)-1
    pos = 0
    while pos != k:
        pos = partition(array, begin, end)
        if pos > k:
            end = pos-1
        else:
            begin = pos+1
    
    for i in range(k):
        print array[i]


