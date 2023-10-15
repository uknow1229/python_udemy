-- SQLite

-- UNION: 2つの選択結果から共通要素は1つにして
-- 合わせた結果を表示
-- UNION ALL: 2つの選択結果を足し合わせた結果を表示
-- EXCEPT: 1つ目の選択結果から2つ目の選択結果に存在するものを除く
-- INTERSECT: 2つの選択結果の共通要素だけ取り出す

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

