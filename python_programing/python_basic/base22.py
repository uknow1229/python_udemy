# 例外処理

FileNotFoundError #プログラムで指定されたファイルが見つからないエラー
IndexError #配列などで指定したインデックスに値が存在しないエラー
TypeError #型に関するエラー
ZeroDivisionError #0で割ろうとしたことによるエラー
Exception #全ての例外

# try except

try:
    b = [10,20,30]
    c = b.method_a()
    a=b[4]
    a = 10 / 0

except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    # print(e, type(e))
    pass
except IndexError as e:
    print('indexerror発生')
except Exception as e:
    print('Exception:', e, type(e) )
else:
    a = 10 / 0
    print('Else処理')
finally:
    print('Finally処理')

print('処理を完了しました')

# import traceback : 詳細を表示

# try, except, else, finally
# 例外処理を複数繋いだもの

# raise 例外を返す,例外自作

class MyException(Exception):
    pass

def devide(a, b):
    if b == 0:
        raise MyException('0では割り切れません')
    else:
        return a / b

try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))


# 演習問題(選択ソート)

list_a = [5,7,4,5,1,2,3,2,9,1,4]

# i: 0 => list_aの長さまでループしたインデックス
for i in range(len(list_a)):
    # min_idx: i以上のインデックスでlist_aに最小値の入っているもの
    min_idx = i
    # j: i+1 => list_aの長さ
    for j in range(i+1, len(list_a)):
        if list_a[min_idx] > list_a[j]:
            min_idx = j
        list_a[i], list_a[min_idx] = list_a[min_idx], list_a[i]

print(list_a)