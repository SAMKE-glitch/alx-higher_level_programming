-- script the list all records in a table except those with no value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
