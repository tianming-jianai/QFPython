class Person(object):
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __setitem__(self, key, value):
        print('setietm方法被调用了，key={},value={}'.format(key, value))
        # self.key = value # 会给类添加一个key的属性
        self.__dict__[key] = value  # 正确的修改属性的值

    def __getitem__(self, item):
        return self.__dict__[item]


p = Person('张三', 18, '洛阳')
print(p.__dict__)  # {'name': '张三', 'age': 18, 'city': '洛阳'}

# 不能直接把一个对象当作字典使用
p['age'] = 20  # [] 语法会调用对象的__setitem__方法
print(p.age)

print(p['name'])  # 不能当作字典获取属性 会调用__getitem__方法
