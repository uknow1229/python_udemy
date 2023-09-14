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


