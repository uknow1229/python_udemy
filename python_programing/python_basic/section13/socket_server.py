# socket通信

"""
ウェルノウンポート番号 (0-1023)
登録済みポート番号 (1024-49151)
動的・プライベート ポート番号 (49152-65535)
"""

import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 50007))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            if not data:
                break
            print('data: {}, addr: {}'.format(data, addr))
            conn.sendall(b'Received' + data)

# udp
# udpはクライアントが投げたらそれを受け取ったことを確かないということで簡単！

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data, addr = s.recvfrom(1024)
        print("data: {}, addr: {}".format(data, addr))