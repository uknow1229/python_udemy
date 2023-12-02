# Hbase
# ワイドカラム型
# Unix系のシステムにインストールすることを想定されている

# create 'sns', 'blog'
# put 'sns', 'user1', 'blog:bitcoin', 'blog1'
# scan 'sns'
# put 'sns', 'user1', 'blog:soccer', 'blog2'
# put 'sns', 'user2', 'blog:soccer', 'blog4'
# scan 'sns'

# 柔軟に値を入れることができる
# get 'sns', 'user1'

# scan 'sns', {COLUMNS => ['blog:soccer']}

# disableにしてから
# disable 'sns'
# 削除
# drop 'sns'

# pythonのコードでやってみる

# まず外部アクセスからのアクセスを許可するプロセスを立ち上げる
# hbase thrift start

import happybase
# pip install happybase

connection = happybase.Connection('localhost')
connection.open()


connection.create_table(b'sns', {'blog': dict()})

table = connection.table(b'sns')

table.put(
  b'user1', {
    b'blog:bitcoin': b'user1 about bitcoin',
    b'blog:soccer': b'user2 about soccer'
  }
)

# 全ての情報を取り出す
print(list(table.scan()))
print()
# user1の情報だけ取り出す
print(list(table.scan(row_prefix=b'user1')))
print()
# blog:soccerというカラムファミリーがある列の情報だけ取り出す
print(list(table.scan(columns=[b'blog:soccer'])))

# 最後にTableをdisableしてデリートする
connection.disable_table(b'sns')
connection.delete_table(b'sns')

# shellでやったことをpyhonでも実行できる

