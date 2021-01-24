# os全称OperationSystem操作系统
# os 模块里提供的方法就是用来调用操作系统里的方法
import os

# os.name ==> 获取操作系统的名字windows系列==>nt /非windows ==>posix
print(os.name)
print(os.sep)  # 路径的分隔符 windows \ 非windows /

print(os.path.abspath('LICENSE'))  # E:\dev\python\QFPython\LICENSE 文件不存在也可以

# isdir判断是否是文件夹
print(os.path.isdir('xxx'))  # False
print(os.path.isdir('rpa'))  # True

# isfile 判断是否是文件
print(os.path.isfile('LICENSE'))  # True
print(os.path.isfile('xxx'))  # False

# exists 判断是否存在
print(os.path.exists('rpa'))  # True
print(os.path.exists('xxx'))  # False

file_name = '2020.2.21.demo.py'
print(file_name.rpartition('.'))  # E:\dev\python\QFPython\LICENSE
print(os.path.splitext(file_name))  # ('2020.2.21.demo', '.py')

# ---------------------------------------------------------------------------------

# sys 系统相关的功能
import sys

print('hello')

print(sys.path)  # 模块所在路径
# 1) 可以在程序运行时临时添加 2)也可以配置 PYTHONPATH 持久化


# sys.exit(100) # 和内置函数exit()功能一样
print('jjjj')

# ---------------------------------------------------------------------------------
import math

print(math.pow(2, 10))  # 1024.0
print(math.factorial(6))  # 720
print(math.floor(12.98))  # 12
print(math.ceil(12.98))  # 13
print(round(12.98))  # 13
print(math.sin(math.pi / 6))  # 0.49999999999999994

# ---------------------------------------------------------------------------------
import random

print(random.randint(1, 5))  # 用来生成[a, b]的随机整数
print(random.random())  # 用来生成[0, 1)的随机整数
print(random.randrange(1, 8))  # 用来生成[a, b)的随机整数
print(random.choice(['zhangsan', 'lisi', 'wangwu', 'zhaoliu']))  # choice用来在可迭代对象里随机抽取一个数据
print(random.sample(['zhangsan', 'lisi', 'wangwu', 'zhaoliu'], 2))  # choice用来在可迭代对象里随机抽取n个数据

# ---------------------------------------------------------------------------------
import datetime as dt

# 涉及到四个类datetime/date/time/timedelta
print(dt.datetime.now())  # 2021-01-24 14:06:09.141065 获取当前的日期时间
print(dt.date(2020, 1, 24))  # 创建一个日期
print(dt.time(14, 7, 22))  # 创建一个时间
print(dt.datetime.now() + dt.timedelta(3))  # 计算三天以后的时间日期

print()
# ---------------------------------------------------------------------------------
import time

print(time.time())  # 获取时间秒数 1611468916.2981489 1970-01-01 00:00:00 至今
print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 按指定格式输出日期
print(time.asctime())  # Sun Jan 24 14:15:16 2021
print(time.ctime())  # Sun Jan 24 14:15:16 2021
print()

# ---------------------------------------------------------------------------------
import calendar  # 日历模块

calendar.setfirstweekday(calendar.SUNDAY)  # 设置每周起始日期码。周- -到周日分别对应日~ 6
print(calendar.firstweekday())  # 返回当前每周起始日期的设置。默认情况下，首次载入calendar模块时返回0 ,即星期一。

c = calendar.calendar(2021)
print(c)  # 打印2021年日历

print(calendar.isleap(2000))  # 判断是否是闰年 true
print(calendar.leapdays(1996, 2010))  # 获取1996年到2010年一共有多少个闰年 4

print(calendar.month(2021, 3))  # 打印2021年3月份日历

# ---------------------------------------------------------------------------------
import uuid  # 全局唯一的标识符

print(uuid.uuid1())  # 32个长度 全球唯一  mac地址 比较慢  用户量超级大的时候才会使用
# print(uuid.uuid2())# 不让用

# uuid3私uid5是使用传入的字符串根据指定的算法算出来的,是固定的
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'zhangsan'))  # md5
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'zhangsan'))  # sha1

print(uuid.uuid4())  # 使用的最多

# 应用场景 我给注册用户发一个激活链接 ， 怎样标识这个链接就是这个用户的 用uuid
