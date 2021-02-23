# Python的的内建模块itertools提供了非常有用的用于操作迭代对象的函数

import itertools

# ------------------------
natuals = itertools.count(1)  # count()会创建一个无限的迭代器，下面代码会打印自然数序列，根本停不下来，只能按Ctrl+c退出
for n in natuals:
    print(n)
    break

# ------------------------
# cycle()会把传入的一个序列无限重复下去
import itertools

cs = itertools.cycle('ABC')
for c in cs:
    print(c)
    break

# ------------------------
# repeat()负责把一个元素无限重复下去，不过入股提供了第二个参数，就可以限定重复次数
ns = itertools.repeat('B', 3)
for c in ns:
    print(c)

# 无限序列只有在for迭代时才会无迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取一个有限的序列
natuals = itertools.count(1)
nn = itertools.takewhile(lambda x: x <= 10, natuals)
# for n in nn:
#     print(n)
print(list(nn))
# ------------------------
# chain() 可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('abc', 'xyz'):
    print(c)

# ------------------------
# groupby() 把迭代器中相邻的重复元素跳出来放在一起
for key, group in itertools.groupby('AAABBBCCCAA'):
    print(key, list(group))
print('-----')
for key, group in itertools.groupby('AAaABbBBbCCCAAaa', lambda c: c.upper()):
    print(key, list(group))

# ------------------------
# 练习
# 计算圆周率可以根据公式
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和
import itertools

# -*- coding: utf-8 -*-
import itertools


def pi(n):
    a = 1  # 这是为了后面符号做准备
    s = 0  # 这是为了返回结果做准备
    for i in itertools.count(1):  # 利用itertools.count生成无限序列，从1开始
        if i > 2 * n:  # 跳出循环
            return s
        if i % 2 == 1:  # 奇数
            s += (4 / i) * a  # 直接求和
            a = -a


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
