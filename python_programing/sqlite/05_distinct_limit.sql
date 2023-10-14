-- SQLite

-- DISTINCT: 列から重複する値を取り除く
-- LIMIT: 指定した行数分だけ取りだす
-- OFFSET: 指定した行数飛ばしてレコードを取り出す

SELECT Age FROM Persons;

-- DISTINCT
SELECT
  DISTINCT Age
FROM
  Persons;

SELECT * FROM Persons;

SELECT
  DISTINCT Name, Age
FROM
  Persons;


SELECT
  DISTINCT Age
FROM
  Persons
WHERE
AGE < 25;

-- LIMIT, OFFSET
SELECT
*
FROM
Persons
LIMIT 3 OFFSET 2;



