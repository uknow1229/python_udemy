from ftplib import FTP
from logging import getLogger

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

