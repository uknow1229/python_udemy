-- SQLite
--CREATE
CREATE TABLE Persons(
    PersonId INTEGER,
    LastName VARCHAR(12),
    FirstName VARCHAR(12),
    PhoneNumber CHAR(11),
    DateOfBirth DATETIME,
    Comment Text
);

-- INSERT
INSERT INTO Persons
VALUES(
    1, 'Taro', 'Yamada', '08011111111', '2019-01-01 11:11:11', 'Comment1'
);

-- SELECT
SELECT * FROM Persons;

-- CREATE TABLE AS SELECT
CREATE TABLE NewPersons AS
SELECT
*
FROM
Persons;

-- SELECT NewPersons
SELECT * FROM NewPersons;

-- DROP
DROP TABLE NewPersons;