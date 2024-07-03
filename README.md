# Task 1
The task consisted of creation of the following sub-tasks:
1. Creation of the suitable enviroment
2. Creation of connection to MySQL using Python and specific modules
3. Creation of the data model using MySQL Workbench
4. Writing script in Python that would support features mentioned below:
    1. Interactive input of paths to the files containing data
    2. Functionality allowing interaction with the database using only Python
    3. Capabiity of saving the results in differenr formats
  
5. Four queries written in files according to specified request
6. Creation of the requirements.txt file
7. Creation of the Dockerfile

# Data model creation
I recreated a model using two tables - students and rooms, the relationship between them were rooms. For 'rooms' table, 'id' was a primary key. For 'students' table, 'room_name' was a foreign key. The relationship was one-to-many as many students can live in the same room.

# Given data
At the very beginning of the task, I was given 2 files - students.json and rooms.json that were suppossed to be loaded into the database using Python scripts and functions, defined manually.
