"""
[DEFAULT]
debug = False

[web_server]
host = 127.0.0.1
post = 80

[db_server]
host = 127.0.0.1
port = 3306
"""
# configファイルの読み書きをするconfigparser
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
  'debug': True
}
config['web_server'] = {
  'host': '127.0.0.1',
  'port': 80
}
config['db_server'] = {
  'host': '127.0.0.1',
  'port': 3306
}
with open('config.ini', 'w') as config_file:
    config.write(config_file)

# 実行するとconfig.iniができてconfigが書き込まれる

# 読み込むとき
config = configparser.ConfigParser()
config.read('config.ini')
print(config['web_server'])
print(config['web_server']['host'])
print(config['web_server']['port'])
# <Section: web_server>
# 127.0.0.1
# 80

print(config['DEFAULT']['debug'])
# True
