CREATE VIEW amount_of_students AS 
SELECT  
r.id, 
r.name as room_n, 
s.name FROM rooms as r 
LEFT JOIN students as s 
ON s.room = r.id
;

SELECT
id,
room_n as 'name of the room',
COUNT(name) as 'amount of people living in a room'
FROM students_rooms.amount_of_students
GROUP BY id, room_n
ORDER BY id
;
