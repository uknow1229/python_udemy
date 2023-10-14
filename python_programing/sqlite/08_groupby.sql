-- SQLite

-- GROUP BY: 特定のカラムで集計する
-- HAVING: GROUP BYで集計したのちに、特定の条件で絞り込む
-- *)WHEREの場合は、集計する前に絞り込み、
-- HAVINGの場合は、集計結果を一部に絞り込む

SELECT
Age, COUNT(*), SUM(Salary), MAX(Salary), AVG(Salary)
FROM
Users
GROUP BY Name, Age;

-- WHERE
SELECT
Age, COUNT(*), AVG(Salary)
FROM
Users
WHERE
Salary > 5000000
GROUP BY Age;

-- HAVING
-- WHERE 絞り込んで集計
-- HAVING 集計したのち絞り込む

SELECT
Age, COUNT(*), AVG(Salary)
FROM
Users
WHERE
Salary > 5000000
GROUP BY Age
HAVING
COUNT(*) > 3;


SELECT
Age, COUNT(*), AVG(Salary)
FROM
Users
WHERE
Salary > 5000000
GROUP BY Age
HAVING
Age > 50;


SELECT
Age, COUNT(*), AVG(Salary)
FROM
Users
WHERE
Salary > 5000000
GROUP BY Age
HAVING
Age > 50
ORDER BY AVG(Salary)
LIMIT 3;

