-- SQLite

-- WITH: 中間テーブルにデータを格納して、利用する

WITH tmp_p AS(
  SELECT
  *
  FROM
  Prefectures
  WHERE name='北海道'
), tmp_s AS(
  SELECT
    sc.id,
    tmp_p.name
  FROM
    Schools AS sc
  INNER JOIN tmp_p
  ON sc.prefecture_id = tmp_p.id
)
SELECT
*
FROM
  Students AS st
  INNER JOIN tmp_s
  ON st.school_id = tmp_s.id
