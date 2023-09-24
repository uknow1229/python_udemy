import xmlrpc.client


with xmlrpc.client.ServerProxy*('http://127.0.0.1:8000/') as proxy:
    print(proxy.add_num(10, 20))

# クライアントのserverにはあまり処理能力はなく、
# サーバー側に重たい負荷をやってもらい返してもらう！といったケースに使われる

# RESTでもいいのではないか？
# RESTはWEBサーバー上に設置して大量のアクセスをWEBサーバーの機能を使って捌けるとか
# 大量にアクセスを受ける場合はRESTの方が使われる！

# 関数で普通のプログラムの通りに書いて、RESTを呼び出してやらなくていいので
# 非常に簡単にプログラムを書けるのがxmlrpcの特徴

# デメリット
# 関数は内部のプログラムではなく外部のプログラムが実行しているので
# ネットワークの遅延とかでプログラムが遅くなったりするのに気付きにくかったり
# ネットワーク遅延による処理をあまり意識していない感じで
# 書かれることが多いので時々問題になったり
# xmlをパースする時のセキュリティイシューも仕様が変わると変えていかなければならない

# 今はRESTの方が好まれているが
# 社内インフラや簡単にソースコードを違うサーバーに分けて作りたい場合に使われたりする