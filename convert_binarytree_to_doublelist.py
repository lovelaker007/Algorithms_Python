# -*- coding: utf-8 -*-

'''
二叉树转换为双向链表，要求链表按从小到大的顺序


'''

from binary_tree import TreeNode, bianli_zhongxu, build_from_list
from double_linked_list import Double_Linked_List

def convert(root):
    if not root:
        return None

    if root.left:
        convert(root.left)
    result_list.add_to_tail(root.value)
    if root.right:
        convert(root.right)



if __name__ == '__main__':
    list_for_tree = [50, 38, 91, 67, 59, 29, 98, 48, 91, 20, 85, 32, 87, 25, 70, 48, 52, 14, 41,\
                     100, 60, 64, 94, 49, 91, 7, 66, 99, 29, 99, 36]
    print list_for_tree
    root = build_from_list(list_for_tree)
    print bianli_zhongxu(root)

    result_list = Double_Linked_List()
    convert(root)
    print result_list.bianli()


