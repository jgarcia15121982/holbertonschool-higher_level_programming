-- Cities by States
SELECT cities.id as id, cities.name AS name, states.name AS name
FROM cities JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
