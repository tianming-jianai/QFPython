# 加盐实际上是Hmac算法：Keyed-Hashing for Message Authentication 它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。

# 和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，更安全。
# Python自带的hmac模块实现了标准的Hmac算法.

# 使用hmac实现带key的哈希
# 我们首先要准备待计算的原始消息message,随机key,哈希算法,
import hmac

message = b'hello world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
# 可见，使用hmac和普通hash算法非常详细，hmac输出的长度和原始哈希算法的长度一致，需要注意，传入的key和message都是bytes类型，
# str类型需要首先编码为bytes


# ------------------------
# 将上一节的salt改为标准的hmac算法，验证用户口令：
import hmac, random


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


print(login('michael', '123456'))  # True
print(login('bob', 'abc999'))  # True
print(login('alice', 'alice2008'))  # True

# Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，使用hmac算法比标准
# hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。
