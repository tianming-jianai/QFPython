# Python循环分为 while 循环和 for 循环
# Python不支持 do...while 循环

# 求1~00之间数的和
result = 0
i = 0
while i < 100:
    i += 1
    result += i
print(result)

# Python的for循环指的是 for...in 循环
# for语句公司：for ele in iterable
# range 内置类用来生成指定区间的整数序列（列表）
# 注意：in的后面必须要是一个可迭代对象
# 目前接触的可迭代对象：字符串、列表、字典、元组、集合、range
for i in range(1, 11):
    print(i)

for i in 'hello':
    print(i)

i = 0
for j in range(1, 101):
    i += j
print(i)

# 素数也叫质数，除了1和它本身以外，不能再被其他的任何数整除
# 求2到100的合数（1既不是质数，也不是合数；2是质数）
for i in range(2, 101):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i, '是质数')

# ----------------九九乘法表------------------------
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j,end='\t')
    print()

