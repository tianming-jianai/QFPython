# 1. 正则表达式
import re

flag = re.match(r'\d{3}\-\d{3,8}$', '010-12345')
print(flag)

# 匹配成功返回一个Match对象，否则返回None

test = '用户收入如的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

# 2. 切分字符串
print('a b   c'.split(' '))  # ['a', 'b', '', '', 'c']  无法识别连续的空格
print(re.split(r'\s+', 'a b  c'))  # ['a', 'b', 'c']

# 无论多少个空格都可以正常分割
print(re.split(r'[\s\,]+', 'a,b, c  d'))  # ['a', 'b', 'c', 'd']
print(re.split(r'[\s,;]+', 'a,b;; c  d'))  # ['a', 'b', 'c', 'd']

# 3. 分组
# 除了简单的判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组(Group)
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))  # 010-12345
print(m.group(1))  # 010
print(m.group(2))  # 12345
# print(m.group(3))  # 多提取直接报错 IndexError: no such group
print(m.groups(), type(m.group()))  # ('010', '12345')  <class 'str'>

# 4. 贪婪匹配
# 特别指出，正则表达式是贪婪匹配，也就是尽可能匹配多的字符
print(re.match(r'^(\d+)(0*)$', '102300').groups())  # ('102300', '')
# 加个？ 就可以让\d+采用非贪婪模式
print(re.match(r'^(\d+?)(0*)$', '102300').groups())  # ('1023', '00')

# 5. 编译
# 当我们是哦那个正则表达式的是否，re内部会干两件事情
# 1. 编译正则表达式
# 2. 用编译后的正则表达式去匹配字符串

# 如果一个正则表达式要重复使用几千次，出于效率考虑，我们可以预编译该正则表达式，接下来重复使用就不需要编译这个步骤了

re_template = re.compile(r'(\d{3})-(\d{3,8})$')
print(re_template.match('010-12345').groups())  # ('010', '12345')
print(re_template.match('010-80865').groups())  # ('010', '80865')
