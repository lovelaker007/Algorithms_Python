# -*- coding:utf-8 -*-

'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数：
如数组{7,5,6,4}，逆序对总共有5对，{7,5}，{7,6}，{7,4}，{5,4}，{6,4}；
'''

class Solution(object):
    # 暴力解法
    def inverse_pairs1(self, llist):
        if not llist:
            return None

        count = 0
        for i in range(len(llist)):
            curr = llist[i]
            for m in range(i+1, len(llist)):
                if curr > llist[m]:
                    count += 1
        return count

    def inverse_pairs2(self, llist):
        if not llist:
            return None
        self.copy = [None]*len(llist)
        return self.inverse_pairs2_t(llist, 0, len(llist)-1)

    def inverse_pairs2_t(self, llist, start, end):
        if start == end:
            return 0

        mid = (start+end)/2
        left = self.inverse_pairs2_t(llist, start, mid)
        right = self.inverse_pairs2_t(llist, mid+1, end)

        for i in range(start, end+1):
            self.copy[i] = llist[i]
        m, n = mid, end
        count = 0
        for i in range(start, end+1):
            if m < start:
                llist[i] = self.copy[n]
                n -= 1
            elif n < mid+1:
                llist[i] = self.copy[m]
                m -= 1
            elif self.copy[m] <= self.copy[n]:
                llist[i] = self.copy[m]
                m -= 1
            else:
                llist[i] = self.copy[n]
                count += (n-mid)
                n -= 1
        return left+right+count


if __name__ == '__main__':
    l = [7, 5, 6, 4]
    s = Solution()
    print s.inverse_pairs1(l)
    print s.inverse_pairs2(l)
