#! /usr/bin/python
# -*- coding:utf-8 -*-

'''
在二维数组中查找数据
二维数组在每行上从左到右递增，每列上从上到下递增
'''

def find(array, number):
    raw_num = len(array)
    col_num = len(array[0])

    m, n = 0, col_num-1
    result = None
    while m < raw_num and n > 0:
        if number > array[m][n]:
            m += 1
        elif number < array[m][n]:
            n -= 1
        else:
            result = (m, n)
            break

    if result:
        print 'find %d at %s' % (number, (m, n))
    else:
        print 'can not find %d' % (number, )

def find_times(array, number):
    raw_num = len(array)
    col_num = len(array[0])

    m, n = 0, col_num-1
    result = []
    while m < raw_num and n >= 0:
        if number > array[m][n]:
            m += 1
        elif number < array[m][n]:
            n -= 1
        else:
            # 如果找到和目标值相等的元素，可以删除元素所在的行和列
            print m, n
            result.append((m, n))
            m += 1
            n -= 1

    if result:
        print 'find %d %d times at %s' % (number, len(result), ', '.join(map(repr, result)))
    else:
        print 'can not find %d' % (number, )

if __name__ == '__main__':
    matrix = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
    find(matrix, 11)
    find(matrix, 30)
    find_times(matrix, 4)
