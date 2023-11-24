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

BULK INSERT
  { database_name.schema_name.table_or_view_name | schema_name.table_or_view_name | table_or_view_name }
      FROM 'data_file'
    [ WITH
    (
  [ [ , ] BATCHSIZE = batch_size ]
  [ [ , ] CHECK_CONSTRAINTS ]
  [ [ , ] CODEPAGE = { 'ACP' | 'OEM' | 'RAW' | 'code_page' } ]
  [ [ , ] DATAFILETYPE =
      { 'char' | 'native' | 'widechar' | 'widenative' } ]
  [ [ , ] DATA_SOURCE = 'data_source_name' ]
  [ [ , ] ERRORFILE = 'file_name' ]
  [ [ , ] ERRORFILE_DATA_SOURCE = 'errorfile_data_source_name' ]
  [ [ , ] FIRSTROW = first_row ]
  [ [ , ] FIRE_TRIGGERS ]
  [ [ , ] FORMATFILE_DATA_SOURCE = 'data_source_name' ]
  [ [ , ] KEEPIDENTITY ]
  [ [ , ] KEEPNULLS ]
  [ [ , ] KILOBYTES_PER_BATCH = kilobytes_per_batch ]
  [ [ , ] LASTROW = last_row ]
  [ [ , ] MAXERRORS = max_errors ]
  [ [ , ] ORDER ( { column [ ASC | DESC ] } [ ,...n ] ) ]
  [ [ , ] ROWS_PER_BATCH = rows_per_batch ]
  [ [ , ] ROWTERMINATOR = 'row_terminator' ]
  [ [ , ] TABLOCK ]

  -- input file format options
  [ [ , ] FORMAT = 'CSV' ]
  [ [ , ] FIELDQUOTE = 'quote_characters']
  [ [ , ] FORMATFILE = 'format_file_path' ]
  [ [ , ] FIELDTERMINATOR = 'field_terminator' ]
  [ [ , ] ROWTERMINATOR = 'row_terminator' ]
    )]