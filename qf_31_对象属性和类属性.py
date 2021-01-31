class Person(object):
    type = '人类'  # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 对象 p 是通过 Person 类创建出来的
p = Person('zs', 18)

# Person类存在哪个地方
# 只要创建了一个实例对象，这个实例对象就有自己的name和age属性
# 对象属性，每个实例对象都单独保存的属性
# 每个实例对象之间的属性没有关联，互不影响

# 获取类属性：可以通过类对象和实例对象获取
print(Person.type)
print(p.type)

p.type = 'monkey'  # 并不会修改类属性，而是给实例对象添加了一个新的属性
print(p.type)
print(Person.type)

# 类属性只能通过类对象修改，实例对象无法修改类属性
Person.type = 'human'
print(p.type)
