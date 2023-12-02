# ファイル操作とシステム

f = open('test.txt', 'w')
f.write('Test\n')
# printよりもwriteを使う方が分かりやすい
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()

# -------------------------------------------------

# withステートメントでファイルをopenする
# インデントの中の作業が終わったらfを勝手にクローズしてくれる

with open('test.txt', 'w') as f:
    f.write('Test\n')

# -------------------------------------------------

# ファイルの読み込み

s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'w') as f:
    # print(f.read())
    while True:
        line = f.readline()
        # printはデフォルトで改行が入っているのでend=''でなくしている
        print(line, end='')
        if not line:
            break
        
# chunk = 2
# 2文字ずつ読み込む
# ネットワークのプログラミングでパケットを読み込んだりとかにも使う

# -------------------------------------------------

# seekを使って移動する

s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'w') as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
    f.seek()

    # 0
    # A
    # B

# 何文字目から読み出したり、また元に戻って読み直したいって時に使う！

# -------------------------------------------------

# 書き込み読み込みモード

s = """\
AAA
BBB
CCC
DDD
"""

# w+で書き込み＋読み込みという意味
with open('test.txt', 'w+') as f:
    f.write(s)
    # 書き込んだ後は1番最後のインデックスなので
    # seekで元の1番初めの0に戻って出力する
    f.seek(0)
    print(f.read())

# 読み込み書き込みOK
# 初めに読み込めないとエラーになる
with open('test.txt', 'r+') as f:
    f.write(s)

# -------------------------------------------------

# テンプレート

import string

# もし間違った操作があったとしても
# もとの文字のテンプレートが壊されることはない

with open('design/email_template.txt') as f:
    # tはwithの外でも使える
    t = string.Template(f.read())
    # テンプレートとしてtを読み込み専用という形で使うと
    # プログラマーが間違えてtを壊してファイルを保存して
    # テキストを書き換えてしまうということがないので
    # 完全にチーム開発でデザイナー・プログラマーでフィル打ごとに分けるのも🙆‍♀️

contents = t.substitute(name = 'Mike', contents ='How are you?')
print(contents)

# Hi Mike.

# How are you?

# Have a good day

# -------------------------------------------------

# CSVファイルへの書き込みと読み込み

import csv

with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

# Name,Count
# A, 1
# B, 2

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])

# A 1
# B 2

# -------------------------------------------------

# ファイル操作

# ライブラリ
import os
import pathlib
import glob
import shutil

print(os.path.exists('text.txt'))
print(os.path.isfile('text.txt'))
print(os.path.isdir('design'))

os.rename('text.txt'), 'renamed.txt'
os.symlink('renamed.txt', 'symlink.txt')
# synlinkはショートカットコピーみたいなイメージ

# ディレクトリを作成
os.mkdir('test_dir')
# 削除する場合
os.rmdir('test_dir')

# 空のファイルができる
pathlib.Path('empty.txt').touch()
# 削除する場合
os.remove('empty.txt')

os.mkdir('text_dir')
os.mkdir('test_dir/test_dir2')
print(os.listdir('test_dir'))
# ['test_dir2']

# test_dir2の中にさらにファイルを生成
pathlib.Path('test_dir/test_dir2/empty.txt').touch

# *を使うとどんなファイルでもいいので、
# このテスト列に入っている中身のものを全てファイル表示してくださいとなる

# empty.txtがコピーされて、それを両方リストにして表示してくれる
shutil.copy('test_dir/test_dir2/empty.txt',
            'test_dir/test_dir2/empty2.txt')
# ['test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt']

print(glob.glob('test_dir/test_dir2/*'))
# ['test_dir/test_dir2/empty.txt]

# 全てのtest_dirを消す
shutil.rmtree('tesr_dir')
# 間違って他のフォルダーを消さないように要注意！

# 今のディレクトリの位置が知りたい
print(os.getcwd())

# -------------------------------------------------

# tarfileの圧縮展開

import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    # tr.extractall(path='test_tar')
    with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())
        # b 'sub'
    
    # 展開しなくてもそのままtarfileを読み込んで、中身を見ることが可能

# -------------------------------------------------

import glob
import zipfile

# zipfile作成
with zipfile.ZipFile('test.zip', 'w') as z: 
    # これで指定してしまうとフォルダーしか作らない                   
    z.write('test_dir')
    # 自分で指定
    z.write('test_dir/test.txt')

    # test_dirの配下にある全てをrecursiveに見ていく
    # *1つだとtest_dirの同じディレクトリだけ
    # **2つだとどんどん下を見ていってくれる！
    for f in glob.glob('test_dir/**', recursive=True):
        z.write(f)

# zipfile読み込み
with zipfile.zipFile('test.zip', 'r') as z:
    # 中身を全て展開
    # z.extractall('zzz2')
    with z.open('test_dir/test.txt') as f:
        print(f.read())

# -------------------------------------------------

# tempfile

import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# hello
# /var/folders/n1/hqqrllp5515wfx3q6j5_z480000gs/T/tmpa0fe4xjs
# test

# macの場合だとcatというコマンドでパスの中身を確認できる

# ファイルではなくディレクトリでもできる
# 一時的なフォルダーを作って、その中にファイルを作って圧縮したりとかも簡単にできる！
with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)

# 添付ファイルは作ってその後必要なくなったら消すという時にもよく使われる

# -------------------------------------------------

# subprocessでコマンドを実行
# いつもターミナルで行っているコマンドをpython上でやってみる

import subprocess

subprocess.run(['ls', '-al'])
# subprocess.run('ls -al | grep test', shell=True)
# |パイプも使えるが、shell=Trueはセキュリティ的に推奨されていない

# このosシステムもあったが現在あまり推奨されていない、古いコードであるかも
# import os
# os.system('ls)

# r = subprocess.run('lsaaa', shell=True, check=True)
# returncodeを用いてエクセプションを上げたり上げなかったりすることも可能
# print(r.returncode)
# print('###')

# 上級者向けなので理解できなくても大丈夫　Popen
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)

# -------------------------------------------------

# datetime

import datetime

now = datetime.datetime.now()
print(now)
# 国際規格isoフォーマット
print(now.isoformat())
# 表示の変更も可能
print(now.strftime('%d/%m/%y-%H%m%S%f'))

# 2017-11-05 13:45:25.548378
# 2017-11-05T13:45:25.548378
# 05/11/17-134525548378

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

# 2017-11-05
# 2017-11-05
# 05/11/17

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))

# 01:10:05.000100
# 01:10:05.000100
# 01_10_05_000100

# 去年とか来年とか何分前とか何分後とかの時間を扱いたい時
# 演算子でやっていく

print(now)
d = datetime.timedelta(weeks=1)
d = datetime.timedelta(days=365)# 1年前
d = datetime.timedelta(hours=1)
d = datetime.timedelta(minutes=1)
d = datetime.timedelta(second=1)
d = datetime.timedelta(microsecond=1)
print(now - d)

import time
print('###')
# 2秒間何もしないで待ってください
time.sleep(2)
print('###')

# エポックタイム
# 1970年の1月1日から数えた秒数で表現したもの
print(time.time())

# 1509918690.863195

# ファイルのバックアップなんかにも使える！
import os
import shutil

file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')
    ))

with open(file_name, 'w') as f:
    f.write('test')
    