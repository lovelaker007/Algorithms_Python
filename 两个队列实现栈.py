# -*- coding:utf-8 -*-

class Queue(object):
    def __init__(self):
        self.l = []
        self.size = 0

    def enqueue(self, value):
        self.l.insert(0, value)
        self.size += 1

    def dequeue(self):
        try:
            v = self.l.pop()
        except IndexError:
            raise ValueError('can not dequeue from empty queue')
        else:
            self.size -= 1
            return v

class Stack_From_Queue(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.current_queue = self.q1
        self.other_queue = self.q2

    def push(self, value):
        self.current_queue.enqueue(value)

    def pop(self):
        if self.current_queue.size == 0:
            raise ValueError('can not dequeue from empty queue')
        while self.current_queue.size > 1:
            v = self.current_queue.dequeue()
            self.other_queue.enqueue(v)
        value = self.current_queue.dequeue()
        self.current_queue, self.other_queue = self.other_queue, self.current_queue
        return value
        

if __name__ == '__main__':
    # q = Queue()
    # q.enqueue(4)
    # print q.dequeue()
    # print q.dequeue()

    s = Stack_From_Queue()
    for i in range(5):
        s.push(i)
    while 1:
        try:
            print s.pop()
        except:
            print 'all items have been poped from queue'
            break
