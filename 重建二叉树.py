# -*- coding:utf-8 -*-

'''
知道二叉树的前序 中序遍历结果，重建二叉树
前序遍历是；对每个节点，先输出自己的value，再遍历左子树，右子树
中序遍历是；对每个节点，先遍历左子树，再输出自己的value，再遍历右子树
前序遍历的时，根节点在第一位，左子节点在第二位，右子节点的位置根据中序遍历的结果得到
中序遍历时，先遍历完了根节点的左子节点，再输出根节点。那找到根节点，前面的节点数就是左子树的大小
在前序遍历中，根节点之后，移动左子树大小的位置，就可以找到右子树
'''

from binary_tree import Tree, TreeNode

def construct(qianxu, zhongxu):
    if not qianxu or not zhongxu:
        return

    root = TreeNode(qianxu[0])
    pos = zhongxu.index(qianxu[0])
    root.left = construct(qianxu[1:pos+1], zhongxu[0:pos])
    root.right = construct(qianxu[pos+1:], zhongxu[pos+1:])
    return root


if __name__ == '__main__':
    qianxu = [50, 38, 29, 20, 14, 7, 25, 32, 36, 48, 41, 49, 91, 67, 59, 52, 60, 64, 66, 85, 70, 87, 98, 94, 100, 99]
    zhongxu = [7, 14, 20, 25, 29, 32, 36, 38, 41, 48, 49, 50, 52, 59, 60, 64, 66, 67, 70, 85, 87, 91, 94, 98, 99, 100] 
    root = construct(qianxu, zhongxu)
    t = Tree()
    t.bianli_ceng(root)
    # [50, 38, 91, 29, 48, 67, 98, 20, 32, 41, 49, 59, 85, 94, 100, 14, 25, 36, 52, 60, 70, 87, 99, 7, 64, 66]
