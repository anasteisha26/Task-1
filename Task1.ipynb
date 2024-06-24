{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 258,
   "id": "8585d8c5-3750-44b1-aa68-728addf2d713",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Connected successfully\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<pymysql.connections.Connection at 0x1455945fad0>"
      ]
     },
     "execution_count": 258,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pymysql\n",
    "import pymysql.cursors\n",
    "import cryptography\n",
    "import json\n",
    "import pandas as pd\n",
    "import sqlalchemy\n",
    "import psycopg2\n",
    "\n",
    "\n",
    "# Connection details\n",
    "host = \"localhost\"\n",
    "user = \"user\"\n",
    "password = \"24242424kal\"\n",
    "\n",
    "# Establishing a connection\n",
    "def get_conn():\n",
    "    try:\n",
    "        connection = pymysql.connect(\n",
    "        host=host,\n",
    "        user=user,\n",
    "        password=password,\n",
    "        charset='utf8mb4',  # Set the character set to handle special characters\n",
    "        cursorclass=pymysql.cursors.Cursor  # Use a cursor\n",
    "    )\n",
    "        print(\"Connected successfully\")\n",
    "        return connection\n",
    "    except:\n",
    "        print(\"Didn't connect\")\n",
    "\n",
    "get_conn()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "79c18df5-e665-4c4a-b91d-97106440b7b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def execute_query(connection, query):\n",
    "    cursor = connection.cursor()\n",
    "    try:\n",
    "\n",
    "        cursor.execute(query)\n",
    "        connection.commit()\n",
    "        print(\"Запрос выполнен успешно\")\n",
    "\n",
    "    except:\n",
    "\n",
    "        print(\"Произошла ошибка\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8760f186-b71a-46cb-b68b-4ed1c193c907",
   "metadata": {},
   "outputs": [],
   "source": [
    "create_db_query = \"\"\"\n",
    "CREATE DATABASE students_rooms;\n",
    "\"\"\"\n",
    "\n",
    "execute_query(connection, create_db_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59143e5c-f391-4941-bc53-da6a5a1ffd11",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Query that creates a \"rooms\" table\n",
    "create_rooms_table_query = \"\"\"\n",
    "CREATE TABLE students_rooms.rooms (\n",
    "id INT,\n",
    "name VARCHAR(255),\n",
    "PRIMARY KEY(id)\n",
    ");\n",
    "\"\"\"\n",
    "\n",
    "execute_query(connection, create_table_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "88ad5aee-5c96-460b-9363-b64203aca433",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Произошла ошибка\n"
     ]
    }
   ],
   "source": [
    "# Query that creates a \"students\" table\n",
    "create_students_table_query = \"\"\"\n",
    "CREATE TABLE students_rooms.students (\n",
    "birthday DATETIME,\n",
    "id INT,\n",
    "name VARCHAR(255),\n",
    "room INT,\n",
    "sex CHAR(1),\n",
    "PRIMARY KEY(id),\n",
    "FOREIGN KEY (room) REFERENCES rooms(id)\n",
    ");\n",
    "\"\"\"\n",
    "\n",
    "execute_query(connection, create_students_table_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "11cd5ed3-cbcb-4d3a-9a2d-adb85fe68d14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Connection to the 127.0.0.1 for user user created successfully.\n"
     ]
    }
   ],
   "source": [
    "# Importing the sqlalchemy in order  to create an engine\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "# DEFINE THE DATABASE CREDENTIALS\n",
    "user = 'user'\n",
    "password = '24242424kal'\n",
    "host = '127.0.0.1'\n",
    "port = 3306\n",
    "database = 'students_rooms'\n",
    "\n",
    "\"\"\" \n",
    "Python function to connect to the mysql database \n",
    "and return the sqlalchemy object\n",
    "\"\"\"\n",
    "def get_connection():\n",
    "\treturn create_engine(\n",
    "\t\turl=\"mysql+pymysql://{0}:{1}@{2}:{3}/{4}\".format(\n",
    "\t\t\tuser, password, host, port, database\n",
    "\t\t)\n",
    "\t)\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "\n",
    "\ttry:\n",
    "\t\n",
    "\t\t# GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE\n",
    "\t\tengine = get_connection()\n",
    "\t\tprint(\n",
    "\t\t\tf\"Connection to the {host} for user {user} created successfully.\")\n",
    "\texcept Exception as ex:\n",
    "\t\tprint(\"Connection could not be made due to the following error: \\n\", ex)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "f2289d20-2779-4a8e-a954-20ecada692b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please, provide a path to the students.json file \"C:\\Users\\37529\\Desktop\\students.json\"\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "10000"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reading and saving students.json\n",
    "path_to_students_file = input(\"Please, provide a path to the students.json file\")\n",
    "\n",
    "with open(path_to_students_file.replace('\"', ''), 'r') as json_file:\n",
    "    json_students_data = json.load(json_file)\n",
    "\n",
    "# Creating pandas' dataframe from the list of records\n",
    "dfstudents = pd.DataFrame(json_students_data)\n",
    "\n",
    "# Writing dataframe into 'students' table\n",
    "dfstudents.to_sql('students', engine, if_exists='replace', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "bd2306d2-35f3-47ca-8cbd-202b92e862c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please, provide a path to the rooms.json file \"C:\\Users\\37529\\Desktop\\rooms.json\"\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1000"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reading and saving rooms.json\n",
    "path_to_rooms_file = input(\"Please, provide a path to the rooms.json file\")\n",
    "\n",
    "with open(path_to_rooms_file.replace('\"', ''), 'r') as json_file:\n",
    "    json_rooms_data = json.load(json_file)\n",
    "\n",
    "# Creating pandas' dataframe from the list of records\n",
    "dfrooms = pd.DataFrame(json_rooms_data)\n",
    "\n",
    "# Writing dataframe into 'rooms' table\n",
    "dfrooms.to_sql('rooms', engine, if_exists='replace', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 289,
   "id": "8ec186e4-cf0e-441d-aca7-ed00e35cdbb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def execute_read_query(connection, query):\n",
    "\n",
    "    cursor = connection.cursor()\n",
    "\n",
    "    result = None\n",
    "\n",
    "    try:\n",
    "\n",
    "        cursor.execute(query)\n",
    "\n",
    "        result = cursor.fetchall()\n",
    "\n",
    "        return result\n",
    "\n",
    "    except mysql.connector.Error as err:\n",
    "        print(f\"Error: {err}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36e60303-8798-424b-ba50-ba024e0a1da3",
   "metadata": {},
   "outputs": [],
   "source": [
    "host = \"localhost\"\n",
    "user = \"user\"\n",
    "password = \"24242424kal\"\n",
    "db = \"students_rooms\"\n",
    "\n",
    "# Establishing a connection\n",
    "connection = pymysql.connect(\n",
    "    host=host,\n",
    "    user=user,\n",
    "    password=password,\n",
    "    charset='utf8mb4',\n",
    "    db=db, # Set the character set to handle special characters\n",
    "    cursorclass=pymysql.cursors.Cursor  # Use a cursor\n",
    ")\n",
    "\n",
    "\n",
    "with connection.cursor() as cursor:\n",
    "    cursor.execute(\"\"\"\n",
    "    SELECT * FROM students\n",
    "    \"\"\")\n",
    "    result = cursor.fetchall()\n",
    "    print(result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "id": "713578b9-f555-43a2-b550-d0ffcf4e8b48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>name</th>\n",
       "      <th>amount of people in a room</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Room #0</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Room #1</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Room #2</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Room #3</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Room #4</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>995</td>\n",
       "      <td>Room #995</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>996</td>\n",
       "      <td>Room #996</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>997</td>\n",
       "      <td>Room #997</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>998</td>\n",
       "      <td>Room #998</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>999</td>\n",
       "      <td>Room #999</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      id       name  amount of people in a room\n",
       "0      0    Room #0                           9\n",
       "1      1    Room #1                           7\n",
       "2      2    Room #2                           9\n",
       "3      3    Room #3                           5\n",
       "4      4    Room #4                          11\n",
       "..   ...        ...                         ...\n",
       "995  995  Room #995                          13\n",
       "996  996  Room #996                           8\n",
       "997  997  Room #997                           9\n",
       "998  998  Room #998                          14\n",
       "999  999  Room #999                          12\n",
       "\n",
       "[1000 rows x 3 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "with connection.cursor() as cursor:\n",
    "    cursor.execute(first_query)\n",
    "    result = cursor.fetchall()\n",
    "\n",
    "type(result)\n",
    "\n",
    "dffirstquery = pd.DataFrame(result, columns=[\"id\", \"name\", \"amount of people in a room\"])\n",
    "display(df)\n",
    "#cursor.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24c57d84-f850-43e9-9503-df0adc31b75c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_from_first_query = df.to_json(orient = 'records', indent = 4)\n",
    "\n",
    "with open(\"demofile17.json\", \"w\") as ddd:\n",
    "    ddd.write(data_from_first_query)\n",
    "\n",
    "f = open(\"demofile17.json\", \"r\")\n",
    "print(f.read())\n",
    "\n",
    "# результат - неправильный json\n",
    "# update - теперь - идеально!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 320,
   "id": "0248b240-5f1d-44eb-bb4b-a3b34bf67ece",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def execute_and_fetch(query):\n",
    "    try:\n",
    "        with connection.cursor() as cursor:\n",
    "            cursor.execute(query)\n",
    "            result = cursor.fetchall()\n",
    "            display(result)\n",
    "    except pymysql.Error as e:\n",
    "        #print(\"Error pymysql %d: %s\" %(e.args[0], e.args[1]))\n",
    "        print(f\"Error pymysql {e}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 331,
   "id": "9fd6047a-b405-4c2e-a2e7-cbddb2b76341",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((482, 'Room #482', 0, None),\n",
       " (661, 'Room #661', 3, Decimal('11.3333')),\n",
       " (913, 'Room #913', 3, Decimal('19.3333')),\n",
       " (111, 'Room #111', 10, Decimal('31.1000')),\n",
       " (957, 'Room #957', 9, Decimal('32.7778')))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Everything completely works if we don't include the creation of the view \"age_of_students!!!\n",
    "# I could try rewriting the creation of the view as a subquery\n",
    "second_query = \"\"\" \n",
    "SELECT\n",
    "r.id,\n",
    "r.name,\n",
    "COUNT(s.name) as amount_of_students_living_in_a_room,\n",
    "AVG(aos.age) as average_age\n",
    "FROM rooms as r\n",
    "LEFT JOIN students as s\n",
    "ON r.id = s.room \n",
    "LEFT JOIN age_of_students as aos\n",
    "ON aos.id = s.id\n",
    "GROUP BY r.id, r.name\n",
    "ORDER BY average_age ASC\n",
    "LIMIT 5;\n",
    "\"\"\"\n",
    "\n",
    "execute_and_fetch(second_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "212e3648-e690-4d00-8036-d177ab4c9a77",
   "metadata": {},
   "outputs": [],
   "source": [
    "execute_and_fetch(\"\"\" SELECT *\n",
    "FROM students\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 345,
   "id": "9cb64b99-20c7-4678-9957-281945efbe1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/* This script is presented in two queries. The first one creates a view with a calculated column 'age'. \n",
      "The second query calculates the average age of people in a room and returns 5 rooms with the lowest average age. \n",
      "*/\n",
      "\n",
      "CREATE VIEW Age_of_Students AS\n",
      "SELECT\n",
      "id,\n",
      "name,\n",
      "EXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday)) as age\n",
      "FROM students;\n",
      "\n",
      "\n",
      "SELECT\n",
      "r.id,\n",
      "r.name,\n",
      "COUNT(s.name) as amount_of_students_living_in_a_room,\n",
      "AVG(aos.age) as average_age\n",
      "FROM rooms as r\n",
      "LEFT JOIN students as s\n",
      "ON r.id = s.room \n",
      "LEFT JOIN age_of_students as aos\n",
      "ON aos.id = s.id\n",
      "GROUP BY r.id, r.name\n",
      "ORDER BY average_age ASC\n",
      "LIMIT 5\n",
      ";\n"
     ]
    }
   ],
   "source": [
    "second_query = open(r\"C:\\Users\\37529\\Desktop\\2ndQuery.sql\", \"r\")\n",
    "print(second_query.read())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 356,
   "id": "d87adbda-0955-47a7-b519-dd1044c57536",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please, provide a path to the 2ndQuery file \"C:\\Users\\37529\\Desktop\\2ndQuery.sql\"\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\"/* This script is presented in two queries. The first one creates a view with a calculated column 'age'. \\nThe second query calculates the average age of people in a room and returns 5 rooms with the lowest average age. \\n*/\\n\\nCREATE VIEW Age_of_Students AS\\nSELECT\\nid,\\nname,\\nEXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday)) as age\\nFROM students;\\n\\n\\nSELECT\\nr.id,\\nr.name,\\nCOUNT(s.name) as amount_of_students_living_in_a_room,\\nAVG(aos.age) as average_age\\nFROM rooms as r\\nLEFT JOIN students as s\\nON r.id = s.room \\nLEFT JOIN age_of_students as aos\\nON aos.id = s.id\\nGROUP BY r.id, r.name\\nORDER BY average_age ASC\\nLIMIT 5\\n;\""
      ]
     },
     "execution_count": 356,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "path_to_second_query_file = input(\"Please, provide a path to the 2ndQuery file\")\n",
    "\n",
    "second_query = open(path_to_second_query_file.replace('\"', ''), \"r\")\n",
    "second_query = second_query.read()\n",
    "second_query"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 349,
   "id": "4c23740e-c99c-4e42-8a9f-42e4fbce1f10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please, provide a path to the 2ndQuery file \"C:\\Users\\37529\\Desktop\\2ndQuery.sql\"\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/* This script is presented in two queries. The first one creates a view with a calculated column 'age'. \n",
      "The second query calculates the average age of people in a room and returns 5 rooms with the lowest average age. \n",
      "*/\n",
      "\n",
      "CREATE VIEW Age_of_Students AS\n",
      "SELECT\n",
      "id,\n",
      "name,\n",
      "EXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday)) as age\n",
      "FROM students;\n",
      "\n",
      "\n",
      "SELECT\n",
      "r.id,\n",
      "r.name,\n",
      "COUNT(s.name) as amount_of_students_living_in_a_room,\n",
      "AVG(aos.age) as average_age\n",
      "FROM rooms as r\n",
      "LEFT JOIN students as s\n",
      "ON r.id = s.room \n",
      "LEFT JOIN age_of_students as aos\n",
      "ON aos.id = s.id\n",
      "GROUP BY r.id, r.name\n",
      "ORDER BY average_age ASC\n",
      "LIMIT 5\n",
      ";\n"
     ]
    }
   ],
   "source": [
    "# Reading and saving rooms.json\n",
    "path_to_second_query_file = input(\"Please, provide a path to the 2ndQuery file\")\n",
    "\n",
    "with open(path_to_second_query_file.replace('\"', ''), 'r') as second_query:\n",
    "    print(second_query.read())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 359,
   "id": "f5d68879-1307-4ec6-95fb-d5e9a92b1d0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "first_query = \"\"\"\n",
    "SELECT\n",
    "id,\n",
    "room_n as 'name of the room',\n",
    "COUNT(name) as 'amount of people living in a room'\n",
    "FROM students_rooms.amount_of_students\n",
    "GROUP BY id, room_n\n",
    "ORDER BY id;\n",
    "\"\"\"\n",
    "\n",
    "second_query = \"\"\"\n",
    "/* This script is presented in two queries. The first one creates a view with a calculated column 'age'. \n",
    "The second query calculates the average age of people in a room and returns 5 rooms with the lowest average age. \n",
    "*/\n",
    "\n",
    "CREATE VIEW Age_of_Students AS\n",
    "SELECT\n",
    "id,\n",
    "name,\n",
    "EXTRACT(YEAR FROM DATE(NOW())) - EXTRACT(YEAR FROM DATE(birthday)) as age\n",
    "FROM students;\n",
    "\n",
    "\n",
    "SELECT\n",
    "r.id,\n",
    "r.name,\n",
    "COUNT(s.name) as amount_of_students_living_in_a_room,\n",
    "AVG(aos.age) as average_age\n",
    "FROM rooms as r\n",
    "LEFT JOIN students as s\n",
    "ON r.id = s.room \n",
    "LEFT JOIN age_of_students as aos\n",
    "ON aos.id = s.id\n",
    "GROUP BY r.id, r.name\n",
    "ORDER BY average_age ASC\n",
    "LIMIT 5;\n",
    "\"\"\"\n",
    "\n",
    "third_query = \"\"\"\n",
    "/* \n",
    "This script shows the youngest, the oldest people in the room, and their age difference\n",
    "*/\n",
    "SELECT\n",
    "r.id,\n",
    "r.name,\n",
    "AVG(aos.age) as 'average age in a room' ,\n",
    "MAX(aos.age) as 'the oldest in a room',\n",
    "MIN(aos.age) as 'the youngest in a room',\n",
    "MAX(aos.age) - MIN(aos.age) as 'difference between ages'\n",
    "FROM rooms as r\n",
    "INNER JOIN students as s\n",
    "ON r.id = s.room\n",
    "LEFT JOIN age_of_students as aos\n",
    "ON aos.id = s.id\n",
    "GROUP BY r.id, r.name\n",
    "ORDER BY 'difference between ages' DESC\n",
    "LIMIT 5;\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25cc4f5f-336c-429c-ac2e-b6e28b73dbb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "execute_and_fetch(third_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c09a72db-4db5-4160-b8fe-bc8e0ff4927e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
