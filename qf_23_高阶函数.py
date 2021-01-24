# 高阶函数的三种表现形式
# 1.一个函数作为另一个函数的返回值
# 2.一个函数作为另一个函数的参数
# lambda 表达式的使用
# 3.函数内部再定义一个函数

def foo():
    print('我是foo，我被调用了')
    return 'foo'


def bar():
    print('我是bar，我被调用了')
    return foo()


a = bar()
print(a)  # foo


def bar2():
    print('我是bar，我被调用了')
    return foo


print()
b = bar2()
print(b)  # <function foo at 0x000001A8468DB1F0>
# 返回的是foo函数，并没有被调用
print()
b()  # foo函数才被调用

# 也可以这样写
print()
c = bar2()()
print(c)

print()


# ---------------------------------------------------------------------------------------------------

def outer():
    def inner():
        print('我是inner函数')

    print('我是outer函数')
    return inner


outer()()
