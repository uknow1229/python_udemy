# タプル型
# リスト[]と似ているがタプルは()で括られる

t = (1, 2, 3, 4, 1, 2)
t
# (1, 2, 3, 4, 1, 2)
type(t)
# <class 'tuple'>

# タプルは新しい値を代入することをサポートしてないのでエラーになる
t[0] = 100

t[0]
# 1
t[-1]
# 2
t[2:5]
# (3, 4, 1)
t
# (1, 2, 3, 4, 1, 2)
t.index(1)
# 0

# 1がインデックス0にあるので、インデックス1から探す
t.index(1, 1)
# 4

t.count(1)
# 2

help(tuple)

# 値は変更できないが、リストを入れることはできる
t = ([1, 2, 3], [4, 5, 6])
t
# ([1, 2, 3], [4, 5, 6])

# これはエラーになるが
t[0] = t[1]

# リストの中に対して値を入れるのは大丈夫
t[0][0] = 100

t = 1, 2, 3
type(t)
# <class 'tuple'>
t
# (1, 2, 3)

t = 1
type(t)
# <class 'int'>

# カンマを入れるとタプルになる！
t = 1,
type(t)
# <class 'tuple'>

t = ()
type(t)
# <class 'tuple'>

t = (1)
t
# 1
type(t)
# <class 'int'>

# タプルのアンパッキング
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)
# 10 20

x, y = (10, 20)
print(x, y)
# 10 20

min, max = 0, 100
print(min, max)
# 0 100

# 長くなりすぎるとプログラムが読みにくくなるので好まれない
a, b, c, d, e, f = 'Mike', '1', '1', 'e', 'f'

# 普通に1つずつ書いた方がよい
a = 'Mike'
b = '1'

# 数字の入れ替えも容易にできる

# アンパッキングを使わない場合、長い
i = 10
j = 20

tmp = i
i = j
j = tmp

print(i, j)
# 20 10

# アンパッキングを使う場合
a = 100
b = 200

a, b = b, a
print(a, b)
# 200 100

# タプルの使い所
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
# ('A', 'B', 'C')
print(answer)
# ['A', 'C']



