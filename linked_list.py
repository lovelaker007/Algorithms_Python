# -*- coding: utf-8 -*-

class Node(object):
    @classmethod
    def new(cls, values):
        if isinstance(values, list):
            head = Node(values[0])
            values.pop(0)
            for i in values:
                head.add_to_tail(i)
        else:
            head = Node(values)
        return head

    def __init__(self, value):
        super(Node, self).__init__()
        self.value = value
        self.next = None

    def bianli(self):
        s = []
        curr = self 
        while curr:
            s.append(curr.value)
            curr = curr.next
        print s

    def size(self):
        size = 0
        curr = self 
        while curr:
            size += 1
            curr = curr.next
        return size

    def add_to_tail(self, value):
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = Node(value)

    def delete(self, value):
        if not value:
            return
        
        prev, curr = None, self
        deleted = 0
        while curr:
            if curr.value == value:
                if curr is self:
                    curr = self.next
                    self = self.next
                    deleted += 1
                else:
                    prev.next = curr.next
                    curr = curr.next
                    deleted += 1
            else:
                prev = curr
                curr = curr.next
            
        if deleted == 0:
            print 'can not find %d in list' % (value, )
        else:
            print 'delete %d nodes' % (deleted, )
        return self

def delete(head, value):
    if not value:
        return
    
    prev, curr = None, head 
    deleted = 0
    while curr:
        if curr.value == value:
            if curr is head:
                curr = head.next
                head = head.next
                deleted += 1
            else:
                prev.next = curr.next
                curr = curr.next
                deleted += 1
        else:
            prev = curr
            curr = curr.next
        
    if deleted == 0:
        print 'can not find %d in list' % (value, )
    else:
        print 'delete %d nodes' % (deleted, )
    return head

def reverse_list(head):
    if not head:
        return None
        
    prev = next_node = None
    curr = head
    while curr.next:
        next_node = curr.next
        head.next = prev
        prev = curr 
        curr = next_node

    curr.bianli()
    return curr

# 倒数第k个, 最后一个为倒数第1个
def find_kth_to_end(head, k):
    if k < 1:
        return None

    prev = after = head
    for _ in range(k-1):
        after = after.next
        # 如果链表的长度小于k
        if after is None:
            return None

    # 移动after到最后一个结点
    while after.next:
        after = after.next
        prev = prev.next
    return prev.value

def delete_duplication(head):
    values = []
    deleted = 0
    prev, curr = None, head 

    while curr:
        if not curr.value in values:
            values.append(curr.value)
            prev = curr
            curr = curr.next
        # 删除重复节点的时候, 不用考虑要删除的节点是链表的第一个节点
        else:
            prev.next = curr.next
            curr = curr.next
            deleted += 1
    print 'delete %d nodes, now the list is:' % (deleted, )
    head.bianli()

def find_first_same_node(heada, headb):
    sizea = heada.size()
    sizeb = headb.size()
    
    if sizea > sizeb:
        diff = sizea - sizeb
        long_list = heada
        short_list = headb
    else:
        diff = sizeb - sizea
        long_list = headb
        short_list = heada

    for _ in range(diff):
        long_list = long_list.next
    while long_list:
        if long_list is short_list:
            print 'find first node, value is %d' % long_list.value
            break;
    print 'two list do not have same node'

def merge_sorted_list(heada, headb):
    ha, hb = heada, headb
    result = []

    while ha and hb:
        if ha.value < hb.value:
            result.append(ha.value)
            ha = ha.next
        else:
            result.append(hb.value)
            hb = hb.next

    while ha:
        result.append(ha.value)
        ha = ha.next
    while hb:
        result.append(hb.value)
        hb = hb.next

    return result

# 找到链表中环的入口
# 遍历链表，如果发现某个node和之前遍历过的node完全一样(python中的is), 就发现了环
def entry_node_of_loop(head):
    if head is None:
        return None

    node_list = []
    curr = head
    while curr:
        if not curr in node_list:
            # 注意是将curr本身放到队列中，不是curr.value
            node_list.append(curr)
            curr = curr.next
        else:
            return curr

# 入栈的序列sin，出栈的序列sout
def is_pop_order(sin, sout):
    s = [] 
    pos = 0

    for v in sin:
        s.append(v)
        while s and s[-1] == sout[pos]:
            s.pop()
            pos += 1
    return len(s) == 0

    
if __name__ == "__main__":
    import random
    def create_list():
        values = []
        for i in range(15):
            value = random.randint(1, 100)
            values.append(value)

        head = Node.new(values)
        return head

    def try_delete(h, values):
        head = values[0]
        values.remove(head)
        tail = values.pop()
        
        print 'try to delete %d' % (head, )
        h.delete(head)
        print 'try to delete %d' % (tail, )
        h.delete(tail)
        for i in range(2):
            random_value = values[random.randint(0, values.__len__())]
            print 'try to delete %d' % (random_value, )
            h.delete(random_value)
            values.remove(random_value)
        print 'try to delete 150'
        h.delete(150)

    head = create_list()
    head.bianli()

    # 删除首节点
    head = head.delete(head.value)
    head.bianli()

    head = delete(head, head.value)
    head.bianli()


        
