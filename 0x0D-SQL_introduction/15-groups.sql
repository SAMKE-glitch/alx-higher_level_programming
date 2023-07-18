-- script that list number of records with the same score 
-- in table second_table of the database hbtn_0c_0 in MYSQL Server
SELECT score, COUNT('score') as number from second_table
FROM second_table
GROUP BY score
ORDER BY score DESC;
