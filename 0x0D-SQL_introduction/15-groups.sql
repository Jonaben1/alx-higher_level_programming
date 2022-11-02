-- a script that lists the number of
-- records with the same score
SELECT COUNT(score) FROM second_table GROUP BY score;
