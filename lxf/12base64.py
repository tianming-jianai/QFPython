# ------------------------
# Base64 是一种用64个字符来表示任意二进制数据的方法
# Python内置的base64可以直接进行Base64的编解码
import base64

a = base64.b64encode(b'binary\x00string')
print(a)
b = base64.b64decode(a)
print(b)

# ------------------------
# 由于标准的Base64编码后可能出现字符+和-,在URL中就不能直接作为参数,
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
c = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(c)
d = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(d)
e = base64.urlsafe_b64decode(d)
print(e)


# ------------------------
# 还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，不过，通常情况下没有必要


# ------------------------
# Base64是一种通过查表的编码方法，不能用于加密，即时使用自定义的编码表也不行
# Base64适用小段内容的编码。比如数字签名证书。Cookie的内容等。
# 由于=字符也可能出现在Base64编码中。但=用在URL、Cookie里面会造成歧义，所以很多Base64编码后会把=去掉

# ------------------------
# 标准Base64
# 'abcd' --> 'YWJjZA=='
# 自动去掉=
# 'abcd' --> 'YWJjZA'
# 去掉=后怎么解码呢？因为Base64是把3个字节变成4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变成4的倍数，可以正常解码了。
# ------------------------

# Base64是一种任意二进制到文本字符串的编码方法，常用语URL、Cookie、网页中传输少量二进制数据
# ------------------------
def safe_base64_decode(s):
    # 添加等于号
    if len(s) % 4 != 0:
        s = s + bytes('=', encoding='utf8') * (4 - len(s) % 4)
        print('s:%s' % s)
    # 解决字符串的bytes类型
    if not isinstance(s, bytes):
        s = bytes(s, encoding='utf8')
        print('s:%s' % s)
    # 解码
    base64_string = base64.b64decode(s)
    print('base64:%s' % base64_string)
    return base64_string


assert b'abcd' == safe_base64_decode(b'YWJjZA=='),safe_base64_decode('YWJjZA==')
print('--------')
assert b'abcd' == safe_base64_decode(b'YWJjZA'),safe_base64_decode('YWJjZA')
print('ok')