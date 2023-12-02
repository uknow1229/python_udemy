# Pythonの書き方

# kとかvとかdとか、コードが長くなると何の変数なのか
# 分からなくなるため分かりやすい名前にしておく(nameとかcountとか)

# 1文字の文字を使うときは大体2行ぐらいであれば良いだろうと言われている
# 練習とか確かめ用の場合だけ使う、実際のアプリ開発でコードが長くなる場合は使わない！

# ----------------------

# ジェネレーターを使えれば使う
# ジェネレーターの方がメモリ上高速で動けるのでforループで回して返すよりいい時がある！

def t():
    # num = []
    for i in range(10):
        yield i
        # num.append(i)
    # return num

for i in t():
    print(i)

# ----------------------

# ラムダ

# 違うファンクションを渡したい時に、また定義してファンクションを呼び出すより
# ただ単純にラムダで他のファンクションを借りてやればいい

def other_func(f):
    print(f(10))

def test_func(x):
    return x * 2

def test_func2(x):
    return x * 5
other_func(test_func)
other_func(test_func2)

other_func(lambda x: x * 2)
other_func(lambda x: x * 5)

# 20
# 20

# ラムダの計算式が複雑だったり、ファンクションが何行も何行もあるような
# ファンクションではうまく使えないので、あまり多用しすぎない！

# ----------------------

# if文こういった書き方もある

y = None
x = 1 if y else 2
print(x)

# 2

# ----------------------

# クロージャ

def base(x):
    def plus(y):
        return x + y
    return plus

plus = base(10)
print(plus(10))
print(plus(30))

# 20
# 40

# ---------------

i = 0
def add_num():
    def plus(y):
        return i + y
    return plus

i = 10
plus = add_num()
print(plus(10))
i = 100
print(plus(30))

# 20
# 130

# グローバル変数を使ってしまうと誰かに書き換えられてコードがおかしくなることがある
# クロージャを使う時にはグローバル変数をうまく隠蔽して使っていく

# ----------------------

# decolator

# 古い書き方
# recommend_restaurant = _hello_decolator(recommend_restaurant)

# 今の書き方
# @_hello_decorator

# 昔のコードを変える場合はチーム内の承諾を得て変える！
# もしかしたら昔のやり方でやる理由があるかもしれない
# 他の企業のソースコードを読んで学んだりする


