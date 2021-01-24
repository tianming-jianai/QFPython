names = ['张三', '李四', '王五', 'jack', '张飞', '关羽', '刘备', '曹操', '孔明']
print(names[3])
names[3] = '花木兰'
print(names)

# 可以通过下标实现切片 ------------------------------------------------------------
print(len(names))
print(names[3:7])  # 包含左边不包含右边

# 列表的数据操作
names.append('黄忠')
print(names)

# insert(index,object) 需要两个参数
# index 表示下标，在哪个位置插入数据
# object 表示对象，具体插入哪个对象
names.insert(2, '李白')  # 下标后面插入
print(names)

x = ['马可波罗', '狄仁杰']
names.extend(x)  # 需要一个可迭代对象，将一个可迭代对象添加到列表
print(names)
print(x)

# 删除数据有三个相关方法：pop  remove clear --------------------------------------------------
# pop 方法默认删除最后一个元素，并返回这个数据
print(names.pop())  # 狄仁杰
print(names)
# pop还可以传入index参数，用来删除指定位置上的数据
print(names.pop(3))
print(names)

names.remove('张三')
# names.remove('孙思邈') # 如果数据在列表中不存在，报错
print(names)

# clear 用来清空列表
# names.clear()
# print(names)

# 使用 del 也可以删除一个数据 不推荐使用
del names[2]
print(names)

# 查询相关方法 ------------------------------------------------------------------------
print(names.index('李白'))  # 1
# print(names.index('八十万禁军教头：林冲')) # 元素不存在，报错
print(names.count('孔明'))  # 1
print(names.count('林冲'))  # 0 不存在
# in 运算符
print('刘备' in names)  # True
print('苏武' in names)  # False

# 修改元素 ----------------------------------------------------------------------------
names[3] = '苏秦'
print(names)

# 遍历列表 ----------------------------------------------------------------------------
for i in names:
    print(i)

i = 0
while i < len(names):
    print(names[i])
    i += 1

# 交换两个变量的值
a = 10
b = 20
# 方法一：使用第三个变量实现
c = a
a = b
b = c
print('a=', a, ',b=', b)
# 方法二：使用运算符实现 只能是数字
a = a + b
b = a - b
a = a - b
print('a=', a, ',b=', b)
# 方法三：使用异或实现 原理：a ^ b ^ b = a
print(a, bin(a))
print(b, bin(b))
a = a ^ b
print(a, bin(a))

b = a ^ b
a = a ^ b
print('a=', a, ',b=', b)
# 方法四：使用Python特有
a, b = b, a
print('a=', a, ',b=', b)

# 列表排序和反转 ---------------------------------------------------------------------------

nums = [6, 5, 3, 1, 8, 7, 2, 4]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# 内置函数sorted，不会改变原有的列表数据，会生成一个新的有序数据
nums2 = [6, 5, 3, 1, 8, 7, 2, 4]
x = sorted(nums2)
print(nums2)
print(x)

print(x[::-1])
