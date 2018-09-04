# -*- coding:utf-8 -*-

'''
输入一个整形数组，数组里有正数也有负数。组中连续的一个或多个整数组成一个子数组，
每个子数组都有一个和。求所有子数组的和的最大值
'''

# 设定该变量的作用是：在输入无效和真的最大子数组和为0的情况下，返回的都是0，该变量辨明这两种情况
invalid_input = True
def find_max_subarray(array):
    global invalid_input
    if not array:
        invalid_input = True
        return 0

    cur_max = 0
    ori_max = -0xffffffff
    for i in range(len(array)):
        if cur_max <= 0:
            cur_max = l[i]
        else:
            cur_max += l[i]

        if cur_max > ori_max:
            ori_max = cur_max
    return ori_max

def find_max_subarray2(l):
    if not l:
        return None
    old_start = start = end = 0
    cur_max = 0
    ori_max = -0xffffffff
    
    for i in range(len(l)):
        if cur_max <= 0:
            cur_max = l[i]
            start = i
        else:
            cur_max += l[i]

        if cur_max > ori_max:
            ori_max = cur_max
            old_start = start
            end = i
        # print old_start, end

    r = []
    for i in range(old_start, end+1):
        r.append(l[i])
    print 'max subarray is: %s\nsum is %d\n' % (r, ori_max) 


if __name__ == '__main__':
    l = [1, -2, 3, 10, -4, 7, 2, -5]
    print find_max_subarray(l)
    find_max_subarray2(l)
    l = [-10, -5, -7, -12, -1, -9, -7]
    print find_max_subarray(l)
    find_max_subarray2(l)
    l = list(range(15))
    print find_max_subarray(l)
    find_max_subarray2(l)


