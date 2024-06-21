/* This script is presented in two queries. The first one creates a view with a calculated column 'age'. 
The second query calculates the average age of people in a room and returns 5 rooms with the lowest average age. 
*/

CREATE VIEW Age_of_Students AS
SELECT
id,
name,
EXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday)) as age
FROM students;


SELECT
r.id,
r.name,
COUNT(s.name) as 'amount of students living in a room',
AVG(aos.age) as 'average age'
FROM rooms as r
LEFT JOIN students as s
ON r.id = s.room 
LEFT JOIN age_of_students as aos
ON aos.id = s.id
GROUP BY r.id, r.name
ORDER BY average_age ASC
LIMIT 5
;
