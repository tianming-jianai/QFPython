import random

# pass 关键字在Python里面没有意义，知识单纯的用来占位，保证豫剧的完整性

# 输入年，写代码判断输入的年是否是闰年，并且打印对应的结果。
# (是闰年的条件:能被4 整除但是不能被100整除或者能够被400整除的年)
year = int(input('请输入一个年份：'))
if (year % 4 == 0 and year % 100 != 0) or (year % 1400 == 0):
    print("您输入的是闰年" + str(year))
    pass

# ---------------猜拳游戏---------------------------
print("0剪刀 1石头 2布")
computer = random.randint(0, 2)
print('电脑' + str(computer))
player = int(input('请输入：'))
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("你赢了")
elif player == computer:
    print("平局")
else:
    print("你输了")
    pass

# ------------------if语句注意点------------------------
# 1. 区间判断
score = float(input('请输入您的份数：'))
# 在某些语言里，判断区间不能连写，需要使用逻辑运算符来连接
# score > 0 and score < 60
# Python里可以使用连续的区间判断
if 0 <= score < 60:
    print('不及格')
# 2. 隐式类型转换
if 4:  # if后面需要的是一个bool类型的值，如果if后面不是布尔类型，会自动转换为布尔类型
    print('hello world')
# 3. 三元表达式：对if else语句的简写
num1 = int(input('请输入一个数字：'))
num2 = int(input('请再输入一个数字：'))
# if num1 > num2:
#     x = num1
# else:
#     x = num2
x = num1 if num1 > num2 else num2
print('两个数里较大的是：', x)
