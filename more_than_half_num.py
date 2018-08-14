# -*- coding:utf-8 -*-

'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
'''

'''
方法一
    如果数字出现的次数超过数组长度的一半，将数组排序后，位于中间位置的数字就是要找的
    随机选一个数，比他小的放到他左边，不比他小的放到右边，此时如果该数的位置正好位于中间位置查找结束
    否则如果该数位置小于中间值，则在右半部分继续查找
    如果该数位置大于中间值，则在右半部分继续查找
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

def find1(array):
    begin = 0
    end = len(array)-1
    while begin < end:
        pos = partition(array, begin, end)
        if pos < len(array)/2:
            begin = pos+1
        elif pos > len(array)/2:
            end = pos-1
        else:
            return array[pos]
    

'''
方法二
    如果一个数字出现的次数超过数组长度的一半，这个数字出现的次数比其他所有数字出现的次数和还要多
    设置两个变量存放数字和次数，初始化为数组首元素和1，之后遍历数组剩下的元素，
    如果下一个元素和存放的数字相同，次数加一
    如果不同，次数减一。当次数减为0时，另取下一个数字存放，并将次数置为1
    最后一次使次数置为一的数字就是要找的数字
'''
def find2(array):
    num = array[0]
    times = 1
    i = 1
    for i in range(1, len(array)):
        if times == 0:
            num = array[i]
            times = 1
            continue
        if array[i] == num:
            times += 1
        else:
            times -= 1
    return num



if __name__ == '__main__':
#     import random
    # l = []
    # for i in range(15):
        # l.append(random.randint(0, 100))
    # print 'before partition: %s' % (l, )

    # partition(l, 0, len(l)-1)
    # print 'after partition: %s' % (l, )

    l = [1,2,3,2,2,2,5,2,4,2,6,2,2,9]
    print find2(l)
