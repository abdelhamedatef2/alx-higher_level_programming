-- li all records of  table second_table having a name value in my MySQL server.
-- Records are ordered by descending .
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC
