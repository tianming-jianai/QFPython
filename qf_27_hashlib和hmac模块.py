import hashlib
import hmac

# 这两个模块都是用来进行数据加密
# hashlib模块里主要支持两个算法 md5 和 sha 加密
# 加密方式： 单向加密： 只有加密过程，不能解密md5/sha 对称加密 非对称加密rsa

# 需要将加密的内容转换为二进制
x = hashlib.md5()  # 生成一个md5对象
x.update('abc'.encode('utf-8'))
print(x.hexdigest())  # 十六进制数字 # 900150983cd24fb0d6963f7d28e17f72

# 文件MD5

# 加密后的字符串长度不一样
h1 = hashlib.sha1('12345'.encode())
print(h1.hexdigest(), type(h1))
y = int(str(h1.hexdigest()), 16)
print('y=', y)
h2 = hashlib.sha224('12345'.encode())
print(h2.hexdigest())
h3 = hashlib.sha256('12345'.encode())
print(h3.hexdigest())
h4 = hashlib.sha384('12345'.encode())
print(h4.hexdigest())

# md5加密现在不安全了，更推荐sha224
