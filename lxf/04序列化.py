# 序列化
# 们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化

import pickle

d = dict(name='Bob', age=20, score=88)
a = pickle.dumps(d)
print(
    a)  # b'\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03Bob\x94\x8c\x03age\x94K\x14\x8c\x05score\x94KXu.'

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写
# 入一个file-like Object

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法
# 从一个file-like Object中直接反序列化出对象
f2 = open('dump.txt', 'rb')
d = pickle.load(f2)
f.close()
print(d, type(d))  # {'name': 'Bob', 'age': 20, 'score': 88} <class 'dict'>
# 变量的内容又回来了！
# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已


# 2. JSON
# 在不通的编程语言之间传递对象，就必须把对象序列化为标准格式，比如xml,单更好的方法时序列化为json,因为json表示出来就是一个字符串，可以被所有语言读取，
# 也可以方便的存储到磁盘或者通过网络传输。json不仅是标准格式，而且比xml更快，而且可以直接在web页面读取，非常方便。
# json表示的对象就是标准的JavaScript语言的对象，


# python内置json模块提供了非常完善的Python对象到json格式
import json

j = dict(name='Bob', age=20, score=88)
print('序列化dumps', json.dumps(j), type(json.dumps(j)))  # {"name": "Bob", "age": 20, "score": 88} <class 'str'>

# 要把json序列化为python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str = '{"age":20,"score":88,"name":"Jerry"}'
dd = json.loads(json_str)
print('反序列化loads', dd, type(dd))  # {'age': 20, 'score': 88, 'name': 'Jerry'} <class 'dict'>


# 3. json进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Jack', 20, 99)


# print(json.dumps(s))  # TypeError


# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# 这样Student实例就先被student2dict转换为dict,然后被序列化为json
jj = json.dumps(s, default=student2dict)
print(jj, type(jj))  # {"name": "Jack", "age": 20, "score": 99} <class 'str'>

# 偷懒
print('序列化dumps', json.dumps(s, default=lambda obj: obj.__dict__))  # {"name": "Jack", "age": 20, "score": 99}


# 把json反序列化为一个Student对象
def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])


print('反序列化loads', json.loads(json_str, object_hook=dict2Student))

obj = dict(name='小米', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)  # {"name": "\u5c0f\u7c73", "age": 20} # 名称变为ASCII方式表示
