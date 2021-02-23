# 摘要算法简介
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换承诺一个长度固定的数据串(通常用16进制的字符串表示)
# 摘要函数就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest,目的是为了发现原始数据是否被人篡改

# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但是通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同

# ------------------------
# md5 128位字节 32位16进制字符串  速度快
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())  # d26a53750bc40b38b65a520292f69306

# 如果数据量很大，可以分块多次调用update(),最后计算的结果是一样的：
md5_2 = hashlib.md5()
md5_2.update('how to use md5 in python'.encode('utf-8'))
md5_2.update(' hashlib?'.encode('utf-8'))
print(md5_2.hexdigest())  # d26a53750bc40b38b65a520292f69306

# ------------------------
# sha1 160bit字节 40位的16进制字符串
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())  # b752d34ce353e2916e943dc92501021c8f6bca8c


# 比sha1更安全的算发是sha256,sha512,不过越安全的算法不仅越慢，而且摘要长度更长。


# ------------------------
# 有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？完全有可能，因为任何摘要算法都是把无限多的数
# 据集合映射到一个有限的集合中。这种情况称为碰撞，比如Bob试图根据你的摘要反推出一篇文章'how to learn
# hashlib in python - by Bob'，并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非
# 常非常困难。


# ------------------------
# 摘要算法应用
# 存储用户名和口令
# 如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数
# 据库的，也就是能获取到所有用户的口令。
# 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
# 当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正
# 确，如果不一致，口令肯定错误。


# ------------------------
# 练习
# 存储md5的好处是，即使运维人员能访问数据库，也无法获知用户的明文口令
# 设计一个用户登录的函数，根据用户输入的口令是否正确，返回True or False
def calc_md5(password):
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


db = {
    'michael': '3704e81a667432bebb436054e64db0e8',  # 123456
    'bob': '1d0f6f75634b620dd27e280e67bcf211',  # abc999
    'alice': '0e89cdfc3512f8cae960a8876a4f629f'  # alice2008
}


def login(user, password):
    print('user:', user, ',password:', password)
    if calc_md5(password) == db.get(user):
        return True
    else:
        return False


print(login('michael', '123456'))
print(login('bob', 'abc999'))
print(login('alice', 'alice2008'))

# ------------------------
# 采用MD5存储口令是否就一定安全呢？也不一定。假设你是一个黑客，已经拿到了存储MD5口令的数据库，如何通过
# MD5反推用户的明文口令呢？暴力破解费事费力，真正的黑客不会这么干。
# 考虑这么个情况，很多用户喜欢用123456，888888，password这些简单的口令，于是，黑客可以事先计算出这些常用
# 口令的MD5值，得到一个反推表
# 'e10adc3949ba59abbe56e057f20f883e': '123456'
# '21218cca77804d2ba1922c33e0151105': '888888'
# '5f4dcc3b5aa765d61d8327deb882cf99': 'password'
# 这样，无需破解，只需要对比数据库的MD5，黑客就获得了使用常用口令的用户账号。
# 对于用户来讲，当然不要使用过于简单的口令。但是，我们能否在程序设计上对简单口令加强保护呢？


# 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的
# MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：


# ------------------------
# 练习
# 根据修改后的md5算法实现用户登录的验证
import hashlib, random


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

print('---------')


def login2(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)


print(login2('michael', '123456'))  # True
print(login2('bob', 'abc999'))  # True
print(login2('alice', 'alice2008'))  # True

# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明
# 文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
