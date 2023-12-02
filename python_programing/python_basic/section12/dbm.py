# DBM
# 簡易的なものを素早く書き出したい・取り出したいって時
# キャッシュなどの簡易的なもの

import dbm


with dbm.open('cache', 'c') as db:
    db['key1'] = 'value1'
    db['key2'] = 'value2'
    # integerは書き込めない
    # db['key3'] = 1

with dbm.open('cache', 'r') as db:
    print(db.get('key1'))

