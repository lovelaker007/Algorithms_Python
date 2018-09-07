# -*- coding:utf-8 -*-

'''
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s，
如果有多对数字的和等于s，输出任意一对即可
'''

class Solution(object):
    def find_numbers(self, llist, s):
        if not llist or (s is None) or len(llist) < 2:
            raise ValueError('invalid input')
        
        former, latter = 0, len(llist)-1
        result = []
        while former < latter:
            if llist[former] + llist[latter] == s:
                result.append((former, latter))
                return result
            elif llist[former] + llist[latter] < s:
                former += 1
            else:
                latter -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    print s.find_numbers([1,2,4,7,11,15], 15)
        


