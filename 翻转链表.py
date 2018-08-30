# -*- coding:utf-8 -*-

def reverse_list(head):
    if not head:
        return None
        
    prev = next_node = None
    curr = head
    while curr.next:
        next_node = curr.next
        curr.next = prev
        prev = curr 
        curr = next_node
# while循环之后，curr位于最后一个元素，但是和倒数第二个元素的连接断开
    curr.next = prev

    curr.bianli()
    return curr

def reverse_list2(head):
    if not head:
        return

    prev, curr = None, head
    while True:
        nnext = curr.next
        curr.next = prev
        if nnext:
            curr = nnext
            prev = curr
        else:
            return curr


if __name__ == '__main__':
    import random
    from linked_list import Node
    l = []
    for i in range(11):
        l.append(random.randint(0, 100))

    head = Node.new(l) 
    head.bianli()

    reverse_list(head)
    reverse_list(Node(23))
