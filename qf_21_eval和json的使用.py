import json

# 内置类 list tuple set
nums = [9, 8, 4, 3, 2, 1]
x = tuple(nums)
print(x)  # (9, 8, 4, 3, 2, 1)

y = set(x)
print(y)  # {1, 2, 3, 4, 8, 9}

z = list({'name': 'zhangsan', 'age': 18, 'score': 98})
print(z)  # ['name', 'age', 'score']

# Python里面有一个比较清淡的内置函数eval,可以执行字符串里的代码
a = 'input("请输入您的姓名:")'  # a是一个字符串
b = '1+1'
print(eval(b))

# JSON的使用,把列表,元组,字典转换为字符串
person = {'name': 'zhangsan', 'age': 18, 'score': 98}
# 字典如果想要把它传入前端页面,或者写入到一个文件中
# dumps转字符串
m = json.dumps(person)
print(m, type(m))  # {"name": "zhangsan", "age": 18, "score": 98} <class 'str'>

# 转换json字符串为字典
# eval loads 转字符串为对象
c = '{"name": "zhangsan", "age": 18, "score": 98}'
d = eval(c)
print(d, type(d))  # {'name': 'zhangsan', 'age': 18, 'score': 98} <class 'dict'>

e = json.loads(c)
print(e, type(e))

# 列表,元组,集合 转换为json
print(json.dumps(nums), type(json.dumps(nums)))  # list -> list [9, 8, 4, 3, 2, 1] <class 'str'>
print(json.dumps(x), type(json.dumps(x)))  # tuple -> list [9, 8, 4, 3, 2, 1] <class 'str'>
print(json.dumps(y))  # set bject of type set is not JSON serializable
