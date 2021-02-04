# 1. 读文件
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便

try:
    f = open('../xxx.txt', 'r', encoding='utf8')
    print(f.read())
finally:
    if f:
        f.close()
# 避免IOError 使用with 代替 try finally ,自动调用f.close()
with open('../xxx.txt', 'r', encoding='utf8') as f:
    print(f.read())

with open('../xxx.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():  # readlines()一次读取所有内容并按行返回list
        print(line.strip())  # 把末尾的'\n'删掉

# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。


# 2. 二进制文件
# rb 读取二进制文件

# errors='ignore'  如果遇到编码错误后  直接忽略

# 3. 写文件
# w 写文本文件 wb 写二进制文件
# f = open('../xxx.txt', 'w')  # 覆盖
# f.write('hello world')
# f.close()

f = open('../xxx.txt', 'a')  # 追加
f.write('hello word')
f.close()

print()
# ----------------------------------------------------
# 3. StringIO /  BytesIO
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
from io import StringIO

f = StringIO()
f.write('hello')
f.write('  ')
f.write('world!')
print(f.getvalue())  # getvalue()用于获取写入后的str
f.close()

print()
print('读取StringIO可以用一个str初始化StringIO,然后像文件一样读取')
f = StringIO('hello!\n Hi! \n Goodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
f.close()

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf8'))  # 写入的是经过utf-8编码的bytes
print(f.getvalue())  # b'\xe4\xb8\xad\xe6\x96\x87'
f.close()

# 初始化一个BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf8'))
f.close()
print()

# 4. 操作文件和目录
# 如果要在Python程序中执行这些目录和文件的操作怎么办？Python内置的os模块也可以直接调用操作系统提供的接口函数
import os

print(os.name)  # 操作系统类型
# print(os.uname())  # 详细的系统信息  # uname()函数在Windows上不提供
print(os.environ)  # 操作系统所有的环境变量
# 获取某个环境变量的值
print(os.environ.get('JAVA_HOME'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
dir = os.path.join('../lxf', 'testdir')  # 拼接文件路径
print(dir)

os.mkdir(dir)  # 创建一个目录  当文件已存在时，无法创建该文件。: '../lxf/testdir'
# 删除一个目录
os.rmdir('./testdir')

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
dirs = os.path.split(dir)
print(dirs)
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# 操作文件
# os.rename('test.txt', 'test.py')
# os.remove('test.py')

# python 本身不提供文件复制功能  shutil 模块提供了 copyfile()函数
# python 过滤文件
a = [x for x in os.listdir('.') if os.path.isdir(x)]  # 列出当前文件夹下的所有目录
print(a)

# 列出所有的.py文件
b = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.split('x')[1] == 'py']
print(b)
