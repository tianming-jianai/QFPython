import time


def cal_time(fn):
    def inner(n):
        start = time.time()
        x = fn(n)
        end = time.time()
        return x, end - start

    return inner


@cal_time  # 第一件事调用cal_time 第二件事把被装饰的函数传递给fn
def demo(n):
    x = 0
    for i in range(1, n):
        x += 1
    return x


# 第三件事：当再次调用demo时，此时demo函数已经不再是上面的demo，而是inner函数
print('装饰后的demo = {}'.format(demo))  # <function cal_time.<locals>.inner at 0x000001AB2259B310>


# y = demo(100000000)
# print(y)

# -----------------------------------------------------

def can_play(fn):
    def inner(x, y, *args, **kw):
        if args[0] < 22:
            fn(x, y)
        else:
            print('太晚了 {} 赶紧睡觉'.format(x))

    return inner


@can_play
def playgame(name, game):
    print('{} 正在玩 {}'.format(name, game))


playgame('张三', '绝地求生', 18)
playgame('李四', '王者荣耀', 23)
