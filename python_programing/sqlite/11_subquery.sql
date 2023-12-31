-- SQLite

-- 副問合せ: SQLの中に別のSQL(SELECT)を追加する
-- 1. FROM句で副問合せを指定する
-- 2. IN句の中に副問合せを入れる
-- 3. SELECTの取得結果にSELECTを含める

SELECT
*
FROM
  Musics;


-- 副問合せの結果を選択
-- singerごとの合計の平均値
SELECT
  AVG(album.seconds)
FROM
(
SELECT
  singer_id,
  SUM(seconds) AS seconds
FROM
  Musics
GROUP BY
  singer_id
) AS album


-- 副問合せをINに入れる
SELECT
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

-- SELECTの取得結果の1つに追加
SELECT
  name,
  (
    SELECT AVG(seconds)
    FROM Musics
    WHERE Musics.singer_id = Singers.id
  ) AS 音楽の長さ
FROM
  Singers;

