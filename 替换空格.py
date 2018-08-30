# -*- coding:utf-8 -*-

def replace(string):
    string = list(string)
    stringReplace = []
    for item in string:
        if item == ' ':
                stringReplace.append('%20')
        else:
                stringReplace.append(item)
    return ''.join(stringReplace)

'''
遍历一遍字符串，计算字符串中空格的个数，新字符串的长度是原长度+空格的个数*2(空格变成%20，会增大2个字符)
为字符串扩充容积之后，设置两个指针分别指向原字符串结尾(a)和新字符串结尾(b)。此时两指针的距离就是增加的容积
从后向前遍历a，如果a是非空白字符，则将a的值复制到b处，ab同时向前移动一个位置
如果是空白字符，a向前移动一个位置，b移动三个，且填充%20
如此循环，直到ab相遇为止
'''
def replace2(s):
    l_s = list(s)
    count = 0
    for i in l_s:
        if i == ' ':
            count += 1
    print 'there are %d blanks in "%s"' % (count, s)

    ori = len(l_s)-1
    l_s.extend([None]*(count*2))
    new = len(l_s)-1

    while ori < new:
        if l_s[ori] != ' ':
            l_s[new] = l_s[ori]
            ori -= 1
            new -= 1
        else:
            new -= 2
            l_s[new: new+3] = list('%20')
            ori -= 1
            new -= 1
    print 'after replace: %s' % (''.join(l_s))


if __name__ == '__main__':
    s = ' if you really want  it '
    # print s
    # s = replace(s)
    # print s
    replace2(s)

