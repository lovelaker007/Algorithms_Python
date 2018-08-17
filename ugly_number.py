# -*- coding:utf-8 -*-

'''
我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到大的顺序的第1500个丑数。
例如6、8都是丑数，但14不是，因为它包含因子7。习惯上我们把1当做第一个丑数。
'''

'''
如果数m是数n的因子，n能被m整除，即n%m==0为真
如果一个数只包含因子2，3，5，可以理解这个数由若干个2，3，5相乘(个数可以为0)
由此可得到判断一个数是否是丑数的方法
    如果数能被2整除，则一直除以2(相当于去掉因子中的2)
    如果数能被3整除，则一直除以3(相当于去掉因子中的3)
    如果数能被5整除，则一直除以5(相当于去掉因子中的5)
    最后该数变成1就是丑数，否则不是
'''
def is_ugly(n):
    while n%2 == 0:
        n /= 2
    while n%3 == 0:
        n /= 3
    while n%5 == 0:
        n /= 5

    if n == 1:
        return True
    return False

# 暴力解法，逐个判断每个整数
r = []
def get_ugly_num(k): # k为要找到的第k个丑数
    i = 1
    r.append(i)
    k -= 1
    while k:
        i += 1
        if is_ugly(i):
            k -= 1
            r.append(i)
    return i

# 错误的解法
def get_ugly_num2(k):
    if k == 1:
        return 1
    ll.add_at_sorted_position(1)
    index = 0
    while True:
        m = ll[index]
        m2 = m*2
        m3 = m*3
        m5 = m*5
        # pdb.set_trace()
        ll.add_at_sorted_position(m2)
        if ll.size == k:
            break
        ll.add_at_sorted_position(m3)
        if ll.size == k:
            break
        ll.add_at_sorted_position(m5)
        if ll.size == k:
            break
        index += 1
    return ll[-1]

'''
书中丑数按顺序生成讲的很好，参考书中的说明
'''
def get_ugly_num3(k):
    if k == 0:
        return None
    if k == 1:
        return 1

    results = [1]
    # 关键数据，存放用来倍乘的数的位置
    poses = [0, 0, 0]
    while len(results) < k:
        next_nums = []
        max_results = max(results)

        # 如果当前位置对应的数倍乘后，没有大于已有丑数的最大值，位置后移一位
        while results[poses[0]]*2 <= max_results:
            poses[0] += 1
        next_nums.append(results[poses[0]]*2)
        while results[poses[1]]*3 <= max_results:
            poses[1] += 1
        next_nums.append(results[poses[1]]*3)
        while results[poses[2]]*5 <= max_results:
            poses[2] += 1          
        next_nums.append(results[poses[2]]*5)
        next_num = min(next_nums)

        if not next_num in results:
            results.append(next_num)
            poses[next_nums.index(next_num)] += 1
        else:
            poses[next_nums.index(next_num)] += 1
    return (results, results[-1])


if __name__ == '__main__':
    print get_ugly_num(30)
    print r

    m, n = get_ugly_num3(30)
    print m
    print n









