"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging
from logging import LogRecord


logging.basicConfig(level=logging.INFO)


logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

# CRITICAL:root:critical
# ERROR:root:error
# WARNING:root:warning
# INFO:root:info

logging.info('info {}'.format('test'))
logging.info('info %s %s' % ('test', 'test2'))
logging.info('info %s %s', 'test', 'test2')
# INFO:root:info test test2

# 書き込んだログ情報をファイルに書き込みたい場合

logging.basicConfig(filename='test.log', level=logging.INFO)

# 実行するとtest.logができて情報が入る！

# -----------------------------

# ロギング フォーマッター
# ロギングのメッセージをカスタマイズできる！

import logging

# formatter = '%(levelname)s:%(message)s'
formatter = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

logging.info('info %s %s', 'test', 'test2')

# 2017-11-10 08:20:12,809:info test test2

# -----------------------------

# ロギング ロガー

# main関数のところでlogging設定してその後は全て
# loggerを使ってやっていくのが1番良いやり方


import logging

# import logtest


logging.basicConfig(level=logging.INFO)

logging.info('info')

logger = logging.getLogger(__name__)
logging.setLevel(logging.DEBUG)
logger.debug('debug')

# INFO:root:info
# DEBUG:__main__:debug

# -----------------------------

# logtest.py

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def do_something():
    logging.info('from logtest info')
    logger.info('from logtest')
    logger.debug('from logtest debug')

# -----------------------------

# ロギング ロガー

# logtestを他のログファイルに書き込みたい場合

# logtest.py
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('logtest.log')
logger.addHandler()
# 実行するとlogtest.logができる
# 中身を見ると
# from logtest
# from logtest debug
# ファイルに書き込まれるのはloggerを使った2つだけ

def do_something():
    logging.info('from logtest info')
    logger.info('from logtest')
    logger.debug('from logtest debug')

# -----------------------------

# ロギング フィルター

import logging

logging.basicConfig(level=logging.INFO)


# 間違えて記載してしまったなど、パスワードなどのキーワードがある場合
# ログに書き込みません、ログに出力しませんという風にする！
# 自分のクラスを作る！
class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        # パスワードというものが入っていなければログメッセージは出力します
        return 'password' not in log_message

logger = logging.getLogger(__name__)
# NoPassFilterをloggerに付け加える(オブジェクトにして渡す)
logger.addFilter(NoPassFilter())
logger.info('from main')
logger.info('from main password = "test"')

# INFO:__main__:from main

# フィルターを使ってロギングのフィルターをコントロールしていくことも
# カスタマイズできる

# -----------------------------

# ロギング コンフィグ

import logging.config


# logging.config.fileConfig('logging.ini')

# dictionary型の設定の仕方もできる
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'sampleFormatter': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
        'handlers': {
            'sampleHandlers': {
                'class': 'logging.StreamHandler',
                'formatter': 'sampleFormatter',
                'level': logging.DEBUG
            }
        },
        'loggers': {
            'simpleExample': {
                'handlers': ['sampleHandlers'],
                'level': logging.DEBUG,
                'propagate': 0
            }
        }
    }
})

logger = logging.getLogger(__name__)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

# -----------------------------

# ロギングの書き方

import logging


logger = logging.getLogger(__name__)


logger.error('Api call is failed')

# key valueで書いてもOK
logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed'
})
# ログ解析のソフトウェアでKeyValueを掛けてどんなログがあるのか分析する
# ログファイルに書き込んで、ログファイルをログ解析ソフトに送る

# システムにおいて非常に大事なところでトラブルが起きたら困る場所には
# なるべく多くのロギングを書いておく！

# -----------------------------

# Email送信(hotmailの場合)

from email import message
import smtplib


smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'xxxx@hotemail.com'
to_email = 'xxxx@hotemail.com'
username = 'xxxx@hotemail.com'
password = 'hgjkarshbgjst'

msg = message.EmailMessage
# mailの中身
msg.set_content('Test email')
# mailのタイトル
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()

# -----------------------------

# 添付ファイルEmail送信

from email import message
from email.mime import multipart
from email.mime import text
import smtplib


smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'xxxx@hotemail.com'
to_email = 'xxxx@hotemail.com'
username = 'xxxx@hotemail.com'
password = 'hgjkarshbgjst'

# MIMEはメールを送る時の規格
# msg = message.EmailMessage
msg = multipart.MIMEMultipart()
# msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('Test email', 'plain'))

with open('lesson.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='lesson.txt'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()


# -----------------------------

# SMTPハンドラーでログをEmail送信

import logging
import logging.handlers

smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'xxxx@hotemail.com'
to_email = 'xxxx@hotemail.com'
username = 'xxxx@hotemail.com'
password = 'hgjkarshbgjst'

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log', 
    credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))

logger.info('test')
logger.critical('critical')

# ログでメールを投げるといっても間違ってプログラムが
# 何度も何度もログを呼び出してしまってメールを大量に送ってしまうこともあり得る
# 今はSMTPハンドラーを使うよりもログをログ解析ソフトに送り、
# ログ解析ソフトがログの情報を集め、毎回メールを送るのではなく、
# 一度にまとめて一回だけメールを送ることもできる！

# -----------------------------

# virtualenv

# pythonをインストールして複数のバージョンを使いたい時
# python環境を独立した環境を使って切り替えることができる！

# pip install virtualenv

# 独自のvirtualenvを作って色んなパッケージをインストールしたり
# リームーブしたりでき、それを使ってプログラムを走らせることができる

# -----------------------------

# optparse

from optparse import OptionParser
from optparse import OptionGroup


def main():
    
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='File name')
    parser.add_option('-n', '--num', action='store', type='init', dest='num')
    # parser.add_option('-v', action='store_true', dest='verbose')
    parser.add_option('-v', action='store_false', dest='verbose', default=True)

    parser.add_option('-r', action='store_const', const='root', dest='user_name')

    parser.add_option('-e', dest='env')

    def is_relase(option, opt_str, value, parser):
        if parser.values.env == 'prd':
            raise parser.error("Can't relase")
        setattr(parser.values, option.dest, True)
        
    parser.add_option('--release', action='callback', callback=is_relase, dest='release')

    group = OptionGroup(parser, 'Dangerous options')
    group.add_option('-g', action='store_true', help='Group option')
    parser.add_option_group(group)
    
    options, args = parser.parse_args()
    print(type(options.filename))
    print(type(args))


if __name__ == '__main__':
    main()






