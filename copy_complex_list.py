# -*- coding: utf-8 -*-

'''
复制复杂链表
复杂链表每个节点有两个指针next和sibling，next指向下一个节点，sibling指向任意的节点(可以为空)

复制出来的链表中，节点的next指针已经解决，难点在于设置节点的sibling指针
方法一
    原链表中，假设节点a的sibling为b，需要从头遍历链表，找到节点b到头节点的距离，
    再根据这个距离在复制链表中找到b'
方法二
    空间换时间
    建立哈希表，存放的是原链表节点a和复制链表节点a'的对应关系，此时b和b'也对应起来
    由a的sibling为b可以找到a'的sibling为b'
方法三
    在原链表上直接复制，节点a的复制节点a'位于a的后面
    原链表上a指向b，由于新链表对应的节点a'，b'就在a，b之后，很容易设置a'到b'
    将新链表从原链表上脱离出来
'''
class Complex_List_Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.sibling = None

def add_to_tail(head, value):
    if not head:
        return

    curr = head
    while curr.next:
        curr = curr.next
    curr.next = Complex_List_Node(value)

# 简单的解析兄弟关系的函数
def analysis_siblings(siblings):
    result = []
    for i in siblings:
        if type(i) != str or len(i) != 2:
            print 'Error siblings %s' % (i, )
            continue
        former = i[0]
        latter = i[1]
        result.append((former, latter))
    return result

def find_valued_node(head, value):
    curr = head
    while curr:
        if curr.value != value:
            curr = curr.next
        else:
            return curr
    return None

def add_sibling_t(head, former, latter):
    if not head:
        return

    m = find_valued_node(head, former)
    n = find_valued_node(head, latter)
    if not m or not n:
        print 'Error sibling %s%s' % (m, n)
    m.sibling = n

def add_sibling(head, siblings):
    analysised_siblings = analysis_siblings(siblings)
    for a in analysised_siblings:
        # 元祖解包
        m, n = a
        add_sibling_t(head, m, n)

def print_list(head):
    result = []
    curr = head
    while curr.next:
        m = '%s -> %s' % (curr.value, curr.next.value)
        result.append(m)
        if curr.sibling:
            m = '%s -> %s' % (curr.value, curr.sibling.value)
            result.append(m)
        curr = curr.next
    for i in result:
        print i

def double_node(head):
    curr = head
    while curr:
        old_next = curr.next
        new_next = Complex_List_Node(curr.value)
        new_next.next = old_next
        curr.next = new_next
        curr = old_next

def add_sibling_for_double(head):
    curr = head
    while curr:
        if curr.sibling:
            sibling = curr.sibling
            former = curr.next
            latter = sibling.next
            former.sibling = latter
        curr = curr.next.next

def separate(head):
    former = head
    latter = head1 = head.next
    while latter.next:
        m = latter.next
        n = m.next
        former.next = m
        latter.next = n

        former = m
        latter = n
    return head1

def copy_list(head):
    if not head:
        return

    double_node(head)
    add_sibling_for_double(head)
    return separate(head)


if __name__ == '__main__':
    head = Complex_List_Node('a')
    for i in 'bcdefghi':
        add_to_tail(head, i)

    add_sibling(head, ['ab', 'bd', 'eh', 'di', 'ie', 'gb'])
    print 'the original list'
    print_list(head)

    print 'the copyed list is'
    head1 = copy_list(head)
    print_list(head1)
