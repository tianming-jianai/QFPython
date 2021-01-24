# 使用bool内置类可以将其他数据类型转换成为布尔值
print(bool(100))
print(bool(-1))
# 数字里，只有数字0被转换成为布尔值是False,其他数字转换成为布尔值都是True
print(bool(0))
print(bool('hello'))
print(bool('False'))

# 字符串里，只有空字符串可以转换成为False,其他字符串都转换成为True
print(bool(''))
# None转换成为布尔值是False
print(bool(None))

print(bool([]))  # 空数组
print(bool(()))  # 空元组
print(bool({}))  # 空字典
print(bool(set())) # 空集合

# 在计算机里, True和False其实就是使用数字1和日来保存的
print(True+1)
print(False+1)

# 臆式类型转换
if 3>2:
    print('hello')

if 3:
    print('hello')

if 0:
    print('hello')
