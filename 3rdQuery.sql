SELECT
r.id,
r.name,
AVG(EXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday))) as average_age_in_a_room ,
MAX(EXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday))) as the_oldest_in_a_room,
MIN(EXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday))) as the_youngest_in_a_room,
MAX(EXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday))) - MIN(EXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday))) as difference_between_ages
FROM rooms as r
INNER JOIN students as s
ON r.id = s.room
GROUP BY r.id, r.name
ORDER BY difference_between_ages DESC
LIMIT 5;
