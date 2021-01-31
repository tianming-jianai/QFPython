import house as house


class Student(object):
    # 在__init__方法里，以参数的形式定义特征，我们称之为属性
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print(self.name, '正在跑步')

    def eat(self):
        print(self.name, "正在吃饭")


# Student() ==> 会自动调用__init__方法
# s = Student() # missing 3 required positional arguments: 'name', 'age', and 'height'

s1 = Student('小米', 11, 1.75)
s2 = Student('华为', 10, 1.8)

s1.run()


# -------------------------------------------------------
# self 语句的使用
class Student2(object):
    # 这个属性直接定义在类里，是一个元组，用来规定对象可以存在的属性
    # __slots__ = 'name', 'age'

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print('大家好，我是', self.name)


# Student('张三',18) 这段代码具体做了什么呢？
# 1. 调用了__new__方法，用来申请内存空间
# 2. 调用__init__方法传入参数，将self指向创建好的内存空间，填充数据
# 3. 变量 s1 也指向创建好的内存空间
s1 = Student2('张三', 18)


# -------------------------------------------------------
# Python是动态语言
# print(s1.height) # 没有属性，会报错
# 直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
# 如果这个属性以前存在，会修改这个属性对应的值
# s1.city = '上海' # 动态属性
# print(s1.city)

# 不能随便添加属性 __slots__

# -------------------------------------------------------
# 魔法方法，也叫魔术方法，是类的一些特殊方法
# 特点： 1. 不需要手动调用，会在合适的时候自动调用 # 当然也可以手动调用
#       2. 这些方法都是使用 __ 开头 使用 __结尾
#       3. 方法名都是系统规定好的，在合适的时机自己调用

class Person(object):
    def __init__(self, name, age):
        # 在创建对象的时候，会自动调用这个方法
        print('__init__方法被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时，会自动调用这个方法
        print('__del__方法被调用了')


p = Person('zhangsan', 18)
del p
import time


# time.sleep(3)


# -------------------------------------------------------
# 运算符相关的魔法方法
# __eq__

class Person2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        print('__eq__方法被调用了', other)
        return other.name == self.name and other.age == self.age

    def __ne__(self, other):
        print('__ne__方法被调用了', other)
        return 'hello'

    # 下面这的方法，没有写就报错
    def __gt__(self, other):  # greater than 使用>会自动调用这个方法
        return self.age > other.age

    def __ge__(self, other):  # greater equal 使用>=会自动调用这个方法
        return self.age >= other.age

    # def __le__(self,other): <=
    # def __add__(self, other): +
    # def __sub__(self, other): -
    # def __mul__(self, other): *
    # def __truediv__(self, other): /
    def __str__(self):
        return self.name

    def __int__(self):
        return 20

    def __float__(self):
        return 20.2


# 1. 调用__new__方法申请内存空间
p1 = Person2('zhangsan', 18)
p2 = Person2('zhangsan', 18)

# p1 & p2 是同一个内存对象吗
print('0x%X' % id(p1))  # 0x2CCAA7256D0
print('0x%X' % id(p2))  # 0x2CCAC3854F0

# is 身份运算符 可以用来判断两个对象是否是同一个对象
print(p1 is p2)  # False
print('p1 == p2 :', p1 == p2)  # False  # 本质是调用__eq__方法p1.__eq__(p2)
print('p1 != p2 :', p1 != p2)  # p1 != p2 : hello
print('p1 > p2 :', p1 > p2)  # p1 > p2 : False
print('p1 >= p2 :', p1 >= p2)  # p1 >= p2 : True
# str()将对象转换成为字符串，会自动调用__str__方法
# 1. str() 2. 打印对象也会调用
# str() 默认会转换为类型+内存地址
x = str(p1)
print('x =', x)  # x = zhangsan
print('print:', p1)  # 调用__str__
# int() ==> 调用对象的 __int__方法
print('int(p1)：', int(p1))
# float() 调用 __float__()
print('float(p1)：', float(p1))

nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
print(nums1 is nums2)  # False
print(nums1 == nums2)  # True


# == 会调用对象的__eq__方法，获取这个方法的比较结果
# __eq__ 如果，不重写，比较的依然是地址

# -------------------------------------------------------
def get_alpha(word):
    new_str = ''
    for w in word:
        if w.isalpha():
            new_str += w
    return new_str


print(get_alpha('hello234good'))


# 写一个函数，默认求10的阶乘，也可以求其他数字的阶乘
def get_factorial(n=10):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


print(get_factorial(3))


# 判断是否以指定字符串结尾
def my_endwith(old_str, str1):
    return old_str[-len(str1):] == str1


print(my_endwith('hello', 'llo'))


# 判断字符串中是否是纯数字
def my_digit(old_str):
    for i in old_str:
        if not '0' <= i <= '9':
            return False
    return True


print(my_digit('112233'))


# 面向对象联系
# 新房子没有任何家具
# 将家具名称追加到家具名称列表中
# 判断家具的面积，是否超过剩余面积，如果超过，提示不能添加这件家具

class House(object):
    def __init__(self, house_type, total_area, fru_list=None):
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        if fru_list is None:
            fru_list = []
        self.fru_list = fru_list

    def add_fru(self, x):
        if x.area > self.free_area:
            print('剩余面积不足，放不进去了')
        else:
            self.fru_list.append(x.name)
            self.free_area -= x.area
            print('需要将家具添加到房子里')


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


house1 = House('三室一厅', 120)
bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

house1.add_fru(bed)
house1.add_fru(chest)
house1.add_fru(table)
print(house1.free_area)
