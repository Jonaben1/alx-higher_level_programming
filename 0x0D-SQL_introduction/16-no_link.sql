-- a script that lists all records of
-- a table displaying the score and the name
-- the score being in descending order
SELECT score, name  FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
