-- import a table to a database and write
-- a script that displays the average 
-- temperature by city ordered by
-- temperature descending
INSERT INTO hbtn_0c_0 FROM download;
SELECT city, AVG(temperature) as avg_temp FROM hbtn_0c_0 ORDER BY temperature DESC;
