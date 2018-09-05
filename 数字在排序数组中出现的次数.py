# -*- coding:utf-8 -*-

class Solution(object):
    def find_times(self, llist, key):
        if not llist or not key:
            return -1
        
        index1 = self.get_first_key(llist, key, 0, len(llist)-1)
        index2 = self.get_last_key(llist, key, 0, len(llist)-1)
        if index1 != -1 and index2 != -1:
            return index2-index1+1
        return -1

    def get_first_key(self, llist, key, begin, end):
        if begin == end:
            if llist[begin] != key:
                return -1
            else:
                return begin
        
        mid = (begin+end)/2
        if key < llist[mid]:
            return self.get_first_key(llist, key, begin, mid-1)
        elif key > llist[mid]:
            return self.get_first_key(llist, key, mid+1, end)
        else:
            # 注意这条语句，当mid位置为第一个key时，有两种情况
            if mid == 0 or (mid > 0 and llist[mid-1]!= key):
                return mid 
            else:
                return self.get_first_key(llist, key, begin, mid-1)

    def get_last_key(self, llist, key, begin, end):
        if begin == end:
            if llist[begin] != key:
                return -1
            else:
                return begin

        mid = (begin+end)/2
        if key < llist[mid]:
            return self.get_first_key(llist, key, begin, mid-1)
        elif key > llist[mid]:
            return self.get_first_key(llist, key, mid+1, end)
        else:
            if mid == end or (mid < end and llist[mid+1]!= key):
                return mid 
            else:
                return self.get_first_key(llist, key, mid+1, end)


if __name__ == '__main__':
    l1 = [1, 3, 5, 5, 5, 8, 9]
    s = Solution()
    print s.find_times(l1, 1)
    print s.find_times(l1, 9)
    print s.find_times(l1, 5)
    print s.find_times(l1, 8)
    print s.find_times(l1, 11)

