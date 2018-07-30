# -*- coding: utf-8 -*-

def print_matrix_clockwisely(matrix):
    if not matrix:
        return
    # 获取matrix矩阵中的元素，采取matrix[pos1][pos2]的形式
    # pos1表示在哪一个一维数组，pos2表示在一维数组的哪一个位置
    pos1_limit = len(matrix)
    pos2_limit = len(matrix[0])

    pos1 = 0
    pos2 = -1
    time = 1
    result = []
    m = n = 0
    while True:
        # 顺时针向右遍历
        if time % 4 == 1:
            m = time/4
            n = time/4
            if m == (pos2_limit-n):
                break
            for i in range(m, pos2_limit-n):
                pos2 += 1
                print pos1, pos2
                result.append(matrix[pos1][pos2])  
            time += 1
        # 顺时针向下遍历
        elif time % 4 == 2:
            m = time/4 + 1
            n = time/4
            if m == (pos1_limit-n):
                break
            for i in range(m, pos1_limit-n):
                pos1 += 1
                print pos1, pos2
                result.append(matrix[pos1][pos2])
            time += 1
        # 顺时针向左遍历
        elif time % 4 == 3:
            m = time/4 + 1
            n = time/4
            if m == (pos2_limit-n):
                break
            for i in range(m, pos2_limit-n):
                pos2 -= 1
                print pos1, pos2
                result.append(matrix[pos1][pos2])
            time += 1
        # 顺时针向上遍历
        else: 
            m = time/4
            n = time/4
            if m == (pos1_limit-n):
                break
            for i in range(m, pos1_limit-n):
                pos1 -= 1
                print pos1, pos2
                result.append(matrix[pos1][pos2])
            time += 1

            
if __name__ == '__main__':
    import random 
    import copy
    matrix = []
    l = [None] 
    for i in range(6):
        for j in range(1):
            l[j] = random.randint(0, 100)
        print l
        matrix.append(copy.deepcopy(l))

    print_matrix_clockwisely(matrix)

          


