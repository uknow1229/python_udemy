-- SQLite
CREATE TABLE T1(
  id INTEGER PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE T2(
  id INTEGER PRIMARY KEY,
  name VARCHAR(255)
);

SELECT * FROM T1;

INSERT INTO T1 VALUES(1, 'test_t1_2');

-- トランザクションの開始
BEGIN TRANSACTION

-- トランザクションの内容を反映する
COMMIT

-- トランザクションを取り消す
ROLLBACK

-- DEAD LOCK: 複数のプロセスが互いのテーブルをロックしてその次の処理に進めなくなること