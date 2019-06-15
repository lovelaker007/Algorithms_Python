# coding: utf-8


# 去掉重复元素并保持顺序
class Solution():
    def __init__(self):
        self._list = ['b', 'e', 'f', 'b', 'a', 'a', 'c', 'f']
        print(self._list)

    def f1(self):
        self._list2 = list(set(self._list))
        self._list2.sort(key=self._list.index)
        print(self._list2)

    def f2(self):
        self._l2 = []
        [self._l2.append(i) for i in self._list if i not in self._l2]
        print(self._l2)


if __name__ == '__main__':
    s = Solution()
    s.f1()
    s.f2()
