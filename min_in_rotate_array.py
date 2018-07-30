# -*- coding:utf-8 -*-

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转，数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转
123456 456123 
在递增数组生成的旋转数组中
    如果中间点大于首元素，说明最小数字在后面一半，
    如果中间点小于尾元素，说明最小数字在前一半。
    依次循环。同时，当一次循环中首元素小于尾元素，说明最小值就是首元素。
    但是当首元素等于尾元素等于中间值，只能在这个区域顺序查找。

输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

def min_in_rotate_array(rotate_array):
    if len(rotate_array) == 0:
        return 0
    front, rear = 0, len(rotate_array) - 1
    midIndex = 0
    while rotate_array[front] >= rotate_array[rear]:
        if rear - front == 1:
            midIndex = rear
            break
        midIndex = (front + rear) // 2
        if rotate_array[front] == rotate_array[rear] and rotate_array[front] == rotate_array[midIndex]:
            return min_in_order(rotate_array, front, rear)

        if rotate_array[midIndex] >= rotate_array[front]:
            front = midIndex
        elif rotate_array[midIndex] <= rotate_array[rear]:
            rear = midIndex
    return rotate_array[midIndex]

def min_in_order(array, front, end):
    result = array[0]
    for i in array[front:end+1]:
        if i < result:
            result = i
    return result


if __name__ == '__main__':
    print min_in_rotate_array([3, 4, 5, 1, 2])
    print min_in_rotate_array([1, 2, 3, 4, 5])
    print min_in_rotate_array([1, 1, 1, 0, 1])
    print min_in_rotate_array([1, 0, 1, 1, 1])
    print min_in_rotate_array([])
    print min_in_rotate_array([1])
