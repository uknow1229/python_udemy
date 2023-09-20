# クラスの定義

# Person(objet)の中のobjectは書かなくても良いとなったが
# 継承のベースクラスとして扱いましょうとなっているので書いておいた方が良い

class Person(object):
    def say_something(self):
        print('hello')

person = Person()
person.say_something()

def person(name):
    if name == 'A':
        print('hello')

# --------------------------------------------------

# クラスの初期化とクラス変数

class Person(object):
    # selfがないと自分自身に値を保持させられないので
    # 毎回メソッドのところにはselfを付けて自分自身に値を保持していく 
    def __init__(self, name):
        # 自分自身の名前に引数で持ってきた名前を入れる
        self.name = name
        print(self.name)

    def say_something(self):
        # self.nameを他のメソッドからも呼び出せる
        print('I am {}. hello'.format(self.name))
        self.run(5)

    # メソッドにはselfとあるが、selfを渡さずに
    # 第1引数を入れてやっていく
    def run(self, num):
        print('run'* num)

person = Person('Mike')
person.say_something()
# I am Mike. hello
# runrunrunrunrun

# クラスのメソッドには、selfを付けてselfを用いて
# 自分自身の保持した値をアクセスしていくことになる

# --------------------------------------------------

# コンストラクタとデストラクタ

class Person(object):
    # オブジェクトを作るときの初めの時に呼ばれるもの、これがコンストラクタ
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(5)

    def run(self, num):
        print('run'* num)

    # デストラクタ
    # オブジェクトがなくなる時に呼ばれる
    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_something()

print('###########')

# I am Mike. hello
# runrunrunrunrun
# ###########
# good bye

# 明示的に呼びたい場合
del person

# --------------------------------------------------

# クラスの継承

class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    # (Car)で継承されてる
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print('#############')
toyota_car = ToyotaCar()
toyota_car.run()
print('#############')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

# run
# #############
# run
# #############
# run
# auto run

# 継承がないと、コードが重複して綺麗にならないといった時に使う

# どの機能を受け継いでいるかは()の中に入っているものを見ればすぐにわかる

# --------------------------------------------------

# メソッドのオーバーライドとsuperによる親メソッドの呼び出し

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        # メソッドを再度定義すると上書きできる！
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        # self.model = model
        # super = 親のCarを指している
        super().__init__(model)
        self.enable_auto_run =enable_auto_run

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print('#############')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('#############')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()

# run
# #############
# Lexus
# fast
# #############
# super fast
# auto run

# --------------------------------------------------

# プロパティーを使った属性の設定

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', 
                enable_auto_run=False,
                passwd='123'):
        # self.model = model
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    # 読み込むことはできるが書き換えることはできない
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # 書き換え可能にするには？
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    # なぜこのような書き方が必要か？どういう時に使う？
    # ある条件が合致した時だけ書き換えてもいいですよって時

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')


tesla_car = TeslaCar('Model S', passwd='456')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

# ＿＿アンダースコア2つを使うのはどういう時？
# クラス内の中からはアクセスできるが、1度クラスを生成してから
# 属性にアクセスしようとしても、エラーが出るようなやり方をしたい時

# _アンダースコア1つを使うのは・・
# 外部から直接いじってほしくない、実際にはいじれるが
# いじってほしくないことを明示的に見せ、アクセスする場合には
# プロパティでやってくださいって時

# --------------------------------------------------

# クラスを構造体として扱うときの注意

class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)
