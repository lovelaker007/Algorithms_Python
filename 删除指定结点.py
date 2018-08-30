# -*- coding:utf-8 -*-

from linked_list import Node

'''
在链表head中删除指定的节点node，时间复杂度为O(1)

常规的删除单向链表中节点的方法中，需要遍历链表，找到删除节点的前一个节点，这种方法复杂度为O(n)
既然已经指定了要删除的节点node，node的下一个节点为next=node.next，将next.value复制到node.value
再将node.next指向next.next，就实现了将next节点替代node节点，此时删除next节点就相当于删除node节点了
'''

def delete_node(head, node_to_delete):
    if not head or not node_to_delete:
        return

    node_next = node_to_delete.next 
    if node_next:
        node_to_delete.value = node_next.value
        node_to_delete.next = node_next.next
        del node_next
    # 要删除节点没有下一个节点，还是要遍历链表，找到删除节点的前一个节点
    else:
        # 如果待删除节点没有前一个节点，即待删除节点就是头节点
        if head is node_to_delete:
            head = node_to_delete = None
        else:
            prev = head
            while not prev.next is node_to_delete:
                prev = prev.next
            prev.next = node_to_delete.next
    

if __name__ == '__main__':


