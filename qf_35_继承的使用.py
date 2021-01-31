# 面向对象编程有三大特性:封装、 继承和多态
# 封装:函数是对语句的封装;类是对函数和变量的封装
# 继承:类和类之间可以认为手动的建立父子关系，父类的属性和方法，子类可以使用
# 多态:是一种技巧，提高代码的灵活度

class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '睡觉了')


class Dog(Animal):
    def bark(self):
        print(self.name + "正在叫")


class Student(Animal):
    def study(self):
        print(self.name + '正在好好学习')


# Dog()调用
# __new__方法,再调用__init__ 方法
# Dog里没有__new__ 方法 ，会查看父类是否重写了__new__ 方法
# 父类里也没有重写__new_ 方法 ,查找父类的父类,找到了object

# 调用__init__方法Dog类没有实现，会自动找Animal父类
d1 = Dog('小黑', 2)
print(d1)
d1.bark()

s1 = Student('小明', 18)
s1.study()

# Rython里允许多继承

# 如果两个不同的父类有同名方法,有一个类属性可以查看方法的调用顺序
s1.sleep()
print(Student.__mro__)  # (<class '__main__.Student'>, <class '__main__.Animal'>, <class 'object'>)


# ------------------------------------------------------------------------------
# 手动的指定Student类继承自object
class Student(object):
    pass


# 没有指定Dog的父类, python3.里默认继承自object
class Dog1:
    pass

# 新式类和经典类的概念:
# 1.新式类:继承自object 的类我们称之为新式类
# 2. 经典类:不继承自object 的类


# 在python2里,如果不手动的指定-个类的父类是object,这个类就是一个经典类
# python3里不存在经典类,都是新式类
