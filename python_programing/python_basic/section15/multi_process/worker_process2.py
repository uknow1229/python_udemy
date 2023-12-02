# ワーカープロセスのプールでブロック

# 並列化しないでブロックするやり方
# p.apply

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
        p.apply(worker1, (200))
        logging.debug(p.apply_async(worker1, (200, )))
        # p.apply 何かブロックさせたい、処理を1番最初にさせたいなどのときに使う
        logging.debug('executed apply')
        p1 = p.apply_async(worker1, (100, ))
        p2 = p.apply_async(worker1, (100, ))
        logging.debug('executed')
        logging.debug(p1.get())
        logging.debug(p2.get())



