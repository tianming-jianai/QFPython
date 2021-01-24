# -------------算数运算符-----------------------
# Python里支持很多算数运算符
# + - * /  **幂运算 //除数  %余数
print(1 + 1)  # 2
print(4 - 1)  # 3
print(3 * 2)  # 6

# Python3里，两个整数相除，得到的结果
print(6 / 2)  # 3.0
print(9 / 2)  # 4.5
print(10 / 3)  # 3.3333333333333335

print(3 ** 3)  # 27
print(81 ** (1 / 2))  # 9.0

# 字符串中里有限度的支持加法和乘法运算符

# 加法运算符：只能用于两个字符串类型的数据，用来拼接两个字符串
print('hello' + 'world')
# print('18' + 1)  # 在Python中数字和字符串之间不能做加法运算
# 乘法运算符：可以用于数字和字符串之间，用来将一个字符串重复多次
print('hello' * 2)

# -------------赋值运算符-----------------------
x = 1
x += 1
print(x)
x -= 1
print(x)
x *= 2
print(x)
x /= 2
print(x)
x **= 4
print(x)
x //= 5
print(x)
x %= 6
print(x)

a = b = c = d = 'hello'
print(a)
print(b)
print(c)

# 拆包时，变量个数和值得个数不一致就报错
e, f = 3, 5  # 拆包
print(e)
print(f)
g = 'hello', 'world'
print(type(g))  # <class 'tuple'>
# * 表示可变长度
h, *i, j = 1, 2, 3, 4, 5, 6
print(h, i, j)  # 1 [2, 3, 4, 5] 6
# -------------比较运算符-----------------------
# > < >= <= != ==
# 字符串之间：根据各个字符的编码值进行逐一比较,ASCII
print('a' > 'b')  # False
print('abc' > 'b')  # False
# 数字和字符串之间： == 结果是False, != 结果是True, 其他 报错
print('a' == 5)
print('a' != 5)
# print('a' > 90)
# -------------逻辑运算符-----------------------
print('------逻辑---------')
# 逻辑与规则:只要有一个运算数是False,结果就是False;只有所有的运算数都是True,结果才是True
print(2 > 1 and 5 > 3 and 10 > 2)  # True
print(3 > 5 and 5 < 4 and 6 > 1)  # False
# 逻辑或规则:只要有一个运算数是True,结果就是True;只有所有的运算数都是False,结果才是False
print(3 > 9 or 4 < 7 or 10 < 3)  # True
print(3 > 5 or 4 < 2 or 8 < 7)  # False
# 逻辑非运算:True ==> False False ==> True
print(not (5 > 2))  # False

# 与and 或or 非not
# 短路与
4 > 3 and print('hhh')
4 < 3 and print('lll')

# 短路或
4 > 3 or print('hhh')
4 < 3 or print('lll')

# 逻辑与运算结果，一定是布尔值吗？不一定
# 逻辑与运算做取值时，取第一个为False的值，如果所有的运算数都是True，取最后一个值
# 短路：只要遇到False就停止，不再继续执行了
print(3 and 5 and 0 and 'hello')  # 0
print(3 and 5 and 1 and 'hello')  # hello

# 逻辑或运算做取值时，取第一个为True的值，如果所有元素都是False，取最后一个值
# 短路：只要遇到True就停止，不再继续执行了
print(0 or [] or 'lisi' or 5)  # lisi
print(0 or [] or {} or ())  # ()

# -------------位运算符-----------------------
# 按位 &与 |或 ^异或 <<左移 >>右移 ~取反
k = 23
l = 15
print(k & l)  # 7
print(k | l)  # 31
print(k ^ l)  # 24

print(5 << 3)  # a << n ==> a * 2的n次方
print(16 >> 2)  # a << n ==> a / 2的n次方

color = 0xF0384E
red = hex(color >> 16)
green = hex(color >> 8 & 0xFF)
blue = hex(color & 0xFF)
print(bin(color), red, green, blue)

# 逻辑运算符的优先级：not > and > or
print(True or False and True)  # True
print(False or not False)  # True
print(True or True and False)  # True

# ------------------------------------------------------
# + :可以用来拼接 字符串/元组/列表
print('hello' + 'world')
print(('good', 'yes') + ('hi', 'ok'))
print([1, 2, 3] + [4, 5, 6])

# - :只能用于集合，求差集
print({1, 2, 3} - {3})

# * :可以用于字符串元组列表，表示重复多次。不能用于字典和集合
print('hello' * 3)
print([1, 3, 4] * 3)
print((1, 3, 4) * 3)
# 字典/集合都是不重复的

# in成员运算符 字符串 元组 列表 字典
print('zhangsan' in {'name': 'zhangsan', 'age': 18, 'height': '180cm'})  # False
print('name' in {'name': 'zhangsan', 'age': 18, 'height': '180cm'})  # True

nums = [19, 82, 39, 12]
# 带下标的遍历
# enumerate 类的使用，一般用于列表和元组等有序的数据
for i, e in enumerate(nums):
    print('第%d个数据是%d' % (i, e))

ll = {'name': 'zhangsan', 'age': 18, 'height': '180cm'}
for i,e in enumerate(ll):
    print('%s的值是%s' % (i,e))
