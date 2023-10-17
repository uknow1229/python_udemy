-- SQLite

-- SQLチューニング

-- 実行計画を見る場合は、EXPLAIN QUERY PLANを実行する(sqliteの場合)
-- SCAN TABLEだけの場合、TABLE FULL SCAN
-- USING INDEXの場合、INDEXを利用している
-- COVERING INDEXの場合、INDEXだけで処置が完結している
-- WHEREの条件、ORDER BYなどにINDEXを使うことでFULL SCANからINDEX SCANに変えることができる

-- *で前カラムからデータを取るのではなく、カラムを指定する
-- テーブルに別名をつけてどのテーブルから取得したデータなのかわかるようにする
-- できればHAVINGではなくWHEREで絞り込む
-- 副問合せでのSELECTの実行回数は少なくする

SELECT COUNT(*) FROM Users;


EXPLAIN QUERY PLAN
SELECT * FROM Users WHERE name='北海道1大学 a'

-- INDEXを作成する。
-- 特に、WHEREでの絞り込み、テーブルの紐付け
-- GROUP BY, ORDER BY, DISTINCTなどでは
-- INDEXを利用すると処理を高速化できる可能性がある。

-- インデックス作成: CREATE INDEX index名 ON テーブル名(カラム名)
CREATE INDEX id_name ON Users(name)

EXPLAIN QUERY PLAN
SELECT * FROM Users WHERE name='北海道1大学 a'

DROP INDEX id_name;

EXPLAIN QUERY PLAN
SELECT * FROM Users WHERE school_id=1 ORDER BY grade;


CREATE idx_school_grade
ON Users(school_id, grade);


DROP INDEX idx_school_grade;


-- 関数の実行結果に対してインデックスを貼りたい場合には、関数INDEXを用いる
-- インデックスを利用できないパターン
-- 1.後方一致、前方一致検索
-- 2. 比較の方が異なる場合
-- 3. 行に計算式を利用している場合(age + 10 < 30など)


-- 関数INDEX
EXPLAIN QUERY PLAN
SELECT * FROM Users
WHERE
UPPER(name) = '北海道1大学 A';

CREATE INDEX idx_name ON Users(UPPER(name));

DROP INDEX idx_name;


-- 前方一致、後方一致、中間一致
CREATE INDEX idx_name ON Users(name);

EXPLAIN QUERY PLAN
SELECT * FROM Users WHERE name LIKE '北海道%';

EXPLAIN QUERY PLAN
SELECT * FROM Users WHERE name LIKE '%北海道';

EXPLAIN QUERY PLAN
SELECT * FROM Users WHERE name LIKE '#北海道%';


-- 式を用いたSQL
EXPLAIN QUERY PLAN
SELECT COUNT(*) FROM Users WHERE grade - 20 < 40;

CREATE INDEX idx_grade ON Users(grade);


EXPLAIN QUERY PLAN
SELECT COUNT(*) FROM Users WHERE grade < 60;


DROP INDEX idx_name;
DROP INDEX idx_grade;


SELECT * FROM Users LIMIT 10;


EXPLAIN QUERY PLAN
SELECT
*
FROM
Users
WHERE name || age = '北海道1大学 a23';


CREATE INDEX idx_name_age ON Users(name, age)



EXPLAIN QUERY PLAN
SELECT
*
FROM
Users
WHERE name= '北海道1大学 a23' AND 
age = 23;


DROP INDEX idx_name_age;


