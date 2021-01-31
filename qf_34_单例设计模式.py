class Singleton(object):
    __isinstance = None
    __is_first = True

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            # 申请内存，创建一个对象，并把对象的类型设置为cls
            cls.__isinstance = object.__new__(cls)
        return cls.__isinstance

    def __init__(self, a, b):
        if self.__is_first:
            self.a = a
            self.b = b
            self.__is_first = False


# __new__方法申请内存
# 如果不重写__new__ 方法， 会调用object的_ .new__ 方法
# object的__new_ 方法会申请内存
# object的__new__ 方法会申请内存
# 如果重写了__new__ 方法 ,需要自己手动的申谓内存
s1 = Singleton('哈哈', 'hh')
s2 = Singleton('呵呵呵', 'hhh')

print(s1 is s2)  # True

print(s1.a, s1.b)
