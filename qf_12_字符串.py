# 如果字符串里还有双引号,外面就可以使用单引号
m = 'xiaoming said "I am xiaoming"'
n = "I'm xiaoming"

p = """
I'm xiaoming
xiaoming said "I'm xiaoming"
"""
q = ""
print(m, n, p, q)

# -------------------------
# 切片
r = "hello world"
print(r[4])

# -------------------------
# 字符串常见操作
a = "abcdebcfg"
# 获取字符串长度
print(len(a))
# 查找内容相关的方法 find/index/rfind/rindex 可以获取指定字符的下标
print(a.find('l'))  # 不存在返回-1
# print(a.index('l')) # 不存在报错

print('bc所在位置：', a.find('bc', 1, 5))

print('bc所在位置：', a.rfind('bc'))

# 字符串操作里面没有查找每一个出现相同子串位置的操作，需要使用正则表达式

# --------------------------------------------------
# 字符串中使用算数运算符
print('hello' + 'world')  # 加法运算符:只能用于两个字符串类型的数据，用来拼接两个字符串
# print('18'+1) # 在Python里，数字和字符串之间，不能做加法运算
print('hello' * 5)  # 乘法运算符:可以用于数字和字符串之间,用来将- -个字符串重复多次

# startweith, endwith, isalpha, isdigit, isalnum, isspace
# is 开头的判断，结果是一个布尔型
print('hello'.startswith('he'))  # True
print('hello'.endswith('lo'))  # True
print('hello'.isalpha())  # True
print('123'.isdigit())  # True
print('1www23'.isalnum())  # 是否由数字和字母组成 True
print('    '.isspace())  # 是否全部由空格组成 True

print('-------------------replace----------------------------')
# replace方法：用来替换字符串
word = 'hello'
m = word.replace('l', 'x')  # replace 将字符串里l替换成x
print(word)  # hello 字符串是不可变数据类型
print(m)  # 原来的字符串不会改变，而是生成-个新的字符串来保存替换后的结果

print('-------------------split----------------------------')
# split splitlines partition repartition
# 字符串类型的数据
x = 'zhangsan-lisi-wangwu-jerry-merry-jack'
y = x.split('-')  # 切割为列表
print(x)
print(y, type(y))  # list
print(x.split('-', 2))  # ['zhangsan', 'lisi', 'wangwu-jerry-merry-jack']
print(x.rsplit('-', 2))  # ['zhangsan-lisi-wangwu-jerry', 'merry', 'jack']

# partition 指定一个字符串作为分隔符，分为三个部分
# 前面  分隔符  后面
print('abcdecfg'.partition('c'))  # tuple ('ab', 'c', 'decfg')
print('abcdecfg'.rpartition('c'))  # tuple ('abcde', 'c', 'fg')

print(r'\abc')
print(x[::-1])

print('---cap-------------------')
# 修改大小写
print(x.capitalize())  # 首字母大写
print(x.upper())  # 全大写
print(x.title())  # 每个单词的首字母大写
print(x.lower())  # 全小写

print('---补全--------------------')
# ljust让字符串以指定长度显示,如果长度不够,默认在右边使用空格补齐
m = 'sunday'
print(m.ljust(10, '-'))  # sunday----
print(m.rjust(10, '-'))  # ----sunday

print(m.center(20, '*'))  # *******sunday*******

# --------去除空格-----------------
n = '   abc   '
print(n.lstrip())
print(n.rstrip())
print(n.strip())

# 将列表转换为字符串
fruits = ['apple', 'pear', 'peach', 'banana', 'orange', 'grape']
# join 参数是：可迭代对象
print('-'.join(fruits))  # 列表 apple-pear-peach-banana-orange-grape
print('*'.join('hello'))  # 字符串 h*e*l*l*o
print('+'.join(('yes', 'ok')))  # 元组 yes+ok

# 格式化
name = 'zhangsan'
age = 18
print('大家好，我的名字是', name, ',我今年', age, '岁了', sep='')
print('大家好，我的名字是%s,我今年%d岁了,我今天赚了%f块钱' % (name, age, 3.14))

print('我是%d号男嘉宾' % 5)  # 数字
print('我是%3d号男嘉宾' % 5)  # 左边空格
print('我是%-3d号男嘉宾' % 5)  # 右边空格
print('我是%03d号男嘉宾' % 5)  # 左边补0补到共3位
print('我今天赚了%.2f块钱' % 3.135)  # 保留两位小数 %f 浮点数占位符
print('今天股票赚了%d%%' % 10)  # %% 输出百分号

a = 255
print('%x' % a)  # ff
print('%X' % a)  # FF

# {} 也可以进行占位
# {} 什么都不写，会读取后面的内容，一一对应填充
x = '大家好，我是{}，我今年{}岁了'.format('张三', 25)
print(x)

# {数字} 根据数字的顺序来进行填入。数字从0开始
y = '大家好,我是{1},我今年{0}岁了'.format(20, 'jerry')
print(y)

# {变量}
u = '大家好，我是{name},我今年{age}岁了,我来自{addr}'.format(name='zhangsan', age=18, addr='orange')
print(u)
# 混合使用 {数字} {变量}
v = '大家好，我是{1},我今年{0}岁了,我来自{addr}'.format(18, 'zhangsan', addr='orange')
print(v)
#  {} 空大括号和{数字}不能混合使用

d = ['zhagnsan', 18, '上海', 180]
b = '大家好，我是{},我今年{}岁了,我来自{},身高{}cm'.format(*d)
print(b)
dd = {'name': 'zhagnsan', 'age': 18, 'addr': '上海', 'height': 180}
c = '大家好，我是{name},我今年{age}岁了,我来自{addr},身高{height}cm'.format(**dd)
print(c)
