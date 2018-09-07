# -*- coding: utf-8 -*-

'''
把n个骰子仍在地上，所有骰子朝上一面的点数之和为s，输入n，打印出s的所有可能的值出现的概率。
'''

class Solution(object):
    def __init__(self):
        # doc_list 存储n个骰子出现的点数的一种情况
        self.doc_list = []
        # sum_dict 存储每种和出现的次数
        self.sum_dict = {}

    # 递归方法
    def func1(self, n):
        if not type(n) == int or n == 0:
            raise ValueError('invalid input')

        # 对于n个骰子，和的最小值为n，最大值为6n，初始化每个和出现的次数为0
        for i in range(n, 6*n+1):
            self.sum_dict[i] = 0

        self.func1_t(n)
        for key in self.sum_dict:
            times = self.sum_dict[key]
            # p = float(times) / float(6**n) * 100
            print '点数%d：次数%d' % (key, times) 
            # print 'sum %d probility %f' % (key, p)

    def func1_t(self, n):
        if n == 1:
            for i in range(1, 7):
                self.doc_list.append(i)
                key = sum(self.doc_list)
                self.sum_dict[key] += 1
                self.doc_list.pop()
            return
                
        for i in range(1, 7):
            self.doc_list.append(i)
            self.func1_t(n-1)
            self.doc_list.pop()

    # 迭代
    # 假如只有1个骰子，和的情况为1-6，每个和出现1次
    # 假如有2个骰子，和的情况为2-12，2的次数为1，即1+1(第一个、第二个骰子都是1点)
        # 3的次数为2，即(2+1, 1+2)
        # 4的次数为3，即(3+1, 2+2, 1+3)
        # 以此增长，直到和为7的情况，有6种可能出现和为7
        # 当和为8时，第一个骰子的最大值不能再为7(8-1)，只能从6开始往下递减，但当减到为1时，要求第二个骰子点数为7，不可能
        # 总结一下，和为n出现的可能：假设第一个骰子取值可能为n-1递减到1，但是由于骰子点数限制，要掐头去尾，
        # 第一个骰子最小值为n-6，此时第二个骰子为6；最大为6，此时第二个骰子为n-6
    # 假如有3个骰子，和的可能值为3-18
        # 和为3，头两个骰子为2，第三个为1
        # 和为4，头两个为3，2；第三个为1，2
        # 总结规律，和为s的可能出现在，头两个和为s-1, s-2 ... s-6, 对应第三个为1-6 
    def func2(self, n):
        if not type(n) == int or n == 0:
            raise ValueError('invalid input')

        # 建立两个列表，p1为m个骰子各种和出现的次数，p2为m+1个骰子各种和出现的次数
        # p1初始化为1个骰子时，和出现的可能数
        p1 = [0]+[1]*6
        p2 = []
        self.curr = p1
        self.next = p2
        # i表示骰子数
        for i in range(2, n+1):
            self.next.extend([0]*(6*i+1))
            # m表示和的可能值
            for m in range(i, 6*i+1):
                # k表示最后的骰子可能的点数，他只能为1-6
                for k in range(1, 7):
                    # pos表示前面的骰子的点数和
                    pos = m-k
                    if pos < 0 or pos > 6*(i-1):
                        pos = 0
                    self.next[m] += self.curr[pos]
            del self.curr[:]
            self.curr, self.next = self.next, self.curr
         
        for i in range(n, 6*n+1):
            print '点数%d：次数%d' % (n, self.curr[i])

            

if __name__ == '__main__':
    s = Solution()
    for i in range(1, 6):
        print '骰子数：%d' % (i, )
        s.func1(i)
        s.func2(i)



