# -*- coding:utf-8 -*-

'''
输入一个整数，输出该数二进制表示中1的个数。
python内置的bin函数可以得到整数的二进制表示，bin(1)='0b1', bin(-1)='-0b1'
-1的二进制在python并没有表示为补码的形式，需要计算 -1&0xffffffff 得到-1的补码表示
bin(-1&0xffffffff)='0b11111111111111111111111111111111'

整数n减1时，从二进制表示可总结规律：从左边开始，将遇到的0改变为1，直到遇到1为止，并将1改为0
n&(n-1)一定会将n的二进制的最右边一位1改变为0，那n经过多少次n=n&(n-1)变为0，二进制中就有多少个1

'''

def numberof1(n):
    if n < 0:
        n = n & 0xffffffff
    count = 0
    while n:
        count += 1
        n = n&(n-1)
    return count


if __name__ == '__main__':
    print '%d > %s > %d' % (88, bin(88), numberof1(88))
    print '%d > %s > %d' % (0, bin(0), numberof1(0))
    print '%d > %s > %d' % (-1, bin(-1&0xffffffff), numberof1(-1))
