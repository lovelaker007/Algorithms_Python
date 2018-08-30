# -*- coding: utf-8 -*-

'''
一种方法是按顺序遍历链表，不过将值放到栈中，栈的输出为后进先出，因此可以实现倒叙遍历
另一种方法是用递归，对每个节点，先完成他下一个节点的遍历，在输出自己的值。如此递归下去，最后一个节点第一个输出
使用递归要注意的是，如果链表过长，会导致递归函数调用栈溢出
'''

# 递归方法实现
def print_from_tail(head):
    if not head:
        return

    print_from_tail(head.next)
    print head.value


if __name__ == '__main__':
    l = [66, 34, 55, 80, 34, 47, 95, 36, 47, 72, 98, 61, 9, 75, 51]
    from linked_list import Linked_List
    ll = Linked_List()
    ll.bulid_from_list(l)
    ll.bianli()

    print_from_tail(ll.head)


