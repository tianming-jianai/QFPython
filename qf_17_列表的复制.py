import copy

# 可变类型和不可变类型
a = 12
b = a
print('修改前：', id(a), id(b))
a = 10
print('修改后：', id(a), id(b))
print('a=', a)
print('b=', b)

nums = [100, 200, 300]
nums2 = nums
print('修改前：', id(nums), id(nums2))
nums[1] = 2
print('修改后：', id(nums), id(nums2))
print(nums)
print(nums2)

# Python里的数据都是保存在内存里的
# Python里的数据又分为可变类型和不可变类型
# 不可变类型:字符串、数字、元组
# 可变类型:列表、字典、集合

# 不可变数据类型，如果修改值，内存地址会发生变化
# 可变数据类型，如果修改值，内存地址不会发生变化

# 列表的浅复制

# 深拷贝只能使用copy模块实现
words = ['hello', 'good', [100, 200, 300], 'yes', 'hi', 'ok']
# word1是words的浅拷贝
# 浅拷贝认为只拷贝了一层
words1 = words.copy()
print('hello:', id(words[1]), 'hello1:', id(words1[1]), 'words:', id(words))
print('list:', id(words[2]), 'list1:', id(words1[2]), 'words1:', id(words1))
# 浅拷贝：内置列表地址一样

# 深拷贝的words2
words2 = copy.deepcopy(words)
print('hello:', id(words[1]), 'hello2:', id(words2[1]), 'words:', id(words))
print('list:', id(words[2]), 'list2:', id(words2[2]), 'words2:', id(words2))
# 深拷贝：内置列表地址不一样
