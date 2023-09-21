# コードスタイル
"""

pep8 軽めのチェック
flake8 もう少し厳し目
pylint もっと厳し目

"""
# 会社やチームによってルールは異なる！

# スタイルルール

# ;セミコロンで次の行に行くのはやめる
x = 1;
y = 2;

# ラインの長さは80文字まで！それ以上は改行する！
# URLは80文字超えてOK
x = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# 無駄な()はつけない！
if (x and y):
    print('exist')

# インデントは4つのスペースが1番綺麗
x = {
    'test': 'sss'
}

# 関数のデフォルト引数を渡すときはスペースなしでOK
def test_func(x, y, z, bvhfvnajk='test'):
    
# 通常のコードは必ず1個スペース空ける
  x = y

# グローバルで宣言されている関数やクラスの間は2個ずつスペースを空ける

class NoTemplateError(Exception):
    """No Template Error"""


def find_template(temp_file):
    """Find for template file in the given location.

    Returns:
        str: The template file path
    """
# クラスの中のメソッドの間は1個の改行ラインを入れる
# 1番上のimportの下も2行改行

# string
# 文字の代入なんかのとき

word = 'hello'
word2 = '!'

# 分かりにくい代入の書き方
new_word = '{}{}' .format(word, word2)

# 直感的に分かりやすいコード
new_word = word + word2

# こんな場合であればこちらの方が分かりやすい
new_word = '{} $$$$$ {} !!!!!!!' .format(word, word2)

# forループで何かものを足していくとき

# こういった書き方は、文字列をどんどん長くして
# 新しい変数をまた作ってメモリ上でどんどん増やしていくのであまりよくない
long_word = ""
for word in ['fdsaf', 'data', 'dsfda']:
    long_word += "{}fdadfdsa".format(word)

# どうすればいいか？

long_word = []
for word in ['fdsaf', 'data', 'dsfda']:
    long_word.append("{}fdadfdsa".format(word)) 
# リストを取り出してどんどん連結してくれてる
new_long_word = ''.join(long_word)

# メモリ管理上、こちらの方が都合がいい
# ループの中で新しいstringに足していくよりは
# リストにappendして最後にjoinする形にする！

# 文字列
# ''と""どっちを使うかは企業によって違う
print('fbvghdjsvbh')
print("fbvghdjsvbh")
# 中に’がある場合
print("fbvghd'jsvbh")

# 文字列の中に何か代入するときはそれがすぐ分かるように
# 代入の中に文字列があるときは必ず""にしようとしている企業もある
"fbvghdjsvbh {} fbvghdjsvbh" .format('test')

# ファイルを開くときは何か理由がない限りはwithステートメントで
# ファイルを開いて必ず閉じる！

# TODOコメントの書き方
# シャープの後に1個スペース空ける
# (jsakai)の部分は企業内の中で自分が使っているユニークなものを使う
# 会社の中でどの人がツールを書いたか後で分かるように！
# TODO (jsakai) Use locking mechanism for avoiding dead lock issue

# importの記述の部分
# カンマを使ってこのようには書かない！
import collections, csv, os

# if文
# 1行でも2行でも書けるが企業のルールに従う

# 2行の方が分かりやすい！
if x:
    print('exit')
else:
    print('else')

if x: print('test')
else: print('else')

# 大文字・小文字
# クラスに関しては始め大文字、次に繋げるものも大文字(キャメルケース)
# 変数や関数に関しては_で繋ぐ(スネークケース)

# プロパティにする場合
# propertyと書けば、user_nameでアクセスできるので
# get_user_nameのget_はいらない
@property
def get_user_name(self):
    return self.user_name

# グローバル変数を宣言するとき
# 全部大文字、繋ぐのは_アンダースコア

DEFAULT_ROBOT_NAME = 'Roboko'
# グローバル変数はなるべく使わない方がいい
# 書き換えられて他のプログラムを壊してしまうことがないように
# 分かりやすいように示す

