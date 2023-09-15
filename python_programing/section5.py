# 制御フローとコード構造

# 複数行コメントを書きたいとき
"""
test
test
test
test
"""

# pythonの場合コメントは横ではなく上に書くべき(暗黙のルール)

# Apple price
some_value = 100

# 1行が長くなるとき
s = 'aaaaaaaaaaaaa' + 'bbbbbbbbbbbbbbb'

# バックスラッシュをつけて改行しないと+が何かわからなくなる！
s = 'aaaaaaaaaaaaa' \
+ 'bbbbbbbbbbbbbbb'

print(s)
# aaaaaaaaaaaaabbbbbbbbbbbbbbb

# バックスラッシュが嫌な場合は、()でもOK
x = (1 + 1 + 1 + 1 + 1 + 1 + 1 
    + 1 + 1 + 1 + 1 + 1 + 1 + 1)
print(x)
# 14

# ルール的に80文字で次の行に行くと決まっている

# ------------------------------------------------

# if文

# pythonでは4つスペースを空けるのが好まれているらしい

x = -10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

# もう1個のケース
a = 5
b = 10

# 他の言語とは違い、Pythonはインデントを綺麗に合わせないとエラーになるので注意！
if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

# ------------------------------------------------

# 比較演算子と論理演算子
a = 2
b = 2

# aもbも真であれば真

if a > 0 and b > 0:
    print('a and b are positive')
# a and b are positive

# and使わないと読みにくい
if a > 0:
    if b > 0:
        print('a and b are positive')
# a and b are positive

# aまたはbが真であれば真
a = -1
b = 1

if a > 0 or b > 0:
    print('a or b are positive')
# a or b are positive

# orを使わないと、同じコードが繰り返されていてよくない
if a > 0:
    print('a or b is positive')
elif b > 0:
    print('a or b is positive')

# ------------------------------------------------

# InとNotの使い所
y = [1, 2, 3]
x = 1

if x in y:
    print('in')
# in

if 100 not in y:
    print('not in')
# not in

# 数字の違いを見る時は、こういった書き方はあまり好まれない、わかりにくい
a = 1
b = 2

if not a == b:
    print('Not equal')
# Not equal

# 値同士が違うというのはこちらの方が分かりやすい
if not a != b:
    print('Not equal')

# じゃあどういう時に使うの？？
# boolean型を否定するとき

is_ok = True

if not is_ok:
    print('hello')

# ------------------------------------------------

# 値が入っていない判定をするテクニック

is_ok = True

if is_ok:
    print('OK!')
# OK!
else:
    print('NO!')

# is_okがtrueになる他の構造体や変数がある
# TRUE 1
# FALSE, 0, 0.0, '', [], (), {}, set()

# ------------------------------------------------

# Noneを判定する場合

# pythonでは何も値が入っていないことをNonと表現する

is_empty = None
print(is_empty)
# None

# pythonでは==でNone判定するのは勧められてない
if is_empty == None:
    print('None!!!')

# isを使う!!
if is_empty is not None:
    print('None!!!')

# 値を1として真同士
print(1 == True)
# True

# オブジェクト同士が同じものである
print(1 is True)
# False

print(True is True)
# True

# isはオブジェクトがNoneか？という時に1番使われる
a = None

# ------------------------------------------------

# while文

count = 0

while count < 5:
    print(count)
    # countがないと無限ループになってしまうので注意!
    count += 1

# break文を使った書き方
count = 0

while True:
    if count >= 5:
        # while文を途中で抜けることができる
        break
    
    # coutinue
    if count == 2:
        count += 1
        continue
    # 下のprint(次の行)が出力されずに次のループに行く
    
    print(count)
    count += 1

# while else文
count = 0
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
# whileでループしている中でbreakで抜けなければこちらが出力される
else:
    print('done')

# whileループを何かのきっかけでbreakした場合には実行したくないといった場面で使う！

# ------------------------------------------------

# input関数

# コンソールから何かを入力して、その値が違うなら
# 次のループに入って違うものを入れるという風にするには
# whileループとinput関数を使うケースが多い！

while True:
    word = input('Enter')
    num = int(word)
    if num == 100:
        break
    print('next')

# ------------------------------------------------

# for文

some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

# forループの場合

# 反復処理をするものをイテレーターというが、
# そういうイテレーターをinで次々入れていって
# ループを回してそれがなくなった時点で終了するといったことが可能！

for i in some_list:
    print(i)

# 文字列でもできるよ

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    # breakもcontinueも使えるよ
    if word == 'name':
        break
    print(word)

# ------------------------------------------------

# for else文

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')

# ------------------------------------------------

# range関数(forループと一緒によく使われる)

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in num_list:
    print(i)

for i in range(10):
    print(i)

# 1つ目の引数 = index
# 3つ目の引数 = 3個飛ばし
for i in range(2, 10, 3):
    print(i)

for i in range(10):
    print(i, 'hello')

# iはいらないよって時は_に入れる
# _を見れば、forループの中ではインデックス番号が使われないということが
# すぐに分かるので_を使うとコードがわかりやすくなる◎

for _ in range(10):
    print('hello')

# ------------------------------------------------

# enumerate関数

for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1
# 0 apple
# 1 banana
# 2 orange

# こう書けるよ、結構使われるよ
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# ------------------------------------------------

# zip関数

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# iがいろんなところにあって読みにくい
for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

# Mon apple coffee
# Tue banana tea
# Wed orange beer

# zip関数を使って綺麗に書けるよ、直感的に分かりやすい！
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# ------------------------------------------------

# 辞書をfor文で処理する

d = {'x': 100, 'y': 200}

# keyとvalue両方出力したい
# itemsメソッド
# kに始めの変数xが入って、100というvalueがvに入る

for k, v in d.items():
    print(k, ':', v)
x : 100
y : 200

# d.itemsは何を返しているのか
print(d.items())

# dict_items([('x', 100), ('y', 200)])

