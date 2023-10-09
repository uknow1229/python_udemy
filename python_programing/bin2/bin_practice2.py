# バイナリデータをバイトごとに取り出したい

from pathlib import Path
import time

bin_path =  Path("sample_binary")
bin_file = open(bin_path, 'rb')

def read_single_chunk_with_variable_items(bin_path, item_sizes):
  """
  ファイルから指定された合計バイト数だけデータを読み込み
  それをitem_sizeに基づいて項目ごとに分解する。

  :param bin_path: 読み込みファイルの名前
  param item_sizes: 各項目のバイト数を示すリストまたはタプル
  :return: 項目ごとのデータのリスト
  """

  chunk_size = sum(item_sizes)
  with open(bin_path, 'rb') as bin_file:
      chunk = bin_file.read(chunk_size)
      items = []
      start = 0
      for size in item_sizes:
          items.append(chunk[start:start+size])
          start += size
          return items

file_name = str(bin_path)
item_sizes = [1, 3, 13]

items = read_single_chunk_with_variable_items(file_name, item_sizes)
for item in items:
    print(item)

