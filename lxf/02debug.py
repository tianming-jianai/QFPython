# 程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。有的bug很简单，看看错误
# 信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一
# 整套调试程序的手段来修复bug。

# 1. print()  用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。

# 2. 断言 assert
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert
# 关闭后，你可以把所有的assert语句当成pass来看。
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'  # AssertionError: n is zero
    return 10 / n


def main():
    foo('0')


main()

# 3. logging  logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
# import logging
#
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)  # INFO:root:n = 0
# print(10 / n)

# 4. pdb 启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行
import pdb

s = '0'
n = int(s)
pdb.set_trace()  # 执行到这里就会停止
print(10 / n)

# 5. ide

# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器
