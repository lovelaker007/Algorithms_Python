# -*- coding: utf-8 -*-
'''
链表的倒数第k个节点，最后一个节点从倒数第一个算起
'''

def find_kth_to_end(head, k):
    if not head or k < 1:
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

# 拓展：找到链表中间的节点
# 如果链表总长为奇数，中间节点只有一个；如果为偶数，返回中间两个节点的任意一个
# 定义两个指针，一个每次跳2个节点，一个跳1个。前面的指针跳到链表末尾时，后面的指针指向的就是中间的节点
def can_jump_two(node):
    if not node.next:
        return False
    elif not node.next.next:
        return False
    else:
        return True

def find_middle_node(head):
    if not head:
        return None
    
    jump_one = jump_two = head
    while can_jump_two(jump_two):
        jump_two = jump_two.next.next
        jump_one = jump_one.next
    return jump_one.value
 

if __name__ == '__main__':
    import random
    from linked_list import Node
    l = []
    for i in range(11):
        l.append(random.randint(0, 100))

    head = Node.new(l) 
    head.bianli()

    print 'the %dth to end: %d' % (3, find_kth_to_end(head, 3))
    print 'the %dth to end: %d' % (11, find_kth_to_end(head, 11))
    # print 'the %dth to end: %d' % (15, find_kth_to_end(head, 15))

    print 'the middle of list: %d' % (find_middle_node(head))

