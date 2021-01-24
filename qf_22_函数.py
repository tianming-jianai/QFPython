# 1. 函数的文档说明
def add(a: int, b: int):  # 这个地方的类型是建议的类型
    """
    两个数字相加
    :param a: 第一个数字
    :param b: 第二个数字
    :return: 两个数字相加的结果
    """
    return a + b


help(add)

x = add(1, 2)
print(x)

y = add('hello', 'world')  # 非指定类型 idea 显示黄色
print(y)


# 2. 函数调用函数
def test1():
    print('test1开始')
    print('test1结束')
    pass


def test2():
    print('test2开始')
    test1()
    print('test2结束')
    pass


test2()


# 定义函数求[n,m)之间所有的整数之和
def add_num(n, m):
    all = 0
    for i in range(n, m):
        all += i
    return all


all = add_num(1, 11)
print(all)


# 求一个整数n的阶乘
def factorial(x):
    res = 1
    for i in range(1, x + 1):
        res *= i;
    return res


res = factorial(3)
print(res)

# 3. 全局变量和局部变量
# 如果局部变量和全局变量同名，会在函数内部定义一个新的局部变量
# 而不是修改全局变量
# 函数内部修改全局变量 使用 global 对变量进行声明

# 内置函数globals() locals()可以查看全局变量和局部变量
print('locals() -> {} \nglobals() -> {}'.format(locals(), globals()))


# 在Python中，只有函数才能分割作用域


# 4. 函数多个返回值
# 元组，字典，列表
# return {'x': x, 'y': y}
# return [x, y]
# return (x, y)
# return x, y # 返回的本质是一个元组

# 总结：
# 1. 函数的声明：使用关键字 def 来声明一个函数
# 2. 函数的格式：def 函数名(形参1,形参2...):
# 3. 函数的调用： 函数名(形参1,形参2...)
# 4. 函数返回值：使用 return 语句返回函数的执行结果
# 5. 函数返回多个结果：就是将多个结果打包成一个整体返回
#     可以使用列表和字典，通常情况下选择使用元组

# 函数名元素一个标识符 字母/数字/下划线 严格区分大小写 不能使用关键字
# 遵守命名规范，使用下划线连接 顾名思义

# --------------------------------------------------------------------------


# 1. 默认参数
# 缺省参数
# 有些函数的参数是，如果你传了参数，就使用传递的参数
# 如果没有传递参数，就使用默认值
# 关键字参数 不要求顺序

# 2. 可变参数
def add_many(iter):
    x = 0
    for i in iter:
        x += i
    return x


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = add_many(nums)
print(res)


def add_many2(a, b, *args, c=1, **keywords):  # *args 表示可变参数 tuple  c=1缺省参数放在可变参数后面 多出来的关键字参数会以字典的形式保存
    d = a + b
    for i in args:
        d += i
    print(keywords)
    return c + d


res = add_many2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, c=2, e=3, f=4)
print(res)


# 3. 可变类型和不可变类型传参

# 4. 函数的注意事项
# 在Python中，不允许函数重名，如果函数重名了，后一个函数会覆盖前一个函数
# 尽量不要函数名一样
# 不要重写函数


# 5. 递归的基本使用
# 求1~n的和
def add_one_n(n):
    if n == 0:
        return 0
    return n + add_one_n(n - 1)


res = add_one_n(10)
print(res)


# 使用递归求n! n! = n*(n-1)!
def factorial2(n):
    return n * factorial(n - 1)


res = factorial2(3)
print(res)

# 使用递归求斐波那契数列的第n个数字
'''
1+1=2 1
1+2=3 2
2+3=5 3
3+5=8 4
5+8=13 5
8+13=21 6
13+21=34 7
'''


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


fbnq = fibonacci(7)
print('fbnq:', fbnq)  # TODO 演示错误
# ---------------------------------------------------------------------------------------------------

# 匿名函数
# 用来表达一个简单的函数，函数调用的次数很少，基本上就是调用一次
# 调用匿名函数两种方式:
# 1.给它定义一个名字(很少这样使用)
# 2. 把这个函数当做参数传给另一个函数使用
a = lambda a, b: a + b
print(a(1, 2))


def calc(a, b, fn):
    return fn(a, b)


def add(a, b):
    return a + b


def minus(x, y):
    return x - y


# 回调函数
x1 = calc(1, 2, add)  # 3
x2 = calc(10, 5, minus)  # 5
print(x1, x2)

x3 = calc(1, 2, lambda x, y: x + y)
print(x3)

# ---------------------------------------------------------------------------------------------------
# 有几个内置函数和内置类,用到了匿名函数
# sorted内置函数,不会改变原有的数据,而是生成一个新的有序的列表
ints = (5, 9, 2, 1, 3, 8, 7, 4)
x = sorted(ints)
print(ints)
print(x)

# 字典和字典之间不能使用比较运算
students = [{'name': '张三1', 'age': 18, 'height': 180},
            {'name': '张三3', 'age': 30, 'height': 185},
            {'name': '张三2', 'age': 19, 'height': 182},
            {'name': '张三4', 'age': 13, 'height': 170}]


# 通过返回值告诉sort方法,按照元素的那个属性进行排序
def foo(ele):
    return ele['height']


# students.sort(key=foo)
# print(students)
print(id(students))
students.sort(key=lambda x: x['age'])
print(students)
print(id(students))

# ---------------------------------------------------------------------------------------------------
# filter对可迭代对象进行过滤,得到的是一个filter对象
# Python2的时候是内置函数, Python3修改成了-一个内置类
ages = [12, 23, 30, 17, 16, 22, 19]
x = filter(lambda ele: ele > 18, ages)
print(x, list(x), type(x))  # <filter object at 0x0000020EE0CB3A00> [23, 30, 22, 19] <class 'filter'>

# map
y = map(lambda x: x + 1, ages)
print(y, list(y), type(y))  # <map object at 0x0000020EE0C95D90> [13, 24, 31, 18, 17, 23, 20] <class 'map'>

# reduce
from functools import reduce  # 导入模块的语法

z = reduce(lambda x, y: x + y, ages)
print(z, type(z))  # 139 <class 'int'>


# ---------------------------------------------------------------------------------------------------
# 函数参数总结
# 1. 位置参数 调用函数时，传入的两个值按照位置顺序依次赋给参数
# 2. 默认参数 默认参数可以简化函数的调用。设置默认参数时，有几点要注意：一是必选参数在前，否则Python解释器报错
#       二是如何设置默认参数：当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#       使用默认参数有什么好处？最大的好处是能降低调用函数的难度。而一旦需要更复杂的调用时，又可以传递更多的参数来实现。
#       定义默认参数要牢记一点：默认参数必须指向不变对象！
# 3. 可变参数 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
# 4. 关键字参数 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
#       关键字参数有什么用？它可以扩展函数的功能。
#       extra = {'city': 'Beijing', 'job': 'Engineer'}
#       **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
# 5. 命名关键字参数 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
#       如果要限制关键字参数的名字，就可以用命名关键字参数
#       def person(name, age, *, city, job):        和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#       def person(name, age, *args, city, job):    如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
#       命名关键字参数必须传入参数名

# 6. 参数组合
#       在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#       但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
