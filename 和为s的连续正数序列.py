# -*- coding:utf-8 -*-

'''
输入一个正数s,打印出所有和为s的连续正数序列（至少含有两个数）。
例如输入15，由于1+2+3+4+5=4+5+6=7+8=15；所以打印出三个连续序列1~5,4~6,7~8
'''

class Solution(object):
    def find_continuous_sequence(self, s):
        if s < 3:
            return None

        result = []
        small, big = 1, 2
        while small < (s+1)/2:
            sum_llist = sum(list(range(small, big+1)))
            if sum_llist < s:
                big += 1
            elif sum_llist > s:
                small += 1
            else:
                result.append(list(range(small, big+1)))
                big += 1
        print result


if __name__ == '__main__':
    s = Solution()
    s.find_continuous_sequence(9)
    s.find_continuous_sequence(100)
    s.find_continuous_sequence(4)

