import datetime


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开头的变量是私有变量

    def test(self):
        self.__money += 10  # 类的内部可以使用私有变量

    def get_money(self):
        # 提供访问私有属性的方法的意义是：记录
        print('{}查询了余额'.format(datetime.datetime.now()))
        return self.__money

    def set_money(self, money):
        if type(money) != int:
            print('参数非法')
            return
        print('修改余额了')
        self.__money = money

    def __demo(self):  # 以两个下划战开始的函数，是私有函数，在外部无法调用
        print('我是demo函数，name={}'.format(self.name))


p = Person('张三', 18)
print(p.age)

# 私有函数外部不能调用
# p.__demo()
# 可以通过这种方式调用
p._Person__demo()  # 不推荐
# print(p.__money)  # 不能直接获取私有变量
# 获取私有比那里的方式：
# 1. 使用 对象._类名__私有变量名 获取
print(p._Person__money)  # 1000
# 2. 定义get和set方法访问
print(p.get_money())

p.set_money(2000)
print(p.get_money())

# 3. 使用property访问（后面补充）
