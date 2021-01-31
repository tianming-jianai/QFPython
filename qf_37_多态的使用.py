# 多态基于继承，通过子类重写父类方法
# 达到不同的子类对象调用相同的父类方法，得到不同的结果
# 提高代码的灵活度
class Dog(object):
    def work(self):
        print('狗正在工作')


class PoliceDog(Dog):
    def work(self):
        print('警犬正在攻击坏人')

    pass


class BlindDog(Dog):
    def work(self):
        print('导盲犬正在工作')


class DrugDog(Dog):
    def work(self):
        print('缉毒犬正在工作')


class Person(object):
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog

    def work_with_dog(self):
        if isinstance(self.dog, Dog):
            self.dog.work()



pd = PoliceDog()
police = Person('张警官', pd)
police.work_with_dog()

bd = BlindDog()
police2 = Person('张警官', bd)
police2.work_with_dog()

dd = DrugDog()
police3 = Person('张警官', dd)
police3.work_with_dog()
