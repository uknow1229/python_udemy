-- SQLite

-- EXISTS: IN句と同様に特定の値のものだけで絞り込む
-- IN句とは、実行計画が異なる

EXPLAIN QUERY PLAN SELECT
*
FROM
  Students
WHERE school_id IN (
  SELECT
    id
  FROM
    Schools
  WHERE
    name='北海道北高校'
)

-- EXISTS
SELECT
*
FROM
  Students
WHERE EXISTS (
  SELECT
    1
  FROM
    Schools
  WHERE
    name='北海道北高校' AND
    id = Students.school_id
)

SELECT
*
FROM
  Students
WHERE school_id NOT IN (
  SELECT
    id
  FROM
    Schools
  WHERE
    name='北海道北高校'
)


SELECT
*
FROM
  Students
WHERE NOT EXISTS(
  SELECT
    1
  FROM
    Schools
  WHERE
    name='北海道北高校' AND
    id = Students.school_id
)

