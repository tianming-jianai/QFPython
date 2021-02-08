import threading


# 在多线程环境下，每个线程都有自己的数据。
# 。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦
class Student(object):
    def __init__(self, name):
        self.name = name


def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都需要它，因此必须传进去
    do_task1(std)
    do_task2(std)


def do_task1(std):
    # do_subtask(std)
    # do_subtask2(std)
    pass


def do_task2(std):
    # do_subtask(std)
    # do_subtask2(std)
    pass


# 套娃传参那还了得？？？


# 如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？
global_dict = {}


def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中
    global global_dict
    [threading.current_thread().name] = std
    do_task_1()
    do_task_2()


def do_task_1():
    # 不传入std,而是根据当前线程查找：
    std = global_dict[threading.current_thread().name]


def do_task_2():
    # 不传入std,而是根据当前线程查找：
    std = global_dict[threading.current_thread().name]


# 这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑。

# 1. ThreadLocal
# 创建全局的ThreadLocal对象
import threading

local_school = threading.local()


def process_student():
    # 获取当前线程相关联的student
    std = local_school.student
    print('hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以
# 把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干
# 扰，也不用管理锁的问题，ThreadLocal内部会处理。

# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有
# 调用到的处理函数都可以非常方便地访问这些资源。


# 多线程模式通常比多进程快一点，但是也快不到哪去，

# 在Windows下，多线程的效率比多进程要高,IIS的稳定性就不如Apache。为了环节这个问题，IIS和Apache现在又有多进程+多线程的混合模式


# 2. 线程切换

# 计算密集型 vs IO密集型
# 是否采用多任务的第二个考虑是任务的类型

# 所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数
# 。常见的大部分任务都是IO密集型任务，比如Web应用 对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。


# 3. 异步IO
# 现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支
# 持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务
# 器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心
# 数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来
# 实现多任务是一个主要的趋势。

# 对应到Python语言，单线程的异步编程模型称为协程
