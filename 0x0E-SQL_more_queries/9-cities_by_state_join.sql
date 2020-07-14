-- Show cities 
-- in the database
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.state_id = cities.state_id
ORDER by cities.id ASCC;
