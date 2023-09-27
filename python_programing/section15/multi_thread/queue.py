import logging
import queue
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(queue):
    logging.debug('start')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug('end')
        queue.task_done()
    # queue.put(100)  # [100, 200]
    # time.sleep(5)
    # queue.put(200)

    logging.debug('longgggggggggggggggggggg')
    logging.debug('end')

# def worker2(queue):
#     logging.debug('start')
#     logging.debug(queue.get())
#     logging.debug(queue.get())
#     logging.debug('end')

if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(10):
        queue.put(i)
    t1 = threading.Thread(target=worker1, args=(queue,))
    # t2 = threading.Thread(target=worker2, args=(queue,))
    t1.start()
    # t2.start()
    logging.debug('tasks are not done')
    queue.join()
    logging.debug('tasks are done')
    queue.put(None)


