import threading
from threading import Lock, RLock
from util.time_util import format_time

"""
    多线程共享全局变量
    线程时进程的执行单元，进程时系统分配资源的最小执行单位，所以在同一个进程中的多线程是共享资源的
"""

"""
        由于线程之间是进行随机调度，并且每个线程可能只执行n条执行之后，当多个线程同时修改同一条数据时可能会出现脏数据，
    所以出现了线程锁，即同一时刻允许一个线程执行操作。线程锁用于锁定资源，可以定义多个锁，像下面的代码，当需要独占
    某一个资源时，任何一个锁都可以锁定这个资源，就好比你用不同的锁都可以把这个相同的门锁住一样。
        由于线程之间是进行随机调度的，如果有多个线程同时操作一个对象，如果没有很好地保护该对象，会造成程序结果的不可预期，
    我们因此也称为“线程不安全”。
        为了防止上面情况的发生，就出现了互斥锁（Lock）
"""

global_num = 100


def work1():
    global global_num
    for i in range(3):  # type: ignore
        global_num += 1
        print(f"In work1 global_num is {global_num}")


def work2():
    global global_num
    print(f"In word2 global_num is {global_num}")


lock = Lock()
n = 0


def lock_work():
    global n
    with lock:
        n += 1
    print(n)


"""
    关于Lock和RLock的区别
"""
r_lock = RLock()


def factorial(n: int) -> int:
    assert n > 0
    if n == 1:
        return 1
    with r_lock:
        out = n * factorial(n - 1)

    return out


if __name__ == "__main__":
    # t1 = threading.Thread(target=work1)
    # t1.start()
    # time.sleep(1)
    # t2 = threading.Thread(target=work2)
    # t2.start()

    for i in range(100):
        p = threading.Thread(target=lock_work)
        p.start()
        print(f"子线程_{i}开始执行{format_time()}")

    print(factorial(3))
