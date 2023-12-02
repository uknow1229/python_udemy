# barrier
# 必ずサーバーとクライアントのスレッドが両方立ち上がってないと
# サービスを始めてはいけませんって時に使う！

import logging
import queue
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(barrier):
    r = barrier.wait()
    logging.debug('num={}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

def worker2(barrier):
    r = barrier.wait()
    logging.debug('num={}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

if __name__ == '__main__':
    barrier = threading.Barrier(2)
    # スレッドが2個立ち上がるまで次に進まない
    t1 = threading.Thread(target=worker1, args=(barrier,))
    t2 = threading.Thread(target=worker2, args=(barrier,))
    t1.start()
    t2.start()




