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


'''
方法二
建立大小为k的容器存放最小的k个值，遍历数组
当容器未满时，直接将值放入容器即可
如果容器已满，则需比较数组下一个值n和容器中最大值m，如果n不小于m，跳过该值继续遍历
否则用m替代n，继续遍历
需要找到合适的数据结构，快速从容器中找到最大值，删掉最大值，放入一个值
此处使用二叉树
'''
from binary_tree import Tree
t = Tree()

def get2(array, k):
    if not array:
        return
    if k<= 0 or k > len(array):
        return   

    for i in range(k):
        t.add(array[i])
    for i in range(k, len(array)):
        if array[i] >= t.max():
            continue
        else:
            t.delete_max()
            t.add(array[i])
    t.bianli_ceng()


if __name__ == '__main__':
    array = [50, 38, 91, 29, 48, 67, 98, 20, 32, 41, 49, 59, 85, 94, 100, 14, 25, 36, \
            52, 60, 70, 87, 99, 7, 64, 66]
    print array
    get2(array, 6)

    


