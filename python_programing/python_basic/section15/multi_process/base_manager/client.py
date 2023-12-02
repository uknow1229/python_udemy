from multiprocessing.managers import BaseManager


class QueueManeger(BaseManager):
    pass

QueueManeger.register('get_queue')

manager = QueueManeger(
    address=('127.0.0.1', 50000),
    authkey=b'abracadabra'
)
manager.connect()
queue = manager.get_queue()
queue.put('hello')
