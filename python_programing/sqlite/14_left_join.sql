-- SQLite

-- 外部結合でテーブルを結合すると
-- 紐付けができなかったレコードはNULLとして表示される

-- 自己結合: 同じテーブル同士をINNER JOIN
-- LEFT JOINで結合すること

SELECT
*
FROM
Students AS st
LEFT JOIN Schools AS sc
ON st.school_id = sc.id;


SELECT
*
FROM
Students AS st
LEFT JOIN Schools AS sc
ON st.school_id = sc.id
INNER JOIN Prefectures AS pr
ON sc.prefecture_id = pr.id;

-- self join

SELECT
*
FROM
People;

SELECT
*
FROM
People AS p1
INNER JOIN People AS p2
ON p1.parent_id = p2.id;

SELECT
*
FROM
People AS p1
LEFT JOIN People AS p2
ON p1.parent_id = p2.id;
