-- SQLite
SELECT
*
FROM
Countries;

-- update

UPDATE Countries
set Capital='City';

-- UPDATE 特定のレコード
UPDATE Countries
SET Capital='Tokyo'
WHERE Name='Japan'

-- SELECT
SELECT
*
FROM
Capitals;

-- DELETE
DELETE FROM Capitals;

SELECT
*
FROM
Countries;

-- DELETE WHERE
DELETE FROM
Countries
WHERE id=3;