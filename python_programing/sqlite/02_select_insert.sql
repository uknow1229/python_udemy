-- SQLite
-- SELECT

SELECT
*
FROM
Persons;

SELECT
FirstName, LastName
FROM
Persons;


-- 計算式
SELECT 1 + 1;

-- 別名(AS)
SELECT
  FirstName AS 名前,
  LastName AS 名字
FROM
  Persons;

-- 条件絞り込み(WHERE)
SELECT
*
FROM
Persons
WHERE
PersonId=1

-- カラムを繋げる(||)
SELECT
LastName || ',' || FirstName AS 本名
FROM
Persons
WHERE
PersonId=1

-- INSERT
CREATE TABLE Countries(
  Id Integer,
  Name VARCHAR(255),
  Capital VARCHAR(255)
);

INSERT INTO Countries VALUES(
  1, 'Japan', 'Tokyo'
)

INSERT INTO Countries(Name, Capital)
VALUES('US', 'NewYork');

SELECT * FROM Countries;

-- 複数のSQL
INSERT INTO Countries(Id, Name, Capital)
VALUES
  (2, 'UK', 'Rondon'),
  (3, 'France', 'Paris'),
  (4, 'Italy', 'Roma');


CREATE TABLE Capitals(
  Id Integer,
  Name VARCHAR(255)
);

INSERT INTO Capitals
SELECT Id, Capital
FROM Countries;

SELECT * FROM Capitals;