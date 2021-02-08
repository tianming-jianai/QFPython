# 多线程
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
import time, threading


# 新线程执行的代码
def loop():
    print('thread %s is running ...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running ...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 任何进程默认就会启动一个线程，我们把改线程默成为主线程，主线程又可以启动新的线程.

# 2. Lock
# 多进程中，同一个变量，各自有一份拷贝存在于每个进程中
# 多线程中，所有变量都由所有线程共享，所以，任何一个变量，都可以被任何一个线程修改，
# 多个线程同时修改一个变量，可能会把内容改乱了

balance = 0  # 银行存款


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('balance:', balance)
# balance 的值不等于0
# balance = balance + n 分为两步
# 1. 计算balance + n 存入临时变量中
# 2. 将临时变量的值赋给balance
# 究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了

# 解决方案 ： 给change_it加锁

balance = 0
lock = threading.Lock()


def run_thread2(n):
    for i in range(100000):
        # 先要获取锁
        lock.acquire()
        try:
            # 放心的改吧
            change_it(i)
        finally:
            lock.release()


t3 = threading.Thread(target=run_thread2, args=(5,))
t4 = threading.Thread(target=run_thread2, args=(8,))
t3.start()
t4.start()
t3.join()
t4.join()
print('balance2:', balance)

# 3. 多核CPU
import threading, multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1


print('cpu核心数：', multiprocessing.cpu_count())
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
# 启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：GlobalInterpreter Lock，任何Python线程执
# 行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全
# 局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，

# 在Python中，可以使用多线程，但不要指望能有效利用多核。

# Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程
# 有各自独立的GIL锁，互不影响。
