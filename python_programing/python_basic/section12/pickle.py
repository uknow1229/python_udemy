# pickle
# DBとは少し違うがPythonのデータをそのままの形で保存する

import pickle

class T(object):

    def __init__(self, name):
        self.name = name

data = {
  'a': [1, 2, 3],
  'b': {'test', 'test'},
  'c': {'key': 'value'},
  'd': T('test')
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(type(data_loaded['a']))
    print(type(data_loaded['b']))
    print(type(data_loaded['c']))
    print(type(data_loaded['d']))

# 保存する時も、ロードする時もPythonのオブジェクトのまま
# 簡単にデータを保存したり、読み込んだりすることができる
# pickleの特徴！

# が、DBの方が他の言語や他の開発への互換性がある
# pickleの場合、他のシステムに移行した時にそのデータが使えなくなる

