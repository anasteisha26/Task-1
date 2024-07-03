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
I recreated a model using two tables - students and rooms, the relationship between them were rooms. For 'rooms' table, 'id' was a primary key. For 'students' table, 'room_name' was a foreign key. The relationship was one-to-many as many students can live in the same room. Additionally, I needed to define data types and some constraints for each created column.
![image](https://github.com/anasteisha26/Task-1/assets/172603404/a17051fa-d7f3-456b-a0ad-ccba8b5a1f29)


# Given data
At the very beginning of the task, I was given 2 files - students.json and rooms.json that were suppossed to be loaded into the database using Python scripts and functions, defined manually.
![image](https://github.com/anasteisha26/Task-1/assets/172603404/5ff1afec-b283-4fe3-937b-50c210e11fe1) ![image](https://github.com/anasteisha26/Task-1/assets/172603404/99edb9d0-93b6-43fb-ab3a-617b94610931)

# Defined functions
I needed a function to support connection between Python and MySQL. More than that, I also needed a SQLAlchemy engine.
![image](https://github.com/anasteisha26/Task-1/assets/172603404/d7e96545-d1f5-4180-9c5e-d88d6475cb36)

Then I needed a simple function that could return execute queries using cursor object.
![image](https://github.com/anasteisha26/Task-1/assets/172603404/8a40400b-5c80-478f-bb9e-026d9a730d65)

This fucntion specifies the amount of files needed to be loaded and, in a form of a cycle, requests a path to each file. After receiving the path, the function loads the data into corresponding table in a database.
![image](https://github.com/anasteisha26/Task-1/assets/172603404/c1d473c2-07b4-48a5-8199-922beca03106)

This one is a big function that refers to 3 other functions inside of it. It performs a full cycle of work to the queries passed in it. It is able to accept an input fron=m the user, in which format to save: XML or JSON?
![image](https://github.com/anasteisha26/Task-1/assets/172603404/f3d78264-4150-401f-9dd8-b31cb4d52945)

The 3 functions being used inside of the full-cycle function:
![image](https://github.com/anasteisha26/Task-1/assets/172603404/fa5930e2-a615-43ee-b1be-5b91c2ee4178)

# Logging
The logging was added  using 'logging' module in Python.
