# 列表可以存储任意数据类型，但是一般情况下，我们都存储单一数据类型
names = ['zhangsan', 'lisi', 'wangwu']
scores = [100, 98, 97, 99]

# 这个列表的每一个元素到底表示什么？
# 列表只能存储值,但是无法对值进行描述
person = ['zhangsan', 18, 98, 97, 95]

# 字典不仅可以保存值,还能对值进行描述
# 使用大括号来表示一个字典,不仅有值value,还有值的描述key
# 字典里的世界都是以键值对key-value的形式保留的
# key和value之间使用冒号,来连接
# 多个键值对之间使用逗号,来分隔
person = {'name': 'zhangsan',
          'age': 18,
          'height': 170,
          'age': 19,
          'isPass': True,
          'hobbies': ['唱', '跳', 'rap', '篮球'],
          18: 19,
          (18,): 99}
# 1. 字典里的key不允许重复,如果key重复了,后一个key对应的值会覆盖前一个
# 2. 字典里的value可以是任意数据类型,但是key只能使用不可变数据类型,一般使用字符串
print(person)
print(person.get(18))

# 字典的增删改查 --------------------查询---------------------------
# 字典的数据在保存时是无序的,不能通过下标获取
print(person['name'])  # zhangsan 使用key获取到对应的value
# person['hair']  # 找不到key直接报错

# 需求:获取一个不存在的key时,不报错,如果这个key不存在,使用默认值
# 使用字典的get方法,如果key不存在,会默认返回None,而不报错
print(person.get('hair'))
# 如果根据key获取不到value,使用给定的默认值
print(person.get('gender', 'female'))  # female
print(person.get('name', 'lisi'))  # zhangsan

print(person)

# ------------------修改---------------------
# 直接使用key可以修改对应的value
person['name'] = 'lisi'

# ------------------新增---------------------
# 如果key存在,修改key对应的value
# 如果key在字典里不存在,会往字典里添加一个新的key-value
person['gender'] = 'female'
print(person)
# ------------------删除---------------------
# 删除一个元素,结果是被删除的这个元素组成的键值对
res = person.popitem()
print(res, type(res))  # ('gender', 'female') <class 'tuple'>
print(person)

# 把name对应的键值对删除了,执行结果是被删除的value
x = person.pop('name')
print(x)  # lisi
print(person)

del person['age']
print(person)

# 清空字典
person.clear()
print(person)

# ------------------update方法的使用---------------------
# 字符串
s1 = 'hello'
s2 = 'world'
print(s1 + s2)  # helloworld

# 列表可以使用extend方法将两个列表合并成为一个列表
nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]
nums1.extend(nums2)
print(nums1)  # [1, 2, 3, 4, 5, 6, 7, 8]
print(nums1 + nums2)  # [1, 2, 3, 4, 5, 6, 7, 8, 5, 6, 7, 8]

# 元组
words1 = ('hello', 'good')
words2 = ('ok', 'hi')
print(words1 + words2)  # ('hello', 'good', 'ok', 'hi')

# 字典
person1 = {'name': 'zhangsan', 'age': 18, 'addr': 'sh'}
person2 = {'addr': 'sz', 'height': 180}
person1.update(person2)
print(person1)  # {'name': 'zhangsan', 'age': 18, 'addr': 'sz', 'height': 180}

# 字典之间不支持加法运算
# print(person1 + person2)  # unsupported operand type(s) for +: 'dict' and 'dict'

# ------------------字典的遍历---------------------
# 第一种遍历方式:直接使用for...in循环字典
for i in person1:  # for...in循环获取的是key
    print(i, '=', person1[i])
print()

# 第二种遍历方式:获取到所有的key,然后根据key获取value
print(person.keys())  # dict_keys([])
for i in person1.keys():
    print(i, '=', person1[i])
print()

# 第三种遍历方式:获取到所有的value
# 只能拿到值,不能拿到key
for v in person1.values():
    print(v)
print()

# 第四种遍历方式:
print(person1.items())  # dict_items([('name', 'zhangsan'), ('age', 18), ('addr', 'sz'), ('height', 180)])
for item in person1.items():
    print(item[0], '=', item[1])
print()

for k, v in person1.items():
    print(k, '=', v)

# 一般情况下我们使用第一种和第四种


# ---------------字典练习----------------------------

chars = ['a', 'c', 'x', 'd', 'p', 'a', 'c', 'a']
char_count = {}
for char in chars:
    # if char in char_count:
    #     print('字典里面已经有了这个字符%s' % char)
    #     char_count[char] += 1
    # else:
    #     char_count[char] = 1
    if char not in char_count:
        char_count[char] = chars.count(char)

print(char_count)  # {'a': 3, 'c': 2, 'x': 1, 'd': 1, 'p': 1}

# 可以使用内置函数 max 取最大值
vs = char_count.values()
print(max(vs))

for k, v in char_count.items():
    if v == max(vs):
        print(k)

persons = [{'name': 'zhangsan', 'age': 34},
           {'name': 'lisi', 'age': 23},
           {'name': 'wangwu', 'age': 14},
           {'name': 'zhaoliu', 'age': 22},
           {'name': 'houzi', 'age': 12}]
# 让用户输入姓名,如果姓名已经存在,提示用户;如果姓名不存在,继续输入年龄,并存入列表
x = input('请输入您的姓名:')
for person in persons:
    if person['name'] == x:
        print('您输入的名字已存在')
        break
else:
    print('您输入的名字不存在')
    # 创建一个新的字典
    new_person = {'name': x}
    age = int(input('请输入您的年龄:'))
    new_person['age'] = age
    persons.append(new_person)
    print('用户添加成功')
print(persons)

# 字典的key,value互换
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {}
for k, v in dict1.items():
    dict2[v] = k
print(dict2) # {100: 'a', 200: 'b', 300: 'c'}

dict1 = {v: k for k, v in dict1.items()}  # 字典推导式
print(dict1)
