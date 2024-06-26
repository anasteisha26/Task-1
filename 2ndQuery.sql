SELECT
r.id as room_id,
r.name as room_name,
COUNT(s.name) as amount_of_students_living_in_a_room,
AVG(EXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday))) as average_age_in_a_room
FROM rooms as r
LEFT JOIN students as s
ON r.id = s.room 
GROUP BY r.id, r.name
ORDER BY average_age_in_a_room ASC
LIMIT 5;
