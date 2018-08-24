# -*- coding:utf-8 -*-

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add_t(self, root, value):
        if not root:
            return TreeNode(value)

        if value < root.value:
            root.left = self.add_t(root.left, value)
        elif value > root.value:
            root.right = self.add_t(root.right, value)
        else:
            pass
        # 注意下面一条关键语句，在递归的回归过程中，被调用函数向调用函数返回当前的节点
        # 当前的节点作为调用函数中的左子节点或右子节点
        return root

    def add(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        self.root = self.add_t(self.root, value)
        
    def build_from_list(self, array):
        if not array:
            return None

        self.root = TreeNode(array.pop(0))
        while array:
            value = array.pop(0)
            self.add(value)

    def bianli_ceng(self):
        node_list = [self.root]
        result = []
        while node_list:
            node = node_list.pop()
            result.append(node.value)
            if node.left:
                node_list.insert(0, node.left)
            if node.right:
                node_list.insert(0, node.right)
        print result
    
    def delete_min(self, root=None):
        if not root:
            if not self.root:
                return
            self.root = self.delete_min_t(self.root)
        else:
            root = self.delete_min_t(root)
            return root

    def delete_min_t(self, root):
        if not root.left:
            return root.right
        # pdb.set_trace()
        root.left = self.delete_min_t(root.left)
        # 下一行关键代码
        return root

    def delete_max(self, root=None):
        if not root:
            if not self.root:
                return
            self.root = self.delete_max_t(self.root)
        else:
            root = self.delete_max_t(root)
            return root

    def delete_max_t(self, root):
        if not root.right:
            return root.left
        root.right= self.delete_max_t(root.right)
        # 下一行关键代码
        return root

    def min(self, root=None):
        if not root:
            if not self.root:
                return
            root = self.root
        while root.left:
            root = root.left
        return root.value

    def max(self, root=None):
        if not root:
            if not self.root:
                return
            root = self.root
        while root.right:
            root = root.right
        return root.value

    def delete(self, value):
        if not self.root:
            return 
        self.root = self.delete_t(self.root, value)

    def delete_t(self, root, value):
        if not root:
            print 'value %d not in tree' % (value, )
            return
        if value < root.value:
            root.left = self.delete_t(root.left, value)
        elif value > root.value:
            root.right = self.delete_t(root.right, value)
        else:
            if not root.left and root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                right_min = self.min(root.right)
                root.value = right_min
                # self.delete_min(root.right)
                root.right = self.delete_min(root.right)
        return root

def bianli_qianxu(root):
    if not root:
        return None

    node = root
    bianli_result.append(node.value)
    if node.left:
        bianli_qianxu(node.left)
    if node.right:
        bianli_qianxu(node.right)

def bianli_zhongxu_t(node, bianli_result):
    if not node:
        return None

    if node.left:
        bianli_zhongxu_t(node.left, bianli_result)
    bianli_result.append(node.value)
    if node.right:
        bianli_zhongxu_t(node.right, bianli_result)

def bianli_zhongxu(root):
    if not root:
        return None

    node = root
    bianli_result = []
    bianli_zhongxu_t(node, bianli_result)
    return bianli_result

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

def is_balanced(tree):
    if not tree:
        return True

    if abs(depth_of_tree(tree.left)-depth_of_tree(tree.right)) > 1:
        return False
    else:
        return True
    return is_balanced(tree.left) and is_balanced(tree.right)

depth_dict = {}
def depth_of_tree(tree):
    return depth_of_tree_t(tree, depth_dict)

def depth_of_tree_t(tree, d):
    if not tree:
        return 0
    if not tree in d:
        d[tree] = max(depth_of_tree_t(tree.left, d), depth_of_tree_t(tree.right, d))
    return d[tree]
 
# 找中序遍历的顺序中，指定节点的下一个节点
# 如果某个节点有右子树，下一个节点就是右子树的最左节点
# 如果没有右子树，如果该节点是其父节点的左子节点，下一个节点就是父节点
    # 如果是父节点的右子节点，需要在向上找父节点，直到某个节点是父节点的左子节点，或者某个节点没有父节点
def find_next_node(node):
    if not node:
        return None

    if node.right:
        res = node.right
        while res.left:
            res = res.left
            return res
    while node.parent:
        if node is node.parent.left:
            return node.parent
        node = node.parent
    return None


if __name__ == '__main__':
    # list_for_tree = [50, ]
    # import random
    # for i in range(30):
        # list_for_tree.append(random.randint(0, 100))
    # print list_for_tree

    import copy
    import pdb
    list_for_tree = [50, 38, 91, 67, 59, 29, 98, 48, 91, 20, 85, 32, 87, 25, 70, 48, 52, 14, 41,\
                     100, 60, 64, 94, 49, 91, 7, 66, 99, 29, 99, 36]
    print list_for_tree

    t = Tree()
    t.build_from_list(list_for_tree)
    t.bianli_ceng()

    # print t.min()
    # print t.max()
    # t.delete_min()
    # print t.min()

    # t.delete(111)
    # t.bianli_ceng()
    t.delete(59)
    t.bianli_ceng()

    print t.max()
    t.delete_max()
    print t.max()

