# ワーカープロセスのプールとマップ

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
        # map
        r = p.map_async(worker1, [100, 100])
        # mapを使えば何行も書いたり、自分でループ回したりしなくていいので楽！
        logging.debug('executed')
        logging.debug(r.get(timeout=1))

        # imap
        r = p.imap(worker1, [100, 200])
        logging.debug('executed')
        logging.debug([i for i in r])

        # p1 = p.apply_async(worker1, (100, ))
        # p2 = p.apply_async(worker1, (100, ))
        # logging.debug('executed')
        # logging.debug(p1.get())
        # logging.debug(p2.get())



