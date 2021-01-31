class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name, '正在吃', food)

    # 如果一个方法里没有用到实例对象的任何属性。可以将这个方法成static
    @staticmethod
    def demo():
        print('hello')

    @classmethod
    def test(cls):  # 如果这个函数只用到了类属性，我们可以把定义成为一个类方法
        # 类方法会有一个参数cls，也不需要手动的传参
        # cls 指的是类对象 cls == Person ==> True
        print('yes', cls.type)
        print("cls is Person:", cls is Person)


p = Person('张三', 18)

# 实例对象在调用方法时，不需要给形参self传参,会自动的把实例对康传递给self
p.eat('红烧牛肉面')  # 直接使用实例对象调用方法

# eat对象方法，可以直接使用实例对象.方法名(参数)调用
# 使用对象名.方法名(参数)调用的方式，不需要传递self
# 会自动将对象名传递给self

# 对象方法还可以使用类对象来调用类名.方法名()
# 这种方式，不会自动给self传参。需要手动的指定self
Person.eat(p, '西红柿鸡蛋面')

# 静态方法:没有用到实例对象的任何属饵
Person.demo()
p.demo()

# 类方法:可以使用实例对象和类对象调用
p.test()
Person.test()
