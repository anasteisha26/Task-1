/* 
This script shows the youngest, the oldest people in the room, and their age difference
*/
SELECT
r.id,
r.name,
AVG(aos.age),
MAX(aos.age) as the_oldest_in_a_room,
MIN(aos.age) as the_youngest_in_a_room,
MAX(aos.age) - MIN(aos.age) as difference_between_ages
FROM rooms as r
INNER JOIN students as s
ON r.id = s.room
LEFT JOIN age_of_students as aos
ON aos.id = s.id
GROUP BY r.id, r.name
ORDER BY difference_between_ages DESC
LIMIT 5
;