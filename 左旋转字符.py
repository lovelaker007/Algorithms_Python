# -*- coding:utf-8 -*-

'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
'''

class Solution(object):
    def reverse_t(self, slist, begin, end):
        while begin <= end:
            slist[begin], slist[end] = slist[end], slist[begin]
            begin += 1
            end -= 1
        return slist

    def reverse(self, s, n):
        if not type(s) == str or not type(n) == int:
            raise ValueError('invalid input')
        if s == '':
            return ''

        # n小于0的话，视为向右移动
        if n < 0:
            n = -n
            n %= len(s)
            n = len(s)-n
        else:
            n %= len(s)

        slist = []
        for i in s:
            slist.append(i)
        self.reverse_t(slist, 0, n-1)
        self.reverse_t(slist, n, len(slist)-1)
        self.reverse_t(slist, 0, len(slist)-1)
        return ''.join(slist)


if __name__ == '__main__':
    s = 'abcdefghijk'
    so = Solution()
    print so.reverse(s, 5)
    print so.reverse(s, -(len(s)-5))



