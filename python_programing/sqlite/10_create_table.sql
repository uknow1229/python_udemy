-- SQLite
CREATE TABLE Schools(
  id INTEGER PRIMARY KEY,
  name VARCHAR(255)
);


CREATE TABLE Students(
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  age INTEGER CHECK(age>=0) DEFAULT 10,
  school_id INTEGER,
  FOREIGN KEY (School_id)
  REFERENCES Schools(id) ON DELETE CASCADE
)

DROP TABLE Students;

SELECT * FROM Schools;

INSERT INTO Schools(name)
VALUES('北高校')
INSERT INTO Schools(name)
VALUES('東高校')

INSERT INTO Students(name, age, school_id)
VALUES('山田 太郎', 15, 1)

SELECT * FROM Students;

-- UNIQUE制約
INSERT INTO Students(name, age, school_id)
VALUES('山田 太郎', 16, 2)

-- NOT NULL制約
INSERT INTO Students(age, school_id)
VALUES(16, 2)

-- CHECK制約
INSERT INTO Students(name, age, school_id)
VALUES('鈴木 涼子', -1, 1)

-- DEFAULT値
INSERT INTO Students(name, school_id)
VALUES('佐藤 京子', 2)


SELECT * FROM Students;

-- 参照制約をつける(sqliteのみ)
PRAGMA foreign_keys=ON;
