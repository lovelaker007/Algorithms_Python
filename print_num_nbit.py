# -*- coding:utf-8 -*-
'''
输入整数n，打印1到最大的n位数
例如输入3时，打印1-999之间的数

要考虑当输入的n很大时，整数溢出的情况
因此不用平常的int类型保存n，而用一个列表保存n的每位上的数值，无论n为多大，保存n个元素的列表都可以保存
'''

def print_to_maxn(n):
    if n == 0:
        print 0
        return

    # 保存n每位上的数值的列表，里面的元素初始化全为'0'
    digital_list = ['0'] * n
    # 在列表表示每位数值的基础上实现加一，并且判断是否出现溢出
    while not add_one(digital_list):
        # 打印列表
        print_digital_list(digital_list)

# 递归方法加1并判断是否溢出
def add_one_at_pos(digital_list, pos):
    if pos >=0:
        # 如果数字小于等于8，可以加1
        if int(digital_list[pos]) <= 8:
            digital_list[pos] = str(int(digital_list[pos])+1)
            # False表示没有溢出
            return False
        else:
            # 该位上的数字为9，需要向左进位了
            digital_list[pos] = '0'
            pos -= 1
            return add_one_at_pos(digital_list, pos)
    # pos < 0说明向左进位到小于0号的位置了，溢出了
    else:
        return True

def add_one(digital_list):
    pos = len(digital_list)-1
    return add_one_at_pos(digital_list, pos)

def print_digital_list(digital_list):
    for i in xrange(len(digital_list)):
        if digital_list[i] != '0':
            break
    print ''.join(digital_list[i:])


if __name__ == '__main__':
    print_to_maxn(2)
