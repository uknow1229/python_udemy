# importの書き方
# import lesson_package.utils
# r = lesson_package.utils.say_twice('hello')

# 違う書き方
# from lesson_package.utils import say_twice
# r = say_twice('hello')

# fromの書き方
# from lesson_package import utils
# from lesson_package.talk import human
# from lesson_package.talk import animal

# *で読まれることを想定してどのモジュールを返したいか定義できるが
# どんなモジュールが読み込まれるか分かっていない状況で、使うケースが多いので
# あまり推奨されていない
# from lesson_package.talk import *

# print(animal.sing())
# print(animal.cry())

# r = utils.say_twice('hello')
# print(r)

# print(human.sing())
# print(human.cry())

# ImportErrorの使い所
# lesson.pyが古いパッケージでも新しいパッケージでも
# どちらでもいいようにするような時に使える
# try:
#     from lesson_package import utils
# except ImportError:
#     from lesson_package.tools import utils

# utils.say_twice('word')

# 組み込み関数
import builtins

builtins.print()

ranking = {
  'A': 100,
  'B': 85,
  'C': 95
}

for key in ranking:
    print(key)
# A
# B
# C

# キーの順番
print(sorted(ranking))
# ['A', 'B', 'C']

# 中身でsort
# ランキングのgetをキーにする
print(sorted(ranking, key=ranking.get, reverse=True))


# ビルドイン関数以外にもたくさんの便利なライブラリが用意されている！
#

s = "nvhalgblvhsbfjabvhjabsdk"

d = {}
for c in s:
    # fというキーがdictionaryに入っていなければ
    if c not in d:
        # デフォルトのcのキーには0を入れておく
        d[c] = 0
    d[c] += 1
print(d)


d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)


from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

# fが何個？
print(d['f'])

# ---------------------------------

# importする際の記述の仕方

# このように書くのではなく
import collections, sys, os
# 1行ずつ書いていくのが良い(アルファベット順だと読みやすい)
import collections
import os
import sys

# 標準ライブラリとサードパーティーのライブラリを
# インポートする間にスペースを開けるのが良い
import termcolor

import lesson_package

import config

# 1番上はpythonの標準ライブラリ
# 次はサードパーティーのアプリ
# 自分達のパッケージ
# 最後はローカルのファイル
# といった順番で書くとどこから取ってきたパッケージか分かりやすい！

# printでcollectionsのファイルがどこにあるかプリントできる
print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)
# sysパスが書いていない場所にパッケージを置いたとしても
# pythonは読み込まないので注意！

# ローカルのパッケージが1番初めに優先されるので
# 例えば標準ライブラリやサードパーティと同じような
# ライブラリをローカルに作ってしまうと、それが先に読み込まれるのでその点も注意！

# ---------------------------------

# __name__と＿_main__

import lesson_package.talk.animal
# animal.pyのprint(sing())もimportされた時点で実行されてしまう
import config


def main():
    # 生で書いておくとimportされたときに実行されてしまうので
    # 実行されないようにこのように書く
    lesson_package.talk.animal.sing()

# どんなスクリプトでも下記の記述があってmainというfunctionがあって実行する
if __name__ == '__main__':
    main()

