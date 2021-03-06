# 模块:在Python里一个py文件，就可以理解为以模块
# 不是所有的py文件都能作为一个模块来导入
# 如果想要让一个py文件能够被导入,模块名字必须要遵守命名规则
# Python为了方便我们开发,提供了很多内置模块

# 5种方式


import time  # 1. 使用import 模块名称 直接导入一个模块
from random import randint  # 2. from模块名import 函数名,导入一个模块里的方法成者变量
from math import *  # 3. from 模块名improt *导入这个模块里的所有方法和变量
import datetime as dt  # 4.导入一个模块并给这个模块起一个别名
from copy import deepcopy as dp  # 5. from 模块名 import 函数名 as 别名

# --1-------------------------
# 导入这个模块以后,就可以使用这个模块里的方法和变量
print(time.time())

# --2-------------------------
x = randint(0, 2)  # 生成[0,2]的随机整数
print(x)

# --3-------------------------
print(pi)

# --4-------------------------
print(dt.time)

# --5-------------------------
dp(['hello', 'good', [1, 2, 3], 'hi'])

# ------------------------------------------------
# 使用from <module_name> import *导入这个模块里"所有"的变量和函数
# 本质是读取模块里的__all__ 属性, 看这个属性里定义了哪些变量和函数
# 如果模块里没用定义__all__ 才会导入所有不以 _ 开头的变量和函数

from module.demo import *

# 使用from demo import * 写法 不需要写模块名
print(m)  # yes
test()
# foo() # name 'foo' is not defined

# 不在__all__中也可以调用
import module.demo as demo

print(demo.n)
