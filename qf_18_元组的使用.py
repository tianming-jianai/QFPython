# 元组和列表的区别在于 列表是可变的，而元组是不可变数据类型
words = ['hello', 'yes', 'good', 'hi']  # 列表 [] 表示
nums = (9, 4, 3, 1, 9, 7, 6, 9, 3, 9)  # 元组 () 表示

# 和列表一样了，也是一个有序的存储数据的容器
# 可以通过下标来获取元素
print(nums[3])  # 1
# nums[3] = 40 # 'tuple' object does not support item assignment
print(nums.index(7))  # 5 获取存在元素下标
# print(nums.index(99)) # 不存在则报错
print(nums.count(9))  # 4 获取元素个数
print(nums.count(99))  # 0 不存在返回0

# 特殊情况
# ages = (18)
# print(type(ages))  # <class 'int'> 这种书写方式，ages是一个整数,并不是一个元组
ages = (18,)  # 如果元组里面只有一个元素,要在最后面加逗号,
print(type(ages))  # <class 'tuple'>

# tuple内置类
# print(tuple(18)) # TypeError: 'int' object is not iterable
print(tuple('hello'))  # ('h', 'e', 'l', 'l', 'o')

# 怎么把列表转换为元组?元组转换为列表?
print(tuple(words))
print(list(nums))

heights = ('189', '174', '170')
print('*'.join(heights))
print(''.join(('h', 'e', 'l', 'l', 'o')))

# 元组也可以遍历
for i in nums:
    print(i)
