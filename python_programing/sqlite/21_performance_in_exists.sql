-- SQLite

-- IN
-- 外側のテーブルのデータ量が多く、
-- 内側(結合先)のテーブルのデータ量が少ない時はINを利用する

-- EXISTS
-- 外側のテーブルのデータ量が少なく、
-- 内側(結合先)のテーブルのデータ量は多い時はEXISTSを利用する

SELECT
*
FROM
Users u
WHERE
u.school_id IN (
  SELECT id FROM Schools
  WHERE name = '沖縄県1大学'
)


-- EXISTS


SELECT
*
FROM
Users u
WHERE
EXISTS (
  SELECT 1 FROM Schools
  WHERE name = '沖縄県1大学' AND
  id = u.school_id
)


-- IN

SELECT
*
FROM
  Schools
WHERE
id IN (
  SELECT
    school_id
  FROM
    Users
  WHERE
    age = 25
  )


CREATE INDEX idx_school ON Users(school_id);

-- EXISTS


SELECT
*
FROM
  Schools s
WHERE
EXISTS (
  SELECT
    1
  FROM
    Users
  WHERE
    age = 25 AND
    school_id = s.id
);


-- NOT IN, NOT EXISTS


SELECT
*
FROM
  Schools
WHERE
id NOT IN (
  SELECT
    school_id
  FROM
    Users
  WHERE
    age = 25
);


SELECT
*
FROM
  Schools s
WHERE
NOT EXISTS (
  SELECT
    1
  FROM
    Users
  WHERE
    age = 25 AND
    school_id = s.id
);