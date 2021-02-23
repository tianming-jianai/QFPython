# struct
# 字节转换
# Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组=二进制str
# 例：32位无符号整数 --> 4个长度字节   位运算：
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = (n & 0xff)
bs = bytes([b1, b2, b3, b4])
print(bs)

# ------------------------
# 在Python中提供了一个struct模块来解决bytes和其他二进制数据类型的转换
# struct 的 pack 函数把任意 数据类型 变成bytes
import struct

a = struct.pack('>I', 10240099)
print(a)

# ------------------------
# unpack把bytes变成相应的数据类型
# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。
b = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(b)
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
# 尽管Python不适合编写底层操作字节流的代码，但是在对性能要求不高的地方，利用struct就方便多了

# ------------------------
# windows 的位图文件.bmp 是一种非常简单的文件格式，我们来用struct分析一下
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# bmp格式采用小端方式存储数据，文件头的结构按顺序如下：
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图； 一个4字节整数：表示位图大小； 一个4字节整数：保留位，始终为0； 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header 的字节数； 一个4字节整数：图像宽度； 一个4字节整数：图像高度； 一个2字节整数：始终为1； 一个2字节整数：颜色数。

# 所以，组合起来用unpack读取
c = struct.unpack('<ccIIIIIIHH', s)
print(c)

# ------------------------
# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
# -*- coding: utf-8 -*-
import base64
import struct


def bmp_info(data):
    info = struct.unpack('<ccIIIIIIHH', data[:30])
    # struct.unpack 如果不明白的可以在廖雪峰老师的python课程中仔细看看，通俗理解就是将二进制数据解析出来
    if info[0] == b'B' and (info[1] == b'M' or info[1] == b'A'):
        # 这里是做相应的判断，判断是否为位图
        return {
            'width': info[6],
            'height': info[7],
            'color': info[9]
        }


# 测试
bmp_data = base64.b64decode(
    'Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
