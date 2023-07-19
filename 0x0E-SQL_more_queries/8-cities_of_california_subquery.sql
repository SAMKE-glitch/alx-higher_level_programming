-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Results must be sorted in ascending order by cities.id
-- The states table contains only one record where name = California 
-- But the id can be different, as per the example)
-- You are not allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command
SELECT 'id', 'name'
FROM 'cities'
WHERE 'state_id' IN (SELECT 'id'
FROM 'states'
WHERE 'name' = "California")
ORDER BY 'id';
