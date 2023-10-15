-- SQLite
-- CASE
SELECT
*
FROM
Users;

SELECT
Age,
CASE
WHEN Age < 30 THEN '20代'
WHEN Age < 40 THEN '30代' 
WHEN Age < 50 THEN '40代' 
ELSE '50代' END AS '年代',
Salary
FROM
Users;

-- GROUP BY
SELECT
CASE
WHEN Age < 30 THEN '20代'
WHEN Age < 40 THEN '30代' 
WHEN Age < 50 THEN '40代' 
ELSE '50代' END AS '年代',
AVG(Salary),
MAX(Salary),
MIN(Salary),
COUNT(*)
FROM
Users
GROUP BY
CASE
WHEN Age < 30 THEN '20代'
WHEN Age < 40 THEN '30代' 
WHEN Age < 50 THEN '40代' 
ELSE '50代' END
ORDER BY
AVG(Salary);

