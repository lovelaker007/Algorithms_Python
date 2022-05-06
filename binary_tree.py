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
            # master注释
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

    def bianli_ceng(self, root=None):
        if not root:
            root = self.root
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

    def bianli_qianxu(self, root=None):
        if not root:
            if not self.root:
                return
            root = self.root

        result = []
        self.bianli_qianxu_t(root, result)
        print result

    def bianli_qianxu_t(self, root, result):
        if not root:
            return
        result.append(root.value)
        if root.left:
            self.bianli_qianxu_t(root.left, result)
        if root.right:
            self.bianli_qianxu_t(root.right, result)

    def bianli_zhongxu(self, root=None):
        if not root:
            if not self.root:
                return
            root = self.root

        result = []
        self.bianli_zhongxu_t(root, result)
        print result

    def bianli_zhongxu_t(self, root, result):
        if not root:
            return
        if root.left:
            self.bianli_zhongxu_t(root.left, result)
        result.append(root.value)
        if root.right:
            self.bianli_zhongxu_t(root.right, result)
   
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

# 重建二叉树
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

# 判断treeb是不是treea的子树
def is_subtree(treea, treeb):
    if not treea or not treeb:
        return False

    result = False
    if treea.value == treeb.value:
        result = is_equal_tree(treea, treeb)
    if not result:
        result = is_subtree(treea.left, treeb)
    if not result:
        result = is_subtree(treea.right, treeb)
    return result

# 判断两个二叉树是否完全相同
def is_equal_tree(treea, treeb):
    if not treeb:
        # treeb为空，无论treea是否为空，都可以表示b是a的子树
        return True
    if not treea:
        # 运行到此处，隐含的条件为treeb不为空
        return False
    if treea.value != treeb.value:
        return False
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

# 是否是平衡树
def is_balanced(tree):
    if not tree:
        return True

    if abs(depth_of_tree(tree.left)-depth_of_tree(tree.right)) > 1:
        return False
    return is_balanced(tree.left) and is_balanced(tree.right)

# 是否是对称二叉树
# 一棵树和其镜像二叉树完全一样就是对称二叉树
class SolutionIsSymmetrical():
    def is_symmetrical(self, tree):
        if not tree:
            return True
        return self.is_symmetrical_t(tree.left, tree.right)

    def is_symmetrical_t(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.value == right.value:
            return self.is_symmetrical_t(left.right, right.left) and \
                    self.is_symmetrical_t(left.left, right.right)
        return False

# 求和为某值的路径，路径是指根节点到某一叶子节点所经过的所有节点
class SolutionFindValuedPath():
    def __init__(self):
        self.value_in_path = []
        self.results = []
    
    def find_valued_path(self, tree, value):
        if tree is None:
            return None

        self.value_in_path.append(tree.value) 
        if tree.left:
            self.find_valued_path(tree.left, value)
        if tree.right:
            self.find_valued_path(tree.right, value)
        if not tree.left and not tree.right:
            if sum(nodes_in_path) == value:
                self.results.append(copy.deepcopy(nodes_in_path))
        self.value_in_path.pop()

# 二叉树的深度
class SolutionDepthOfTree():
    def __init__(self):
        self.depth_dict = {}
        # 下面的属性用于按层遍历求深度
        self.depth = None
        self.nodes_of_level = []
        self.last_of_level = None

    # 递归方法
    def depth_of_tree1(self, tree):
        if not tree:
            return 0
        
        if not tree in self.depth_dict:
            left = self.depth_of_tree1(tree.left)
            right = self.depth_of_tree1(tree.right)
            self.depth_dict[tree] = max(left, right)+1
        return self.depth_dict[tree]
    
    # 非递归方法，按层遍历
    def depth_of_tree2(self, tree):
        if not tree:
            self.depth = 0
        
        self.nodes_of_level.append(tree) 
        self.last_of_level = tree
        while self.nodes_of_level:
            current = self.nodes_of_level.pop(0)
            if current.left:
                self.nodes_of_level.append(current.left)
            if current.right:
                self.nodes_of_level.append(current.right)
            if current is self.last_of_level:
                self.depth += 1
                if self.nodes_of_level:
                    self.last_of_level = self.nodes_of_level[-1]
        return self.depth

# 按层打印二叉树
class SolutionPrintLevel():
    def __init__(self):
        # 用二维数组表示二叉树所有的节点值，数组的元素也是一个数组，表示一层中的节点值
        self.result = []
        # 一层节点的值
        self.tmp = []
        # 按层遍历树，辅助存储节点的队列
        self.nodes_of_level = []
        # 每层最后一个节点
        self.last_of_level = None
    
    def print_level_t(self, tree):
        if not tree:
            return
        
        self.nodes_of_level.append(tree)
        self.last_of_level = tree
        while self.nodes_of_level:
            current = self.nodes_of_level.pop(0)
            self.tmp.append(current.value)
            if current.left:
                self.nodes_of_level.append(current.left)
            if current.right:
                self.nodes_of_level.append(current.right)
            if current is self.last_of_level:
                self.result.append(copy.deepcopy(self.tmp))
                print self.tmp
                self.tmp = []
                if self.nodes_of_level:
                    self.last_of_level = self.nodes_of_level[-1]           

    
    def print_level(self, tree):
        self.print_level_t(tree)
        for i in self.result:
            print i


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
    import copy
    import pdb
    list_for_tree = [50, 38, 91, 67, 59, 29, 98, 48, 91, 20, 85, 32, 87, 25, 70, 48, 52, 14, 41,\
                     100, 60, 64, 94, 49, 91, 7, 66, 99, 29, 99, 36]
    print list_for_tree

    t = Tree()
    t.build_from_list(list_for_tree)
    t.bianli_ceng()
    # [50, 38, 91, 29, 48, 67, 98, 20, 32, 41, 49, 59, 85, 94, 100, 14, 25, 36, 52, 60, 70, 87, 99, 7, 64, 66]
    t.bianli_qianxu()
    # [50, 38, 29, 20, 14, 7, 25, 32, 36, 48, 41, 49, 91, 67, 59, 52, 60, 64, 66, 85, 70, 87, 98, 94, 100, 99]
    t.bianli_zhongxu()
    # [7, 14, 20, 25, 29, 32, 36, 38, 41, 48, 49, 50, 52, 59, 60, 64, 66, 67, 70, 85, 87, 91, 94, 98, 99, 100] 

    s1 = SolutionPrintLevel()
    s2 = SolutionDepthOfTree()
    s3 = SolutionFindValuedPath()

    s1.print_level(t.root)
