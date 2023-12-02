"""
from multiprocessing import(
    Process, RLock, Semphore, Queue, Condition, Event, Barrier,
    Pipe, Value, Array, Manager)
"""

# 違うプロセスの間で共有メモリーに対してプロセスセーフで読み書きをするといったもの
# Value, Array

import logging
import multiprocessing


logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)

def f(num, arr):
    logging.debug(num)
    num.value += 1.0
    logging.debug(arr)
    # 並列化のマルチプロセッシングで共有メモリーで
    # プロセスセーフにするためのオブジェクトで特別なかたち
    for i in range(len(arr)):
        arr[i] *= 2

if __name__ == '__main__':
    num = multiprocessing.Value('f', 0.0)
    arr = multiprocessing.Array('i', [1, 2, 3, 4, 5])

    p1 = multiprocessing.Process(target=f, args=(num, arr))
    p2 = multiprocessing.Process(target=f, args=(num, arr))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    logging.debug(num.value)
    logging.debug(arr[:])
