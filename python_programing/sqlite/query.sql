INSERT INTO students (name, student_id, score) VALUES ('山岡', 101, 67);


SELECT AVG(score) AS average_score, SUM(score) AS total_score FROM students;


SELECT student_id
FROM students
WHERE score > (SELECT AVG(score) FROM students);


SELECT *
FROM students
JOIN classes ON students.class_id = classes.class_id;


SELECT *
FROM students, classes
WHERE students.class_id = classes.class_id;


SELECT class_id, COUNT(student_id) AS student_count, AVG(score) AS average_score
FROM students
GROUP BY class_id;
