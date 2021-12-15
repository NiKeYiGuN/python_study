# type: ignore
import threading
import time
import numpy as np


def task_1(N_max, some_threshold, nx, ny, n):
    print(f"子程_{n}开始执行{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    # A grid of c-values
    xs = np.linspace(-2, 1, nx)
    ys = np.linspace(-1.5, 1.5, ny)
    mandelbrot_set = np.zeros((len(xs), len(ys)))
    for i in range(len(xs)):
        for k in range(len(ys)):
            x = xs[i]
            y = ys[k]
            c = x + 1j * y
            z = c
            is_inside = 1
            for j in range(N_max):
                z = z ** 2 + c
                if abs(z) >= some_threshold:
                    is_inside = 0
                    break
            mandelbrot_set[i, k] = is_inside

    print(f"线程_{n}执行完毕{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    return mandelbrot_set


if __name__ == "__main__":
    # 在 CPython 中，由于存在全局解释器锁，#
    # 同一时刻只有一个线程可以执行Python代码#
    # 虽然某些性能导向的库可能会去除此限制#
    # 对于CPU密集任务多线程并不能提高效率
    # 以下是一个简单的测试案例
    print(f"主线程开始执行{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    t1 = threading.Thread(target=task_1, args=(500, 4, 500, 500, 1))
    t2 = threading.Thread(target=task_1, args=(500, 4, 500, 500, 2))
    t1.start()
    t2.start()

    # API
    count = threading.active_count()
    print(count)

    t1.join()
    t2.join()

    # task_1(500, 4, 500, 500, 1)
    # task_1(500, 4, 500, 500, 1)

    # 使用多线程的执行时间是19s,不使用多线程的执行时间是18秒
    # 由于是伪多线程，增加的一秒时间是CPU时间片的切换造成的
    print(f"主线程执行完毕{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
