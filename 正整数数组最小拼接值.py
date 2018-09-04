# -*- coding:utf-8 -*-

'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组[3，32，321]，则打印出这三个数字能排成的最小数字为321323
'''

def PrintMinNumber(numbers):
    if not numbers:
        return 0
    numstr = map(str,numbers) #用str方式将int型数字转换成string
    # 匿名函数，指定比较的方式
    l = lambda n1,n2: int(n1+n2)-int(n2+n1)
    numsort = sorted(numstr,cmp=l) #用特定的比较方式进行比较
    return int("".join(i for i in numsort)) #拍完序之后用join进行连接成结果


if __name__ == '__main__':
    print PrintMinNumber([3, 32, 321])
