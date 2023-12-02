# SQLite
# 非常に軽量

import sqlite3


# conn = sqlite3.connect('test_sqlite.db')
# メモリー上にデータベースを作ってくれるので練習用におすすめ！
conn = sqlite3.connect(':memory:')

curs = conn.cursor()

curs.execute(
  'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
conn.commit()

curs.execute(
  'INSERT INTO persons(name) values("Mike")'
)
conn.commit()

curs.execute(
  'INSERT INTO persons(name) values("Nancy)')
curs.execute(
  'INSERT INTO persons(name) values("Jun")')
conn.commit()

curs.execute('UPDATE persons set name = "Michel WHERE name = "Mike"')
conn.commit()

curs.execute('DELETE FROM persons WHERE name = "Michel"')
conn.commit()

curs.execute('SELECT * FROM persons')
print(curs.fetchall())

conn.close()
conn.close()
