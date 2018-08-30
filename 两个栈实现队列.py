# -*- coding:utf-8 -*-

class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, value):
        self.s1.append(value)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()


if __name__ == '__main__':
    l = list(range(10))
    print 'the enqueue sort: %s' % (l, )
    q = Queue()
    for i in l:
        q.enqueue(i)
    # print q.s1
    while 1:
        try:
            print q.dequeue()
        except IndexError:
            break


    
