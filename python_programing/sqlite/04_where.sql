-- SQLite
DROP TABLE Persons;

CREATE TABLE Persons(
  PersonId Integer,
  Name VARCHAR(12),
  Age Integer,
  PhoneNumber CHAR(11),
  Comment Text
)

INSERT INTO Persons
VALUES
  (1, '山田 一郎', 18, '08011111111', 'こんにちは'),
  (2, '田中 次郎', 21, '08022222222', 'こんにちは'),
  (3, '佐藤 花子', 15, '08033333333', 'こんにちは'),
  (4, '宮田 よし子', 18, '09011111111', ''),
  (5, '鈴木 五郎', 30, '09022222222', NULL);

-- PersonId=1だけ絞り込み
SELECT
*
FROM
Persons
WHERE
  PersonID=1;

SELECT
*
FROM
Persons
WHERE
  Age=18;

SELECT
*
FROM
Persons
WHERE
  Name='宮田 よし子';

-- NOT EQUAL
SELECT
*
FROM
Persons
WHERE
  Age<>18;

SELECT
*
FROM
Persons
WHERE
  Name<>'宮田 よし子';

-- > < >= <=
SELECT
*
FROM
  Persons
WHERE
  Age >= 18;

-- LIKE(ある条件を満たしている人だけ取り出せる)
SELECT
*
FROM
Persons
WHERE
  Name LIKE '山田%';

SELECT
*
FROM
Persons
WHERE
  PhoneNumber LIKE '080%';

SELECT
*
FROM
Persons
WHERE
  PhoneNumber LIKE '%1111';

-- 中間一致
SELECT
*
FROM
Persons
WHERE
  Name LIKE '%田%';

SELECT
*
FROM
  Persons
WHERE
  Name LIKE '山田 一_';

INSERT INTO Persons
VALUES
  (6, '山田 一', 23, '09033333333', ''),
  (7, '山田 一也', 26, '09044444444', ''),
  (8, '山田 一二三', 27, '09055555555', '');

# 中間一致とか後方一致とかを使うと処理が遅くなるので注意！

-- BETWEEN
SELECT 
  *
FROM
  Persons
WHERE
  PersonId BETWEEN 2 AND 4;

SELECT 
  *
FROM
  Persons
WHERE
  PersonId NOT BETWEEN 2 AND 4;

SELECT
  *
FROM
  Persons
WHERE
  PersonId IN (1, 3, 5);

SELECT
  *
FROM
  Persons
WHERE
  PersonId NOT IN (1, 3, 5);

SELECT
*
FROM
  Persons
WHERE
  Name NOT LIKE '山田 一_';

-- IS NULL
SELECT
*
FROM
Persons
WHERE
Comment IS NULL;


SELECT
*
FROM
Persons
WHERE
Comment IS NOT NULL;

-- 空白取り出し
SELECT
*
FROM
Persons
WHERE
Comment = '';

-- AND, OR
SELECT
*
FROM Persons
WHERE
Age > 18 AND Comment IS NULL;


SELECT
*
FROM Persons
WHERE
Age > 25 OR PersonId < 3;


SELECT
*
FROM Persons
WHERE
(Age >= 18 AND PhoneNumber LIKE '%1') OR (Age >= 25 AND PhoneNumber LIKE '%2');





