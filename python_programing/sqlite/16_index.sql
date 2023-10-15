-- SQLite

-- INDEXを作成すると少量のデータを絞り込む際に
-- 高速で絞り込むことができる

-- 作成する構文: CREATE INDEX INDEX名
-- ON テーブル名(カラムリスト)
-- 削除する構文: DROP INDEX INDEX名

EXPLAIN QUERY PLAN SELECT
*
FROM
Students
WHERE
name='山田太郎';


CREATE INDEX
idx_name
ON Students(name);

-- 複合INDEX
EXPLAIN QUERY PLAN SELECT
*
FROM
Students
WHERE
name='山田太郎' AND age=15;

CREATE INDEX
idx_name_age
ON Students(name, age);

