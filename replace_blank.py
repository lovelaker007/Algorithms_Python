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


if __name__ == '__main__':
    s = 'if you really want it'
    print s
    s = replace(s)
    print s

