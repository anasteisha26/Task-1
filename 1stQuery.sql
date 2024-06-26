SELECT
r.id as room_id,
r.name as room_name,
COUNT(s.name) as people_amount_in_a_room
FROM rooms AS r 
LEFT JOIN students AS s 
ON s.room = r.id
GROUP BY r.id, r.name
ORDER BY r.id
;
