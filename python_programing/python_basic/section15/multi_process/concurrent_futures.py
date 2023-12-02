import threading
import multiprocessing

# concurrent_futuresは高水準のインターフェースで簡単に並列が書ける
# 単純な並列をして結果を返してもらいたい時はthreadingやmultiprocessingよりも
# concurrent_futuresで簡単に実装できる！

import concurrent_futures
import logging
import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s'
# )
logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)

def worker(x, y):
    logging.debug('start')
    time.sleep(3)
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r

def main():
    # threadで並列化し、並列化させたスレッドに何かやらせて、
    # その結果を返してもらうような場合にはThreadPoolExecutorを使えば簡単にできる！
    with concurrent_futures.ThreadPoolExecutor(max_workers=1) as executor:
        # max_workerでスレッドが走る数も簡単にコントロールできる
        # f1 = executor.submit(worker, 2, 5)
        # f2 = executor.submit(worker, 2, 5)
        # logging.debug(f1.result())
        # logging.debug(f2.result())

        args = [[2, 2], [5, 5]]
        r = executor.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])
        # 結果を見るには、リスト内をループして取り出していけば結果が見れる！

if __name__ == '__main__':
    main()

