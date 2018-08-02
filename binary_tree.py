# -*- coding:utf-8 -*-

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add(root, value):
    if not root:
        return TreeNode(value)

    if value < root.value:
        root.left = add(root.left, value)
    elif value > root.value:
        root.right = add(root.right, value)
    # 注意下面一条关键语句，在递归的回归过程中，被调用函数向调用函数返回当前的节点
    # 当前的节点作为调用函数中的左子节点或右子节点
    return root
        
def build_from_list(array):
    if not array:
        return None
    root = TreeNode(array.pop(0))

    while array:
        value = array.pop(0)
        add(root, value)
    return root

def bianli_ceng(root):
    node_list = [root]
    result = []
    while node_list:
        node = node_list.pop()
        result.append(node.value)
        if node.left:
            node_list.insert(0, node.left)
        if node.right:
            node_list.insert(0, node.right)
    print result

def bianli_qianxu(root):
    if not root:
        return None

    node = root
    bianli_result.append(node.value)
    if node.left:
        bianli_qianxu(node.left)
    if node.right:
        bianli_qianxu(node.right)

def bianli_zhongxu(root):
    if not root:
        return None

    node = root
    if node.left:
        bianli_zhongxu(node.left)
    bianli_result.append(node.value)
    if node.right:
        bianli_zhongxu(node.right)

def bianli_houxu(root):
    if not root:
        return None

    node = root
    if node.left:
        bianli_houxu(node.left)
    if node.right:
        bianli_houxu(node.right)
    bianli_result.append(node.value)

def chongjian(qianxu_list, zhongxu_list):
    if (not qianxu_list) or (not zhongxu_list):
        return None
    root = TreeNode(qianxu_list[0])
    pos = zhongxu_list.index(root.value)
    # print qianxu_list[1: pos+1]
    # print zhongxu_list[0: pos]
    root.left = chongjian(qianxu_list[1: pos+1], zhongxu_list[0: pos])
    root.right = chongjian(qianxu_list[pos+1: ], zhongxu_list[pos+1: ])
    return root

def min_tree(root):
    node = root
    while node.left:
        node = node.left
    return node.value

# 判断treeb是不是treea的子树
def is_subtree(treea, treeb):
    result = False
    if treea and treeb:
        if treea.value == treeb.value:
            result = is_equal_tree(treea, treeb)
        if not result:
            result = is_subtree(treea.left, treeb)
        if not result:
            result = is_subtree(treea.right, treeb)
    return result

# 递归判断两个二叉树是否完全相同
def is_equal_tree(treea, treeb):
    if (not treea) and (not treeb):
        return True
    if (treea is None and treeb is not None) or (treea is not None and treeb is None) or \
        (treea.value != treeb.value):
        return False
    # 上面的条件能否改写成如下
    # if not treea or not treeb or treea.value != treeb.value:
        # return False
    return is_equal_tree(treea.left, treeb.left) and \
        is_equal_tree(treea.right, treeb.right) 

# 求treea的镜像
def mirror_of_tree(treea):
    if not treea:
        return None
    treeb = TreeNode(treea.value)
    if treea.left:
        treeb.right = mirror_of_tree(treea.left)
    if treea.right:
        treeb.left = mirror_of_tree(treea.right)
    return treeb

# 求和为某值的路径，路径是指根节点到某一叶子节点所经过的所有节点
def find_valued_path(tree, value):
    if tree is None:
        return None

    nodes_in_path.append(tree.value) 
    if tree.left:
        find_valued_path(tree.left, value)
    if tree.right:
        find_valued_path(tree.right, value)
    if not tree.left and not tree.right:
        if sum(nodes_in_path) == value:
            result_of_find_valued_path.append(copy.deepcopy(nodes_in_path))
        return nodes_in_path.pop()
    nodes_in_path.pop()


if __name__ == '__main__':
    # list_for_tree = [50, ]
    # import random
    # for i in range(30):
        # list_for_tree.append(random.randint(0, 100))
    # print list_for_tree

    import copy
    list_for_tree = [50, 38, 91, 67, 59, 29, 98, 48, 91, 20, 85, 32, 87, 25, 70, 48, 52, 14, 41,\
                     100, 60, 64, 94, 49, 91, 7, 66, 99, 29, 99, 36]
    print list_for_tree

    root = build_from_list(list_for_tree)

    # bianli_ceng(root)
    # print min_tree(root)

    # bianli_result = []
    # bianli_qianxu(root)
    # qianxu_list = copy.deepcopy(bianli_result)
    # bianli_result = []
    # bianli_zhongxu(root)
    # zhongxu_list = copy.deepcopy(bianli_result)
    # print qianxu_list
    # print zhongxu_list

    # root1 = chongjian(qianxu_list, zhongxu_list)
    # bianli_ceng(root1)

    result_of_find_valued_path = []
    nodes_in_path = []
    find_valued_path(root, 319)
    if result_of_find_valued_path:
        print result_of_find_valued_path
    else:
        print None


