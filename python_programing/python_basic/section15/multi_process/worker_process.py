# ワーカープロセスのプールで非同期

# ワーカーの数をプロセスで走らせる時に数を決められる

from multiprocessing import (
    process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager
)

import logging
import multiprocessing
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    return i

if __name__ == '__main__':
    # t1 = multiprocessing.Process(target=worker1, args=(i, ))
    with multiprocessing.Pool(3) as p:
        p1 = p.apply_async(worker1, (100, ))
        p2 = p.apply_async(worker1, (100, ))
        logging.debug('executed')
        logging.debug(p1.get(timeout=1))
        logging.debug(p2.get())



