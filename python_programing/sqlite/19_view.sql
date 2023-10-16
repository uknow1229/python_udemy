-- SQLite

-- VIEWでは、間接的にテーブルからデータを取り出すことができるようになります。
-- 外部から利用しやすいインターフェースを提供する際に用いられます。
-- CREATE VIEW VIEW名 AS ~: VIEWの作成
-- DROP VIEW: VIEWの削除

CREATE VIEW v_student
(student_name, school_name, prefecture_name)
AS
SELECT
  st.name,
  sc.name,
  pr.name
FROM
  Students st
INNER JOIN Schools sc
ON  st.school_id = sc.id
INNER JOIN Prefectures pr
ON sc.prefecture_id = pr.id
ORDER BY st.id


SELECT
*
FROM
  v_student
WHERE
student_name='さとうじろう';


UPDATE v_student SET student_name='さとうじろう' WHERE student_name='佐藤次郎'


UPDATE Students SET name='佐藤次郎' WHERE name='さとうじろう'

CREATE VIEW
v_singer_misic(id, name, avg, sum, max, min)
AS
SELECT
  Singers.id,
  Singers.name,
  AVG(Musics.seconds) AS avg_seconds,
  SUM(Musics.seconds) AS sum_seconds,
  MAX(Musics.seconds) AS max_seconds,
  MIN(Musics.seconds) AS min_seconds
FROM
  Singers
INNER JOIN Musics
ON Singers.id = Musics.singer_id
GROUP BY Singers.id, Singers.name
ORDER BY Singers.id, Singers.name

SELECT
*
FROM
v_singer_misic

-- VIEWの削除
DROP VIEW v_singer_misic;