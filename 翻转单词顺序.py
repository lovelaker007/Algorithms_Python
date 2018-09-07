# -*- coding:utf-8 -*-

'''
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student."，则输出"student. a am I"
'''

class Solution(object):
    # 使用内置函数
    def reverse1(self, s):
        s_sub = s.split(' ')
        return ' '.join(s_sub[::-1])

    def reverse2_t(self, slist, begin, end):
        print len(slist)-1, begin, end
        while begin <= end:
            slist[begin], slist[end] = slist[end], slist[begin]
            begin += 1
            end -= 1
        return slist

    def reverse2(self, s):
        if not s:
            return ''
        
        slist = []
        for i in s:
            slist.append(i)
        slist = self.reverse2_t(slist, 0, len(slist)-1)
        word_begin = word_end = 0
        while True:
            while word_begin <= len(slist)-1 and slist[word_begin] == ' ':
                word_begin += 1
            if word_begin > len(slist)-1:
                break
            word_end = word_begin
            # 注意此处的条件，word_end有可能遇到了字符串的结尾，有可能word_end的下一个字符为空格
            while word_end < len(slist)-1 and slist[word_end+1] != ' ':
                word_end += 1
            self.reverse2_t(slist, word_begin, word_end)
            word_begin = word_end+1
        return ''.join(slist)


if __name__ == '__main__':
    s = ' if you really want it'
    # s.split() = ['if', 'you', 'really', 'want', 'it', '']
    so = Solution()
    print so.reverse1(s)
    print so.reverse2(s)


