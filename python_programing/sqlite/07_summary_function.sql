-- SQLite
-- AVG: 要素の平均値を集計する

DROP TABLE users;

CREATE TABLE Users(
  Name VARCHAR(255),
  Age Integer,
  Salary Integer
);

SELECT abs(random()) % 40 + 20;

INSERT INTO Users
VALUES
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000),
('test', abs(random()) % 40 + 20, abs(random()) % 10000000);

SELECT * FROM Users;

-- COUNT

SELECT
COUNT(*)
FROM
Users;

-- SUM
SELECT
SUM(Salary)
FROM
Users;

-- MAX, MIN
SELECT
MAX(Salary), MIN(Salary)
FROM
Users;

-- AVG
SELECT
AVG(Salary)
FROM
Users;


SELECT
SUM(Salary), AVG(Salary), MAX(Salary), MIN(Salary)
FROM
Users
WHERE
Age > 50;

SELECT
AVG(Age)
FROM
Users;

SELECT
AVG(Name)
FROM
Users;

