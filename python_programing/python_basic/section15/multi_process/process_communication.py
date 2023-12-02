# プロセス間通信に関して
# マルチプロセスの場合は共有メモリーではなく、
# プロセス独自が管理している！

import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(d, lock):
    with lock:
        i = d['x']
        time.sleep(2)
        d['x'] = i + 1
    logging.debug(d)

if __name__ == '__main__':
    d = {'x': 0}

    lock = multiprocessing.Lock()
    t1 = multiprocessing.Process(target=worker1, args=(d, lock))
    t2 = multiprocessing.Process(target=worker2, args=(d, lock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logging.debug(d)

    # Process-1: {'x': 1}
    # Process-2: {'x': 1}
    # MainProcess: {'x': 0}
    