# 1. 原始写法---------------------------------------------------------------------------
# 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭他们。
# try:
#     f = open('/path/to/file', 'r')
#     f.read()
# finally:
#     if f:
#         f.close()

# 写try...finally非常繁琐，with语句允许我们非常方便的使用资源，而不必要担心资源没有关闭
# with open('/path/to/file', 'r') as f:
#     f.read()

# 2. 重写方法---------------------------------------------------------------------------
# 并不是只有open()函数返回的fp对象才能使用with语句，实际上，任何对象，只要正确实现了上下文管理，就可以使用with语句
# 思想上下文管理是通过__enter__ 和 __exit__这两个方法实现的

class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s ...' % self.name)


with Query('bob') as q:
    q.query()

# 3. 简化对象---------------------------------------------------------------------------
# 编写—__enter__ 和 __exit__依然很繁琐，因此，Python标准库contextlib提供了更简单的写法
from contextlib import contextmanager


class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query2 info about %s ...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()


# 4. 代码前后执行内容---------------------------------------------------------------------------
# 很多时候，我们希望在某段代码前后都执行特定代码，也可以使用@contextmanager实现
@contextmanager
def tag(name):
    print('<%s>'% name)
    yield
    print('</%s>'% name)

with tag('h1'):
    print('hello world!')
# 代码的执行顺序是：
# 1. with语句首先执行yield之前的语句，因此打印出<h1>；
# 2. yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 3. 最后执行yield之后的语句，打印出</h1>。

# 5. closing---------------------------------------------------------------------------
# 如果一个对象没有实现上下文。我们就不能把它用于with语句，这个时候可以用closing()来把该对象变为上下文对象。
# 例如：用with语句使用urlopen()
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)

# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()
