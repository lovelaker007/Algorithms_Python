# -*- coding: utf-8 -*-

class Double_Linked_Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Double_Linked_List(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def build_from_list(self, array):
        v = array[0]
        self.head = Double_Linked_Node(v)
        self.length += 1

        for i in xrange(1, len(array)):
            self.add_to_tail(array[i])

    def add_to_tail(self, value):
        if not self.head:
            self.head = Double_Linked_Node(value)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        new = Double_Linked_Node(value)
        curr.next = new
        new.prev = curr
        self.length += 1

    def bianli(self):
        result = []
        curr = self.head
        if not curr:
            return
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

    # 在位置pos处插入，位置从0开始算起
    def insert(self, pos, value):
        if not self.head:
            self.head = Double_Linked_Node(value)
            self.length += 1
            return

        curr = self.head
        if pos == 0:
            self.head = Double_Linked_Node(value)
            self.head.next = curr
            curr.prev = self.head
        else:
            for i in xrange(pos-1):
                curr = curr.next
            if not curr.next:
                new = Double_Linked_Node(value)
                curr.next = new
                new.prev = curr
            else:
                old_next = curr.next
                new_next = Double_Linked_Node(value)
                curr.next = new_next
                new_next.prev = curr
                new_next.next = old_next
                old_next.prev = new_next
        self.length += 1

    # 删除链表中值为value的节点，如果有多个节点值都为value，都会删除
    def delete(self, value):
        deleted = 0
        if not self.head:
            raise ValueError('delete from empty Double_Linked_List')

        curr = self.head
        while curr:
            if curr.value == value:
                if curr is self.head:
                    self.head = curr.next
                    deleted += 1
                else:
                    prev = curr.prev
                    if not curr.next:
                        prev.next = None
                    else:
                        nnext = curr.next
                        prev.next = nnext
                        nnext.prev = prev
                    deleted += 1
            curr = curr.next

        if not deleted:
            print 'can not find a node by value %d' % (value, )
        else:
            print 'delete %d node' % (deleted, )
            self.length -= deleted


if __name__ == '__main__':
    l = Double_Linked_List()
    import random
    values = []
    for i in xrange(10):
        values.append(random.randint(0, 100))
    print 'values: ', values 

    l.build_from_list(values)
    print 'list: ', l.bianli()

    n = random.randint(0, 100)
    l.insert(0, n)
    l.insert(5, n)
    print 'list: ', l.bianli()   
    print l.length

    l.delete(n)
    print 'list: ', l.bianli()   
    print l.length


