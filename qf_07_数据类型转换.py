# 进制转换 将int类型以不同的进制表现出来
# 类型转换 将一个类型的数据转换为其他类型的数据
# int ==> str str ==> int bool ==> int int ==> float
# age = input("请输入您的年龄：")
# new_age = int(addrge)
# print(type(new_age))

# -------------int-----------------------

x = '1a2c'
y = int(x, 16)  # 把字符串 1a2c 当做十六进制转换为整数
print(y, type(y))

m = '12'
n = int(m, 16)  # 把字符串 12 当做八进制转换为整数
print(n, type(n))

# -------------float-----------------------

a = '12.34'
# 使用内置函数float可以将其他类型转换为浮点数
b = float(a)
print(b + 1)

# 如果字符串不能被转换为有效的浮点数，会报错
# c = float('hello')
# print(c)

c = 101
print(float(c))

m = float('12')  # 将字符串转换为浮点数
n = float(12)  # 将整型数字抓换为浮点数
print(m, n)

# -------------str-----------------------

# 使用str内置函数可以将其他类型的数据转换为字符串
a = 34
b = str(a)

print(a + 1)
# print(b+1)
print(a, type(a))
print(b, type(b))

# -------------bool-----------------------

{}  # 空字典
s = set({})  # 空集合
print(bool(s), type(s))
# 在Python中，只有空字符串'',"",数字0，空字典{}，空列表[]，空元组()，和空数据None会被抓换为False

# 在计算机里，True和False都是使用数字保存的
print(True + 1)  # 2

# -------------bool-----------------------
# 隐式转换

