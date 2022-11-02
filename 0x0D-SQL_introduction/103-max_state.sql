-- import a table to a database and write a
-- script that displays the max temperature
-- of each state ordered by state
INSERT INTO hbtn_0c_0 FROM download;
SELECT state, MAX(temperature) AS max_temp FROM hbtn_0c_0 ORDER BY state; 
