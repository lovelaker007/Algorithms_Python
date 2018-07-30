# -*- coding: utf-8 -*-

'''
含有min函数的栈

建立一个辅助栈，初始化时，栈和辅助栈都为空，辅助栈的栈顶就是最小值
当新加入的元素比辅助栈栈顶小时，辅助栈和原来的栈都压入该元素
否则该元素只压入主栈，辅助栈再次压入自身栈顶的元素
'''

class Stack_With_Min():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.length = 0

    def push(self, value):
        old_min = self.min()
        if not old_min or value < old_min:
            self.stack1.append(value)
            self.stack2.append(value)
            self.length += 1
        else:
            self.stack1.append(value)
            self.stack2.append(self.min())
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        value = self.stack1.pop()
        self.stack2.pop()
        self.length -= 1
        return value

    def min(self):
        if not self.stack2:
            return None
        return self.stack2[len(self.stack2)-1]

    def __repr__(self):
        return repr(self.stack1)


if __name__ == '__main__':
    import random
    s = Stack_With_Min()
    for i in range(10):
        s.push(random.randint(0, 100))
        print 'stack: %s' % (s, )
        print 'min of stack: %d' % (s.min(), )

    for i in range(9):
        s.pop()
        print 'stack: %s' % (s, )
        print 'min of stack: %d' % (s.min(), )

        

