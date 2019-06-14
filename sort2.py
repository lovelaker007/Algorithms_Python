# coding: utf-8

# import random


'''
random_nums = []
for i in range(30):
    random_nums.append(random.randint(0, 100))
print(random_nums)
'''


class Sort():
    def __init__(self):
        self.random_nums = [28, 20, 75, 78, 70, 56, 46, 92, 72, 96,
                            1, 57, 97, 34, 92, 38, 12, 3, 88, 80, 74,
                            100, 78, 2, 96, 11, 44, 65, 48, 26]
        self.random_nums2 = [
            28, 20, 75, 78, 70, 56, 46, 92, 72, 96, 1, 57, 97,
            34, 92, 38, 12, 3, 88, 80, 74, 100, 78, 2, 96, 11, 44, 65, 48, 26]
        print(self.random_nums)

    def swap(self, m, n):
        self.random_nums[m], self.random_nums[n] = \
            self.random_nums[n], self.random_nums[m]

    def xuanze_paixu(self):
        for pos in range(len(self.random_nums) - 1):
            for m in range(pos+1, len(self.random_nums)):
                if self.random_nums[pos] > self.random_nums[m]:
                    self.random_nums[pos], self.random_nums[m] = \
                        self.random_nums[m], self.random_nums[pos]
        print(self.random_nums)

    def charu_paixu(self):
        for m in range(1, len(self.random_nums)):
            for n in range(m, 0, -1):
                if self.random_nums[n] < self.random_nums[n-1]:
                    self.swap(n, n-1)
                else:
                    break
        print(self.random_nums)

    def maopao_sort(self):
        # 一次大循环，最后一个位置
        last_pos = len(self.random_nums) - 1
        while last_pos >= 1:
            # 一次大循环中发生交换的次数
            swap_times = 0
            for m in range(0, last_pos):
                if self.random_nums[m] > self.random_nums[m+1]:
                    self.swap(m, m+1)
                    swap_times += 1
                    last_pos = m

            if swap_times == 0:
                break
        print(self.random_nums)

    def quick_sort(self):
        if len(self.random_nums) == 1:
            return

        self.quick_sort_t(0, len(self.random_nums)-1)
        print(self.random_nums)

    def quick_sort_t(self, start, end):
        if (end - start) <= 5:
            return self.charu_paixu_t(start, end)

        # 优化二，便于取出中间大小的值，分割数组
        self.middle(start, end)
        pos = self.mm(start, end)
        self.quick_sort_t(0, pos-1)
        self.quick_sort_t(pos+1, end)

    def middle(self, start, end):
        pass

    def mm(self, start, end):
        n = start
        for m in range(start, end):
            if self.random_nums[m] < self.random_nums[end]:
                self.swap(m, n)
                n += 1
        self.swap(n, end)
        return n

    def charu_paixu_t(self, start, end):
        if end <= start:
            return

        for m in range(start+1, end+1):
            for n in range(m, start, -1):
                if self.random_nums[n] < self.random_nums[n-1]:
                    self.swap(n, n-1)
                else:
                    break


class SomeClass():
    pass





if __name__ == '__main__':
    s = Sort()
    s.quick_sort()
