# 集合是一个不重复的无序的可以使用{}或者set来表示
# {} 有两种意思:字典/集合
# {} 里如果放的是键值对,它是一个字典,如果{}放的是单个的值,就是一个集合
person = {'name': 'zhangsan', 'age': 18}
x = {'hello', 1, 'good'}
print(type(person), type(x))  # <class 'dict'> <class 'set'>

# 如果有重复的数据,会自动去除
names = {'zs', 'ls', 'ww', 'zs', 'ls', 'ww'}
print(names)  # {'zs', 'ls', 'ww'}
# 添加一个元素
names.add('ll')
print(names)  # {'ll', 'ww', 'ls', 'zs'}
# 清空集合
# names.clear()
# print(names)  # set() 空集合

# names.pop()  # 随机删除一个元素
# print(names)

names.remove('zs')  # 删除指定元素 ,删除不存在的元素报错
print(names)

x = names.union({'zbs', 'gdg'})  # 两个集合拼接为一个新的集合
print(x)  # {'gdg', 'ls', 'zbs', 'll', 'ww'}
print(names)  # {'ll', 'ls', 'ww'}

names.update({'zbs', 'gdg'})  # 将一个集合拼接入另一个集合
print(names)  # {'zbs', 'gdg', 'ww', 'll', 'ls'}

# 集合的高阶使用 ---------------------------------
first = {'李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石'}
second = {'李商隐', '杜甫', '李白', '白居易', '岑参', '王昌龄'}
third = {'李清照', '刘禹锡', '岑参', '王昌龄', '苏轼', '王维', '李白'}

# set 支持很多算数运算
# print(first+second)  # unsupported operand type(s) for +: 'set' and 'set'/
print(first - second)  # {'王安石', '李清照', '孟浩然', '王维'} 差集
print(first & second)  # {'杜甫', '白居易', '李白', '王昌龄'} 交集
print(first | second)  # {'王昌龄', '李清照', '王维', '岑参', '王安石', '李白', '孟浩然', '李商隐', '白居易', '杜甫'} 并集
print(first ^ second)  # {'岑参', '王维', '孟浩然', '李清照', '王安石', '李商隐'} 非交集
