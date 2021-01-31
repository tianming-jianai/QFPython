class Person(object):
    """
    这是一个人类
    """
    __slots__ = 'name','age'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, '正在吃饭')


p = Person('zhangsan', 18)

print(dir(p))  # 列出对象的所有属性/函数
print(p.__class__)  # 是什么类 <class '__main__.Person'>
# print(p.__dict__)  # 转换为字典 {'name': 'zhangsan', 'age': 18}
print(p.__dir__())  # 等价于 dir()
print(p.__doc__)  # 文档注释
print(Person.__doc__)  # 文档注释
print(p.__module__) # 模块名字
print(p.__slots__) # ('name', 'age') 规定了类的私有属性
