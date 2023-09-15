# 関数定義

def say_something():
    print('hi')

# pythonは上からスクリプトを読み込んでいくので関数定義をしてから関数を呼び出すこと！
say_something()

# typeは??
print(type(say_something))
# <class 'function'>

# 返り値
def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)
# hi

# 引数
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"
    
result = what_is_this('red')
print(result)
# tomato

# ------------------------------------------------

# 関数の引数と返り値の宣言

# 一応こういう書き方ができるよってことを覚えておく！(こういった書き方はあまりされないが)
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num('a', 'b')
print(r)

# ab
# stringで渡しても実行できる、エラーとして返してはくれないので気をつける

# ------------------------------------------------

# 位置情報とキーワード引数とデフォルト引数

def menu(entree, drink, dessert):
    # このようにキーワードを指定すれば、順序を間違えないで済む！
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu(entree='beef', dessert='beer', drink='ice')

# beef
# beer
# ice

# デフォルト引数

def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu()
# デフォルトで引数が指定されているので何も入れなくても下記が出力される！
# entree = beef
# drink = wine
# dessert = ice

# 書き換え可能！
menu(entree='chicken', drink='beer')
# entree = chicken
# drink = beer
# dessert = ice

# ------------------------------------------------

# デフォルト引数で気をつけること
# リストとかディレクショナリなどをデフォルト引数を用いる場合は
# Noneを用いて関数内の1番始めの部分で空のリストを作る！

def test_func(x, l=[]):
    l.append(x)
    return

y = [1, 2, 3]
r = test_func(100, y)
print(r)
# [1, 2, 3, 100]

r = test_func(100)
print(r)
# [100]
r = test_func(100)
print(r)
# [100, 100]
# 100が2個入った状況で返ってくる、バグに繋がる原因になるので、
# pythonではリストはデフォルト引数に与えるべきではない！(暗黙の了解)

# なぜか？リストは参照渡し・・1番始めに定義した時点でpythonは
# 空のリストをデフォルト引数として用意する（空のリストを指しているLは一回だけ生成される)
# なので2回目に実行した時も同じアドレスを指したままということになる！

# これをpythonでどう解決するか？
# 空のリストでデフォルト引数で渡すのではなく、Noneとしておく！

def test_func(x, l=None):
    # Noneの時だけリストを初期化する
    if l is None:
        l = []
    l.append(x)
    return

# ------------------------------------------------

# 位置引数のタプル化
# 何個引数が入ってくるか分からない場合に*argsを使ってどんどん引数を追加していく！

def say_something(*args):
    # タプル化されたものを一つずつ取り出す
    for arg in args:
      print(arg)

# 引数を何個入れても*argsでまとめてタプル化してくれるよってこと
say_something('Hi!', 'Mike', 'Nancy')
# Hi!
# Mike
# Nancy

# ------------------------------------------------

# キーワード引数の辞書化

def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree='beef', drink='coffee')
# beef coffee

# kwargs
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')
# print(kwargs)
# {'entree': 'beef', 'drink': 'coffee'}

# print(k, v)
# entree beef
# drink coffee

# 他のやり方もできるよ
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
# このように辞書に**つけて渡すケースも見やすいのでよく使われるよ
menu(**d)
# **dでdが展開されて渡される！

# entree beef
# drink ice coffee
# dessert ice

# 位置引数とタプル化と辞書化をまとめてできる
# 順序は＊、**で間違わない！
def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')
# banana
# ('apple', 'orange')
# {'entree': 'beef', 'drink': 'coffee'}

# ------------------------------------------------

# Docstringsとは

# functionのドキュメントを書く場合は、function内で3つの"""で囲って書くのが一つのルール
def example_func(param1, param2):
    """Example function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for succcess, False otherwise.
    """
    print(param1)
    print(param2)
    return True

print(example_func.__doc__)
# docを使うと上で書いたドキュメントの内容が出力される！
# ドキュメントの部分をHTML化してWeb上で見ることも可能！
help(example_func)
# helpを使っても出力される！

# ------------------------------------------------

# 関数内関数

# この関数内だけで繰り返しコードを使う場合
def outer(a, b):
    
    def plus(c, d):
        return c + d
    
    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r)

outer(1, 2)
# 6

# ------------------------------------------------

# クロージャー(結構高度なpythonの技術)

def outer(a, b):
    
    def inner():
        return a + b
    
    return inner

f = outer(1, 2)
r = f()
print(r)
# 3
# これどんな時に使う??1+2を後ほどやりたい今実行したくないって時
# 引数に入れた値を最終的に気にせずに実行したいってケース

# ちょっと分かりにくいのでもう1個例を！
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))
# 314.0
# 314.1592
# 初めに設定した引数を元にして後々用途によって使い分けたいといった時に使うらしい

# クロージャの特性を活かすことで、プログラムの柔軟性を高めることができたり、
# 特定の状態を保持しながら動作する関数を生成することが可能になる！！

# ------------------------------------------------

# デコレーター
def add_num(a, b):
    return a + b

print('start')
r = add_num(10, 20)
print('end')

print(r)
# start
# end
# 30

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b

f = print_info(add_num)
r = f(10, 20)
print(r)
# start
# end
# 30

# decorator

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# decoratorの関数を指定すると、この関数が実行される時にprint_infoに行ってくれる！
@print_info
def add_num(a, b):
    return a + b

f = add_num(10, 20)
print(r)
# start
# end
# 30

# functionに何か機能を付け加えたいときに使う

@print_info
def sun_num(a, b):
    return a - b

# decoratorは一度記載すれば何度でも＠をつけて
# 色々なファンクションの実行の前後処理をdecoratorを用いて実装できる◉

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# ここの順序も大事だよってことを覚えておく！
@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
# start
# func: add_num
# args: (10, 20)
# kwargs: {}
# result: 30
# end
# 30

# decoratorは何かを包み込むといったイメージ
