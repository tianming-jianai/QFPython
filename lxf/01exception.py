# 1. 解决错误  try except finally
try:
    print('try ...')
    r = 10 / 0
    print('result :', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally ...')
print('end')
# try ...
# except: division by zero
# finally ...
# end
print()

try:
    print('try ...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error')  # expect 后增加 else ,当没有错误语句时，自动执行
finally:
    print('finally ...')
print('end')

print()


# Python的错误其实也是class，所有的错误类型都继承自BaseException
# 应该先捕获子类，再捕获父类，否则子类始终捕获不到

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    print('main ...')
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally ...')


main()
print()
# 2. 记录错误
# Python内置的logging模块可以非常容易地记录错误信息
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
import logging


def foo2(s):
    return 10 / int(s)


def bar(s):
    return foo2(s) * 2


def main2():
    print('main2 ...')
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main2()
print('end2 ...')

print()


# 抛出错误
# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比
# 如ValueError，TypeError），尽量使用Python内置的错误类型。

# class FooError(ValueError):
#     pass
#
#
# def foo3(s):
#     print('foo3 ...')
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value : %s' % s)
#     return 10 / n
#
#
# foo3('0')


# 打印一个ValueError!后，又把错误通过raise语句抛出去了
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数
# 不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个
# 问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
# raise语句如果不带参数，就会把当前错误原样抛出

# def foo4(s):
#     print('foo4 ...')
#     n = int(s)
#     if n == 0:
#         raise ValueError('invalied value:%s' % s)
#     return 10 / n
#
#
# def bar2():
#     print('bar2 ...')
#     try:
#         foo4('0')
#     except ValueError as e:
#         print('ValueError')
#         raise
#
#
# bar2()
# print('bar2 end ...')

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转
# 化成另一种类型,只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error')

