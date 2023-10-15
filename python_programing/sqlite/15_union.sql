-- SQLite

SELECT
name, age
FROM
Students
UNION
SELECT
name, age
FROM
People;


-- UNION ALL
SELECT
name, age
FROM
Students
UNION ALL
SELECT
name, age
FROM
People;


-- EXCEPT

SELECT
name, age
FROM
Students
EXCEPT
SELECT
name, age
FROM
People;

-- INTERSECT(共通要素)
SELECT
name, age
FROM
Students
INTERSECT
SELECT
name, age
FROM
People;

