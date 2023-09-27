import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(d, lock):
    logging.debug('start')
    # このような書き方でもOK
    with lock:
        i = d['x']
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            d['x'] = i + 1
    logging.debug('end')

def worker2(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')

if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.RLock()
    t1 = threading.Thread(target=worker1, args=(d, ))
    t2 = threading.Thread(target=worker2, args=(d, ))
    t1.start()
    t2.start()


    # タイマー
    # t = threading.Timer(3, worker1, args=(100,), kwargs={'y': 200})
    # t.start()


# 生存中のThreadオブジェクト全てのリスト
    # # threads = []
    # for _ in range(5):
    #     t = threading.Thread(target=worker1)
    #     t.setDaemon(True)
    #     t.start()
    #     # threads.append(t)
    # print(threading.enumerate())
    # for thread in threading.enumerate():
    #     if thread is threading.currentThread():
    #         print(thread)
    #         continue
    #     thread.join()


    # t1 = threading.Thread(target=worker1)
    # t1.setDaemon(True)
    # t2 = threading.Thread(target=worker2)
    # t1.start()
    # t2.start()
    # print('started')
    # t1.join()
    # t2.join()
