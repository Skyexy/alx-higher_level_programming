-- List all cities of CA that can be found in db 'hbtn_0d_usa'
-- 'states' table contains only one record where 'name = California'
-- but 'id' cant be different
-- Results must be sorted in ascending order by 'cities.id'
-- Not allowed to use JOIN keyword
SELECT cities.id, cities.name, states.name
FROM states
INNNER JOIN cities
ON states.id = cities.state_id;
