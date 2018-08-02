# -*- coding: utf-8 -*-

'''
两个序列，按照前一个序列的顺序入栈，查看后一个序列是否是出栈的某种顺序
'''

from stack_with_min import Stack_With_Min

def is_pop_order(in_order, out_order):
    s = Stack_With_Min()
    while in_order:
        value = in_order.pop(0)
        s.push(value)
        # 如果栈顶元素和出序列的第一个元素相等，则一直出栈，直到和出序列不相等为止
        if value == out_order[0]:
            while s.length>=0 and out_order and s.top() == out_order[0]:
                s.pop() == out_order.pop(0)
        
    if s.length == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    in_order = list(range(10))
    out_order = [5, 4, 3, 2, 7, 6, 1, 8, 9, 0]

    print in_order
    print out_order
    print is_pop_order(in_order, out_order)

