# all, any

if all((True, 10 < 20, 'a' == 'a')): # allは全てTrue
    print('allの中の処理')

if not any((30 < 20, 10 < 5, 'a' == 'b')): # anysは1つでもTrue
    print('anyの中の処理')


# 演習問題
msg = input('文字の入力を受け付けます')

if msg == 'A':
    print('Aの入力を受け付けました')
elif msg == 'B':
    print('Bの入力を受け付けました')
else:
    print('その他の文字の入力を受け付けました')

# for

for i in range(10):
    print(i)

for _ in range(100):
    print('A')

for i in range(2,20,3):
    print(i)

# sample = ['John', 'Paul', 'George', 'Ringo']
sample = ('John', 'Paul', 'George', 'Ringo')
for member in sample:
    print(member)

human = {
    'Name': 'Taro',
    'Age': 20,
    'gender': 'Man'
}

for h in human:
    print(h, human.get(h))

# enumerate
# 配列の中の値とインデックスを同時に取得する

sample=['A','B','C']
for index, value in enumerate(sample):
    print(index) # 0 1 2を表示
    print(value) # A B Cを表示

# zip
# 2つの配列の中の値を同時に取得する
# for a,b in zip(list1,list2):

# enumerate, zip, while

fruits = ['grape', 'Pine', 'Apple']

for index, value in enumerate(fruits):
    print('index={}'.format(index))
    print('value={}'.format(value))

classA = ['Taro', 'Hanako', 'Jiro']
classB = ['Katsuo', 'Wakame', 'Taro']

for A, B in zip(classA, classB):
    print('classA student: {}'.format(A))
    print('classB student: {}'.format(B))

count = 0
while count < 10: # countが10より小さい場合は中の処理を実行
    print(count)
    count += 1


# continue 
# ループ内にcontinueがあると処理が一度飛ばされる

# break
# breakが実行されるとループの外に処理が出る

for i in range(10):
    if i == 3:
        continue
    print(i)

for i in range(10):
    if i == 3:
        break
    print(i)


for i in range(10):
    if i == 3:
        continue
    print(i)
else:
    print('ループ処理終了')

num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1
else:
    print('whileループ終了')

# セイウチ演算子(python3.8以降)
# :=イコールの前に：コロンをつけた演算子
# 変数の代入と変数の使用を同時に実行できるという特徴を持っている

if(n:=10)>5: # nに10を代入するのとn>5の比較を同時に実行している
    print('nは5より大きい')

# 1番良く使うパターンはwhile文かな？

n = 0
while(n:=n + 1)< 10:
    print(n)

n = 1
while n < 10:
    print(n)
    n += 1

if (n := 10) > 5:
    print('5より大きい: {}'.format(n))

n = 0
while (n := n + 1) < 10:
    print(n)


