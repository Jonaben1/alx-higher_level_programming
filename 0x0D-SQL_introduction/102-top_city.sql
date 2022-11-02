-- import a table to a database and write
-- a scriot that displays the top 3 of the 
-- cities temperature during July - August
-- ordered by temperarure descending
INSERT INTO hbtn_0c_0 FROM download;
SELECT city, AVG(temperature) AS avg_temp FROM hbtn_0c_0 ORDER BY temperature DESC LIMIT 3;
