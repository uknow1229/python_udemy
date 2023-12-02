# python(ファイル入力)

f = open(file_path, mode='r') # 読み込みモード
line = f.read() # ファイルの中身全体を読み込み
f.close()

f = open(file_path, mode='r', encoding='utf-8') # utf-8でファイルを開く
f = open(file_path, mode='r', encoding='sjis') # shift-jisでファイルを開く
f = open(file_path, mode='r', newline='¥r¥n') # 改行コードを¥r¥nに指定(crlf)
lines = f.readlines() # 行ごとに分割したリストとして取得
line = f.readline() # ファイルを１行毎に読み込み

# read, readlinesはファイルを全て一気に読み込むため、処理は速いがメモリの消費は大きい(小さいファイル向け)
# readlineはファイルを1行ずつ読み込むため、処理は遅いがメモリの消費は小さい(大きいファイル向け)

# ファイルのopenとcloseを自動的に行う(with)

with open(file_path, mode='r') as f:
    for x in f.readlines():
        
# with構文を抜けると自動的にファイルがクローズされる

# セイウチ演算子(python3.8以降)
# ファイルの代入と比較を同時に行う
with open('file.csv', mode='f') as f:
    while msg := f.readline():
        print(msg)