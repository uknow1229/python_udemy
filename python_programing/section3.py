# num = 1
# name = 'Make'
# is_ok = True

# print(num, type(num ))
# print(name, type(name))
# print(is_ok, type(is_ok))

# print('Hi', 'Mike', sep=',', end='.\n')

# import math
# result = math.sqrt(5)
# print(result)

# y = math.log2(10)
# print(y)

print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don\'t know\"")

print('hello. \nHow are you?')
# 改行したくない場合はrを先頭につける！
print(r'C:\name\name')

# 複数行ある場合はこっちの方が見やすく改行できる！(\は空白行を出さないため)
print("################")
print("""\
line1
line2
line3\
""")
print("################")

# 文字列に演算子を使うこともできる！
print('Hi.' * 3 + 'Mike.')

s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print('#################')
# 1番目から2番目まで
print(word[0:2])
# 上と同様に0を省略できる
print(word[:2])
print('#################')
# 2番目から最後まで
print(word[2:])
word = 'j' + word[1:]
# 全てのwordのコピー
print(word[:])
# indexの長さを求める
n = len(word)
print(n)

s = 'My name is Mike. Hi Mike.'
print(s)
# Myから始まっているか調べる！>> True
is_start = s.startswith('My')
print(is_start)
# Xから始まっていないので、>> False
is_start = s.startswith('X')
print(is_start)

print("#############")

# Mikeがどこにあるか調べる！>> 11
print(s.find('Mike'))
# 後のMikeを見つけたいときはrをつける！>> 20
print(s.rfind('Mike'))

# 何個この文字列に入っているか?>> 2
print(s.count('Mike'))

# 一番最初は大文字、あとは小文字になる
print(s.capitalize())
# 全てのワードの一番始めの文字が大文字になる
print(s.title())
# 全てが大文字になる
print(s.upper())
# 全てが小文字になる
print(s.lower())

# 文字列の置き換え
print(s.replace('Mike', 'Nancy'))
