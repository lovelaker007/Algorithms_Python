

class Node(object):
    def __init__(self, value):
        super(Node, self).__init__()
        self.value = value
        self.next = None

class Linked_List(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def bulid_from_list(self, values):
        if isinstance(values, list):
            self.head = Node(values.pop(0))
            self.size += 1
            for i in values:
                self.add_to_tail(i)
        else:
            self.head = Node(values)
            self.size += 1
        return

    def add_to_tail(self, value):
        if not self.head:
            self.head = Node(value)
            self.size += 1
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value)
        self.size += 1

    def add_at_sorted_position(self, value):
        if not self.head:
            self.head = Node(value)
            self.size += 1
            # print 'add %d' % (value)
            return 
        head = self.head
        self.add_at_sorted_position_t(head, value)

    def add_at_sorted_position_t(self, head, value):
        if value == head.value:
            return
        if not head.next:
            if value < head.value:
                if head is self.head:
                    self.head = Node(value)
                    self.size += 1
                    # print 'add %d' % (value)
                    self.head.next = head
                    return
                else:
                    pass
            else:
                head.next = Node(value)
                self.size += 1
                # print 'add %d' % (value)
                return
        else:
            nnext = head.next
            if nnext.value == value:
                return
            if value < head.value:
                if head is self.head:
                    self.head = Node(value)
                    self.size += 1
                    self.head.next = head
                    # print 'add %d' % (value)
                    return
                else:
                    # 程序逻辑，这种情况不可能发生
                    pass
            elif value > head.value and value < nnext.value:
                head.next = Node(value)
                head.next.next = nnext
                self.size += 1
                # print 'add %d' % (value)
                return
            else:
                self.add_at_sorted_position_t(nnext, value)


    def delete(self, value):
        if value is None or not self.head:
            return
        
        prev, curr = None, self.head
        deleted = 0
        while curr:
            if curr.value == value:
                if curr is self.head:
                    self.head = curr.next
                    curr = curr.next
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
            self.size -= deleted
            print 'delete %d nodes' % (deleted, )

    def bianli(self):
        s = []
        curr = self.head 
        while curr:
            s.append(curr.value)
            curr = curr.next
        print s
    
    # 使对象可以使用[]操作符
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise ValueError('index must be a int')
        size = self.size
        if index >= size or index < -size:
            raise ValueError('index out of range')

        if index < 0:
            index = size+index
        head = self.head
        for _ in range(index):
            head = head.next
        return head.value


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
    pass

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
class SolutioFindEntranceofCycle
    def find_entrance_of_cycle(self, after):
        if not head or not head.next:
            return None

        quick = slow = head
        while quick.next.next:
            quick = quick.next.next
            slow = slow.next
            if quick is slow:
                len_cycle = 0
                # 求环的长度
                while not quick.next is slow:
                    quick = quick.next
                    len_cycle += 1
                # 求起始点
                quick = slow = head
                for _ in range(len_cycle+1):
                    quick = quick.next
                while not quick.next is slow:
                    slow = slow.next
                    quick = quick.next
                return slow
        return None

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

    l = [0, 34, 55, 80, 34, 47, 95, 36, 47, 72, 98, 61, 9, 75, 51]
    print l

    linked_list = Linked_List()
    linked_list.bulid_from_list(l)
    linked_list.bianli()

    linked_list.delete(0)
    linked_list.bianli()
    linked_list.delete(47)
    linked_list.bianli()
    linked_list.delete(666)









        
