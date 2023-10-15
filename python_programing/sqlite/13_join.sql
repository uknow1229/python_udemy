-- SQLite

-- 一般的な方法とINNER JOINによる内部結合の方法を学んだ
-- 1.テーブル紐付けの一般的な方法
-- FROM テーブル1 (AS) t1, テーブル2 (AS) t2
-- 2. INNER JOIN, JOIN
-- INNER JOIN テーブル名 (AS) t1
-- ON 紐付けの条件

SELECT
*
FROM
Students;


SELECT
*
FROM
Schools;


SELECT
st.name AS student_name,
st.age AS age,
sc.name AS school_name
FROM
Students AS st, Schools AS sc
WHERE
st.school_id = sc.id


SELECT
*
FROM
Students AS st, Schools AS sc, Prefectures AS pr 
WHERE
st.school_id = sc.id AND
sc.prefecture_id = pr.id


--JOIN INNER JOIN

SELECT
st.name AS student_name,
sc.name AS school_name,
pr.name AS prefecture_name
FROM
Students AS st
INNER JOIN
Schools sc
ON st.school_id = sc.id
INNER JOIN
Prefectures pr
ON sc.prefecture_id = pr.id;