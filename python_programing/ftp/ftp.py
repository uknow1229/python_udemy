from ftplib import FTP
from logging import getLogger
import os


from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpblib.servers import FTPServer


def setup_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("username", "password", "/path/to/your/directory", perm="elradfm")

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.directory = "/path/to/your/directory"

    server = FTPServer(("127.0.0.1", 21), handler)
    server.serve_forever()

if __name__ == "__main__":
    setup_ftp_server()

# ログ出力設定
logger = getLogger("FTP Test")


HOST = 'XXX.com'
PORT = 21
USER = 'userName'
PASSWORD = 'password'
DIRECTORY = 'test'

# アップロードファイル名
FILE_NAME = 'test.jpg'

# FTP接続、ファイルアップロード
logger.debug("== Start FTP ==")
with FTP() as ftp:
    try:
        ftp.connect(HOST, PORT)
        ftp.login(USER, PASSWORD)
        ftp.cwd(DIRECTORY)
        with open(FILE_NAME, 'rb') as f:
            ftp.storbinary('STOR' + FILE_NAME, f)
    except FTP.all_errors as e:
          logger.error('FTP error = %s' % e)
    else:
          logger.debug('FTP success.')
logger.debug('== End FTP ==')

