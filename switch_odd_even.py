# -*- coding: utf-8 -*-

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分
'''

def switch(array):
    if not array or len(array) <= 1:
        return

    begin, end = 0, len(array)-1
    while True:
        while array[begin] & 0x1:
            begin += 1
        while not array[end] & 0x1:
            end -= 1

        if begin < end:
            array[begin], array[end] = array[end], array[begin]
        else:
            break

if __name__ == '__main__':
    import random
    l = []
    for i in range(20):
        l.append(random.randint(1, 100))
    print l

    switch(l)
    print l



