# ラムダ

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()
# 上記コードを、ラムダを使ってもっと簡単に書けるよ
sample_func = lambda word: word.capitalize

change_words(l, sample_func)
# 上のラムダのコードをこの中に入れても良い
# change_words(l, lambda word: word.capitalize())
# change_words(l, lambda word: word.lower())
# ラムダを使わない場合はどんどんコードが増えていく！

# Mon
# Tue
# Wed
# Thu
# Fri
# Sat
# Sun

# ------------------------------------------------

# ジェネレーター(イテレーターの要素)
# 1要素を取り出してそれを生成していく！

l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print("#################")

# ジェネレーター

def greeting():
    yield 'Good morning'
    # yierd = 生産するといった意味
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)

# Good morning
# Good afternoon
# Good night
#################
# Good morning
# Good afternoon
# Good night

# 同じ反復処理だがジェネレーターの場合は1個1個要素を生産していく

# 下記コードで確認してみると分かりやすい！
g = greeting()

print(next(g))
print('@@@@@')
print(next(g))
print('@@@@@')
print(next(g))

# Good morning
# @@@@@
# Good afternoon
# @@@@@
# Good night

# pythonはyieldを見るとジェネレーターと判断する！

def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))

print(next(g))

# forループで一気に処理して終わってしまうのではなく
# 始めの要素を生成した時点でその状態を保持しているので
# 他の処理(run)をした後にまた(good afternoon)の処理ができたりする！

# Good morning
# run
# run
# run
# Good afternoon
# run
# run
# run
# Good night

# ------------------------------------------------

# リスト内包表記

t = (1, 2, 3, 4, 5)
# これを1つ1つ取り出してリストを作りたい時

r = []
for i in t:
    r.append(i)

print(r)
# [1, 2, 3, 4, 5]

# リスト内包表記は上を1行で書ける！

r = [i for i in t]
print(r)
# [1, 2, 3, 4, 5]

# if文を追加したい場合は？
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)
# [2, 4]

# リスト内包表記
r = [i for i in t if i % 2 == 0]
print(r)
# [2, 4]

# 短いforループはリスト内包表記で書いてもいい🙆‍♀️

# 違う例

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)
# [5, 6, 7, 8, 9, 10, 10, 12, 14, 16, 18
# 20, 15, 18, 21, 24, 27, 30, 20, 24, 28
# 32, 36, 40, 25, 30, 35, 40, 45, 50]

# リスト内包表記
# forループがこんな感じで2個続いたりとか、もっと続く場合は
# 分かりにくくなるので通常通り書いた方がいいと言われている！

r = [i * j for i in t for j in t2]
print[r]
# [5, 6, 7, 8, 9, 10, 10, 12, 14, 16, 18
# 20, 15, 18, 21, 24, 27, 30, 20, 24, 28
# 32, 36, 40, 25, 30, 35, 40, 45, 50]

# ------------------------------------------------

# 辞書内包表記

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)
# {'mon': 'coffee', 'tue': 'milk', 'wed':
# 'water'}

# 辞書内包表記

d = {x: y for x, y in zip(w, f)}
print(d)
# {'mon': 'coffee', 'tue': 'milk', 'wed':
# 'water'}

# ------------------------------------------------

# 集合内包表記

s = set()

for i in range(10):
    if i % 2 == 0:
      s.add(i)
print(s)
# {0, 2, 4, 6, 8}

s = {i for i in range(10) if i % 2 == 0}
print(s)
# {0, 2, 4, 6, 8}

# ------------------------------------------------

# ジェネレーター内包表記

def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# <class 'generator'>
# 0
# 1
# 2
# 3
# 4

# ジェネレーター内包表記
def g():
    for i in range(10):
        yield i

g = g()

g = (i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# <class 'generator'>
# 0
# 1
# 2
# 3

# タプルと間違いやすいので注意！

# ------------------------------------------------

# 名前空間とスコープ

animal = 'cat'

def f():
    animal = 'dog'
    print('after:', animal)

f()
print('grobal:', animal)

# after: dog
# global: cat

# global変数のanimalを関数内から書き換えるには？？
animal = 'cat'

def f():
    # このように宣言する！
    global animal
    animal = 'dog'
    print('local:', animal)

f()
print('grobal:', animal)

# どちらも変わった！
# local: dog
# global: dog

# pythonには、function内の中で
# local変数を出力するfunctionがある！= locals()

animal = 'cat'

def f():
    animal = 'dog'
    print('local:', locals())

f()
print('global:', animal)
# dictionary型で返してくれる！
# local: {'animal': 'dog}
# global: cat

# 同じようにglobalもある
f()
print('grobal:', globals())

# ------------------------------------------------

# 例外処理

# 下記例として書いたが、
# 全てのexceptionをキャッチするような書き方は
# pythonでは推奨されていない

l = [1, 2, 3]
i = 5

try:
    () + l
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
# エラーなく抜けた場合にelseを実行
else:
    print('done')
finally:
    print('clean up')

# ------------------------------------------------

# 独自例外

# 自分たちの作ったエラーということが分かりやすいように
# 独自例外を作って例外を発生させる

class UppercaseError(Exception):
    pass

def check():
    words = ['apple', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')
