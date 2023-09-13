l = [1, 20, 4, 50, 2, 1, 2]

l
[1, 20, 4, 50, 2, 1, 2]

# リストの1番目
l[0]
1
# リストの2番目
l[1]
20
# リストの最後から1番目
l[-1]
2
# リストの最後から2番目
l[-2]
1

l[0:2]
[1, 20]
l[:2]
[1, 20]

l[2:5]
[4, 50, 2]

l[2:]
[4, 50, 2, 1, 2]

l[:]
[1, 20, 4, 50, 2, 1, 2]

# リストの長さ
len(l)
7
# リストのタイプ
type(l)
<class 'list'>

# 1文字1文字取り出してリストに変換
list('abcdefg')
['a', 'b', 'c', 'd', 'e', 'f', 'g']

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1つ飛ばしで摘出したいとき
n[::2]
[1, 3, 5, 7, 9]

# -1とやると後ろから摘出してくれる
n[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# ネストさせた配列
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

x
[['a', 'b', 'c'], [1, 2, 3]]

x[0]
['a', 'b', 'c']

x[1]
[1, 2, 3]

x[0][1]
'b'

x[1][2]
3

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

s
['a', 'b', 'c', 'd', 'e', 'f', 'g']

s[0]
'a'

# 文字列はエラーが出るが、配列の場合は書き換え可能！
s[0] = 'X'
['X', 'b', 'c', 'd', 'e', 'f', 'g']

s[2:5]
['c', 'd', 'e']

s[2:5] = ['C', 'D', 'E']

s
['X', 'b', 'C', 'D', 'E', 'f', 'g']

s[2:5] = []

s
['X', 'b', 'f', 'g']

s[:]
['X', 'b', 'f', 'g']

s[:] = []
s
[]

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 最後にデータを付け加えたいとき
n.append(100)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]

n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]

# 一番始めにデータを入れたい場合
n.insert(0, 200)
[200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]

# 一番最後の100を取り出したいとき
n.pop()
100

n
[200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 一番最初を取り出したいとき（またインデックスを指定）
n.pop(0)
200

n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 削除したいとき
del n[0]

n
[2, 3, 4, 5, 6, 7, 8, 9, 10]

n = [1, 2, 2, 2, 3]

n.remove(2)

n
[1, 2, 2, 3]

n.remove(2)
n.remove(2)
n
[1, 3]

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

x = a + b

x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a += b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

x.extend(y)

x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# -----------------------

# リストのメソッド

r = [1, 2, 3, 4, 5, 1, 2, 3]
# 3がどのインデックスにあるか >> 2
print(r.index(3))

# 3番目のインデックスから3を探してください >> 7
print(r.index(3, 3))

# カウント >> 2
print(r.count(3))

# このリストの中に5はあるか >> exist
if 5 in r:
  print('exist')

# rのソート >> [1, 1, 2, 2, 3, 3, 4, 5]
r.sort()
print(r)

# 逆にソートしたいとき >> [5, 4, 3, 3, 2, 2, 1, 1]
r.sort(reverse=True)
print(r)

# ソートに引数を渡すのではなくリバースもある >> [1, 1, 2, 2, 3, 3, 4, 5]
r.reverse()
print(r)

# スピリット スペースで分けてリストに入れてくれる >> ['My', 'name', 'is', 'Mike.']
s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

# 元に戻す >> My name is Mike.
x = ' '.join(to_split)
print(x)

# >> My ##### name ##### is ##### Mike.
x = ' ##### '.join(to_split)
print(x)

# ドキュメント
print(help(list))

# -----------------------

# リストのコピー

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100

print('j=', j)
print('i=', i)

# j = [100, 2, 3, 4, 5]
# i = [100, 2, 3, 4, 5]

# i = [1, 2, 3, 4, 5]メモリに保存してる一番初めのアドレスをJに入れてくださいということ
# リストの先頭を指しているようなイメージなので、iも書き換わってしまう

# copyメソッド
x = [1, 2, 3, 4, 5]
# メソッドを呼び出してからyに入れる
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)

# yは書き換わったが、xは書き換わっていない
# y = [100, 2, 3, 4, 5]
# x = [1, 2, 3, 4, 5]

X = 20
Y = X
Y = 5

print(id(X))
print(id(Y))
print(Y)
print(X)

# 4390263376
# 4390262896
# 5
# 20

X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)

# リストを使った場合のIDは同様なIDが返ってくる
# 4373915784
# 4373915784
# ['p', 'b']
# ['p', 'b']

# リストの使い所
seat = []
min = 0
max = 5
min <= len(seat) < max
# True

seat.append('p')
min <= len(seat) < max
# True

len(seat)
#1

seat.append('p')
min <= len(seat) < max
# True

len(seat)
# 2
seat.append('p')
seat.append('p')
min <= len(seat) < max
# True

seat.append('p')
min <= len(seat) < max
# False

len(seat)
# 5

seat.pop(0)
# 'p'

min <= len(seat) < max
# True
