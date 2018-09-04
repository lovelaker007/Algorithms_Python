# -*- coding:utf-8 -*-

'''
输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。
例如输入12，从1到12这些整数中包含1的数字有1,10,11和12，1一共出现了5次
'''

'''
一位数：1 0-9
二位数：9*1+10+1 = 20 0-99
三位数：9*20+100+20 = 300 0-999
四位数：9*300+1000+300 = 4000
'''

# 暴力解法
def func1(x):
    num = 0
    for i in range(x+1):
        m = str(i)
        for n in m:
            if n == '1':
                num += 1
    return num

# 打印数字的每一位
def func2(num):
    while num:
        print num % 10
        num /= 10

# 任意两位数
def func3(num):
    shi = num/10
    ge = num%10
    if ge == 0:
        num_ge = shi*1  
    else:
        num_ge = shi*1 + 1
    if shi > 1:
        num_shi = 10
    else:
        num_shi = ge+1
    return num_ge + num_shi

'''
和书中的解法不一样，每次循环统计一位上1出现的次数
对于任意的整数 4427689，假设统计千位上1出现的次数
    整数n从1逐渐增加的过程中，千位上的数值在0-9之间循环变化(n小于1000时，将千位看作0)
    想象一下千位上的数值：1000个0，1000个1，1000个2 ... 1000个9，然后循环
    循环的次数是千位的高位组成的数值，本示例中是442。那么在442次循环中，1出现的次数是1000*442

    千位上的数值完成442次完整的循环后，还会从0变化到7
    如果千位上的数字是0，则还没有出现1
    如果是1，则1出现的次数不足1000，应该为千位的低位组成的数值，本示例中是689
    如果大于1，1出现的次数都是1000次

    整个序列中，千位上出现1的次数是 689+1000*42
'''

def func5(num):
    r = 0
    weishu = 0
    # 当前位之后的数值，用于计算当前位为1时，当前为出现1的次数
    houmian = 0
    while num:
        # 当前位的数值
        m = num%10
        # 当前位前面的数值，表示当前位从0-9循环的次数
        num = num/10
        # 已经处理的位数
        weishu += 1
        # 所有完整的循环中，当前位为1的次数
        r_xunhuan = num*(10**(weishu-1))
        # 计算未完成的循环，当前位为1的次数
        if m == 0:
            r_banxunhuan = 0
        elif m == 1:
            r_banxunhuan = houmian+1
        else:
            r_banxunhuan = 10**(weishu-1)
        # print m, r_xunhuan, r_banxunhuan
        r += (r_xunhuan+r_banxunhuan)
        houmian = 10**(weishu-1)*m + houmian
    return r

            
if __name__ == '__main__':
    l = [1, 50, 667, 1000, 8994, 10000, 999]
    for i in l:
        print '%d\t%d' % (func1(i), func5(i))

