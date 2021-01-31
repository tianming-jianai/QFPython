# 继承特点:如果一个类A 继承自类B,由类A创建出来的实例对象都能直接使用类B里定义的方法

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Student(Person):
    def __init__(self, name, age, school):
        # self.name = name
        # self.age = age
        # 子类在父类实现的基础上，又添加了自己的新功能
        # 调用父类方法的两种方式：
        # 1. 父类名.方法名(self,参数列表)
        # Person.__init__(self, name, age)
        # 2. 使用super直接调用父类的方法，推荐
        super(Student, self).__init__(name, age)
        self.school = school

    def sleep(self):
        print(self.name + '正在课间睡觉')

    def study(self):
        print(self.name + '正在' + self.school + '学习')


s = Student('jerry', 18, '复旦大学')  # 调用了父类的init方法
s.sleep()  # 调用了父类的sleep方法
print(Student.__mro__)  # mro method resolution order

# 1. 子类的实现和父类的实现完全不- -样,子类可以选择重写父类的方法。
# 2. 子类在父类的基础上又有更多的实现
s.study()
