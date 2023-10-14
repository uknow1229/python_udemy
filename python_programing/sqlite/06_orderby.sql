-- SQLite
SELECT * FROM Persons;

-- ORDER BY
SELECT
*
FROM 
  Persons
ORDER BY
Age ASC;

--DESC
SELECT
*
FROM
Persons
ORDER BY
Age DESC;

-- 複数
SELECT
*
FROM
Persons
ORDER BY
Age, PhoneNumber DESC;

SELECT
*
FROM
Persons
WHERE
Name LIKE '%田%'
ORDER BY Age;

SELECT
*
FROM
Persons
WHERE
Name LIKE '%田%'
ORDER BY Name
LIMIT 3;

