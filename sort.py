# -*- coding: utf-8 -*-
import random

random_nums = [35, 34, 82, 59, 74, 13, 14, 40, 14, 84, 54, 21, 7, 75, 39, 62, 23, 87, 66, 12, 66]
# random_nums = [35, 34, 82, 59, 74, 13, 14, 40, 14]
print 'before sort: %s' % (random_nums, )

# 选择排序，稳定的排序算法。第一次循环找到最小的数，第二次循环找到第二小的，以此类推
# 花费的时间和排序数组的输入没有关系，时间复杂度：n的平方
# 每一次大循环，确定剩余数组中的最小值，再将最小值和数组前一个位置交换。一次大循环只发生一次交换
def sort(nums):
    for i in range(len(nums) - 1):
        min = i
        for n in range(i+1, len(nums)):
            if nums[n] < nums[min]:
                min = n
        nums[i], nums[min] = nums[min], nums[i]
    print 'nums after sort: %s' % (random_nums, )

# 最坏情况下，需要 n的平方/2 次比较，n的平方/2 次交换
# 平均情况下，需要 n的平方/4 次比较，n的平方/4 次交换
# 冒泡排序对于部分有序的数组比选择排序高效
def maopao_sort(nums):
    for i in range(1, len(nums)):
        m = i
        while m >= 1:
            n = m - 1
            if nums[m] < nums[n]:
                nums[m], nums[n] = nums[n], nums[m]
            else:
                break
            m -= 1
    print 'nums after sort: %s' % (random_nums, )

def insert_sort(nums):
    if not nums or len(nums) == 1:
        return
    for i in range(1, len(nums)):
        for m in range(i, 0, -1):
            if nums[m] < nums[m-1]:
                nums[m-1], nums[m] = nums[m], nums[m-1]
            else:
                break

# 希尔排序的复杂度很难估计，但是比冒泡排序效率高
def xier_sort(nums):
    step = 0
    while step < len(nums)/3:
        step = 3*step + 1

    while step >= 1:
        for i in range(step, len(nums)):
            m = i
            while m >= step:
                n = m - step
                if nums[m] < nums[n]:
                    nums[m], nums[n] = nums[n], nums[m]
                else:
                    break
                m -= step
        step /= 3
    print 'nums after xiersort: %s' % (nums, )

help_nums = []
for i in range(len(random_nums)):
    help_nums.append(None)

def merge(start, mid, end):
    if start == end:
        return

    for i in range(start, end+1):
        help_nums[i] = random_nums[i]

    m, n = start, mid+1
    pos = start
    while pos <= end:
        if m > mid:
            random_nums[pos] = help_nums[n]
            pos += 1
            n += 1
            continue
        if n > end:
            random_nums[pos] = help_nums[m]
            pos += 1
            m += 1
            continue

        if help_nums[m] < help_nums[n]:
            random_nums[pos] = help_nums[m]
            pos += 1
            m += 1
        else:
            random_nums[pos] = help_nums[n]
            pos += 1
            n += 1

# 需要1/2nlgn到nlgn次数的比较
def guibin_sort():
    step = 1
    while step <= len(random_nums):
        print 'step %d' % (step, )
        for i in list(range(len(random_nums)))[:: step*2]:
            merge(i, i+step-1, min(i+2*step-1, len(random_nums)-1))
        print random_nums
        step = 2*step
    print 'nums after guibin: %s' % (random_nums, )

def guibin_digui_sort(start, end):
    if start == end:
        return
    mid = (start+end)/2
    guibin_digui_sort(start, mid)
    guibin_digui_sort(mid+1, end)
    merge(start, mid, end)

import pdb
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    # pdb.set_trace()
    # 每一次while循环, 从right边开始, 将小于等于key的值放到左边
    # 再从left开始, 寻找大于key的值放到右边
    # left = right时跳出循环, 此时left左边的值小于等于key, 右边的值大于key
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)

# 快速排序的平均时间复杂度为O(N*logN), 最坏的情况复杂度为O(N*N)
# 考虑复杂度时, 影响因素是递归调用的次数和每次递归调用中, 比较的次数.
# 每次调用中, 交换元素的次数不用考虑

# 下面的算法, 选取数组固定位置的元素作为分割数组的key
# 这种选择在遇到数组有序时, 递归调用的次数增加
# 可以随机选取数组中的元素做为key
# 也可以选取数组左中右三个位置的元素的中间值做为key
# 另一个优化是对于小数组，快速排序的效率不如插入排序
def quick_sort2(array, l, r):
    if not array or l >= r:
        return
    elif r-l < 10:
        insert_sort(array)
    else:
        q = partition(array, l, r)
        lq, gq = get_equal_edge(array, l, r, q)
        quick_sort2(array, l, lq-1)
        quick_sort2(array, gq+1, r)

def get_equal_edge(array, l, r, q):
    key = array[q]
    for i in range(q, r+1):
        if array[i] != key:
            break
    if array[i] == key:
        gq = i
    else:
        gq = i-1

    for i in range(q, -1, -1):
        if array[i] != key:
            break
    if array[i] == key:
        lq = i
    else:
        lq = i-1
    return (lq, gq)

def quzhong_youhua(array, left, right):
    mid = (left+right)/2
    if array[left] < array[mid]:
        array[left], array[mid] = array[mid], array[left]
    if array[mid] < array[right]:
        if array[left] < array[right]:
            array[left], array[right] = array[right], array[left]
    else:
        array[mid], array[right] = array[right], array[mid]

def partition(array, l, r):
    quzhong_youhua(array, l, r)
    x = array[r]
    i = l-1
    for j in range(l, r):
        if array[j] <= x:
            i = i+1
            array[i], array[j] = array[j], array[i]
    i = i+1
    array[i], array[r] = array[r], array[i]
    return i

# 下面的算法错误
def partition2(array, l, r):
    x = array[l]
    i = l
    for j in range(l+1, r+1):
        if array[j] <= x:
            i = i+1
            array[i], array[j] = array[j], array[i]
    i = i+1
    array[i], array[l] = array[l], array[i]
    return i

# 快速排序的一种优化, 比较时将和key相等的元素聚集在一起, 分割时不再对其分割
def quick_sort3(array, left, right):
    if left >= right:
        return
    lt, gt = left, right
    i = left+1
    key = array[left]
    while i <= gt:
        if array[i] > key:
            array[i], array[gt] = array[gt], array[i]
            gt -= 1
        elif array[i] < key:
            array[i], array[lt] = array[lt], array[i]
            lt += 1
            i += 1
        else:
            i += 1
    quick_sort3(array, left, lt-1)
    quick_sort3(array, gt+1, right)

# 用栈实现，递归转换为迭代
def quick_sort_stack(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    pdb.set_trace()
    while stack:
        # list.pop(0)方法，弹出第一个元素
        # list.append(x) list.pop() 实现栈
        # list.append(x) list.pop(0) 实现队列
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])

    
if __name__ == "__main__":
    # saort(random_nums)
    # maopao_sort(random_nums)
    # xier_sort(random_nums)

    # random_nums = [12, 49, 88, 156, 177, 23, 25, 27, 60, 100]
    # sorted_nums = random_nums[:]
    # print 'before sort: %s' % (random_nums, )
    # merge(0, len(random_nums)-1)
    # print 'after sort: %s' % (sorted_nums, )

    # guibin_sort()
    # guibin_digui_sort(0, len(random_nums)-1)
    # print 'nums after guibin_digui: %s' % (random_nums, )

    # quick_sort2(random_nums, 0, len(random_nums)-1)
    # print 'after sort2: %s' % (random_nums, )

#   quick_sort_stack(random_nums, 0, len(random_nums)-1)
#   print 'after sort: %s' % (random_nums, )

    l = []
    for i in range(100):
        l.append(random.randint(0, 150))

    print l
    quick_sort2(l, 0, 99)
    print l

