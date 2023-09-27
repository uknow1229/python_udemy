# pipe

# 1つのプロセスの出力を他のプロセスの入力として扱える

"""
from multiprocessing import(
    Process,
    Lock, RLock, Semphore, Queue, Condition, Event, Barrier,
    Pipe, Value, Array, Manager
)"""
import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)

def f(conn):
    conn.send(['test'])
    time.sleep(5)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn, ))
    p.start()
    logging.debug(child_conn.recv())

# MainProcess: ['test']

# コマンドなんかでもパイプで1つのプロセスが終了したその出力を
# 他のパイプで渡してやったコマンドが使うよといった場合にも使える
