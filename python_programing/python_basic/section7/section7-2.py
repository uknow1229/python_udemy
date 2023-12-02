# ダックタイピング
# クラスが別でも、同じ名前のメソッドを使用することができるスタイル

class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError
        
class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)

# オブジェクト指向の考え方
# クラスはこのように扱うと分かりやすくなる1例としてダックタイピング

# --------------------------------------------------

# 抽象クラス
# 特に使う必要がなければあまり使わなくてOK

import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # driveファンクションを必ず継承するクラスで実装してください
    # (personの中では実装されない)
    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        raise Exception('No drive')
        
class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        print('ok')    
    
baby = Baby()
# baby.drive()
adult = Adult()
adult.drive()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

# --------------------------------------------------

# 多重継承
# なるべくなければ良い、順番が分からず同じ名前のメソッドを付け足して
# バグに繋がる可能性もある
# 開発のコードが大きくなってくると多重継承せざる得ないという場合もある

class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

# 上2つの機能を持ったクラスを作る
# 左のPersonが優先され、Carのrunは実行されない
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()

# talk
# car run
# fly

# --------------------------------------------------

# クラス変数

# 再度ユニットで初期化しなくてもいいようなものを共有する時に使われる
# リストなんかは共有してしまってバグに繋がったりするので注意！

class Person(object):
    
    # クラス変数は全て作ったオブジェクトの中で共有される
    kind = 'human'
    
    def __init__(self, name):
        self.name = name
    
    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

# A human
# B human

class T (object):
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')

d = T()
d.add_word('add 3')
d.add_word('add 4')
print(c.words)

# ['add 1', 'add 2']
# ['add 3', 'add 4']

# --------------------------------------------------

# クラスメソッドとスタティックメソッド

class Person(object):
    
    kind = 'human'

    def __init__(self):
        self.x = 100

    # オブジェクトとして生成はされていないが
    # クラスのメソッドと指定してあげることで
    # まだオブジェクトじゃない状況でも
    # クラスのkindを指し示すことができる
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind
    
    # スタティックメソッド
    # あまり使わないかもしれないが覚えておく
    @staticmethod
    def about(year):
        print('about human {}' .format(year))

a = Person()
print(a.what_is_your_kind())
b = Person
print(b.what_is_your_kind())

Person.about(1999)

# human
# human
# about human

# このようにオブジェクトを生成しない状態でも
# インスタンスメソッドやクラスメソッドにアクセスすることができる

# --------------------------------------------------

# 特殊メソッド

class Word(object):
    
    def __init__(self, text):
      self.text = text

    # 文字列として読み込まれた時に呼ばれるメソッド(1番よく使われる)
    def __str__(self):
        return 'Word!!!!'
    
    def __len__(self):
        return len(self.text)
    
    def __add__(self, word):
        self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() + word.text.lower()
        
w = Word('test')
w2 = Word('###########')

# クラスを足し合わせることも特殊メソッドなら可能
# 本来はw.text + w2.text
print(w + w2)

# イコールメソッドが呼ばれる
print(w == w2)



