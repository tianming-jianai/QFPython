# gbk utf-8 big5
# 字符串转换为指定编码集结果
# GBK编码，一个汉字占两个字节
print('你'.encode('gbk'),ord('你'),bin(20320)) # b'\xc4\xe3' 20320 0b100111101100000
print('你'.encode('utf-8')) # b'\xe4\xbd\xa0' 三个字节

x = b'\xe4\xbd\xa0' # b开头的字符串 表示二进制
print(x.decode('utf-8'))


