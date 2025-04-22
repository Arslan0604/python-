import sqlite3

DB_NAME = "sqlite_db.db"

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews >= 5" # monipulaticya
    sql_cursor = sqlite_conn.execute(sql_request)
    # for record in sql_cursor:
    #     print(record[1])
    records = sql_cursor.fetchall()
    print(records)
    


# napolnenie bazy dannyh add records

# courses = [
#     (235, "JavaScript course", 99, 54),
#     (43, "C++ course", 12, 43),
#     (54, "Java course", 89, 21),
#     (44, "Ruby course", 77, 11)
# ]

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()

# Create a new table in the database:

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         student_qty integer,
#         reviews integer
#     );"""
#     sqlite_conn.execute(sql_request)
    
    
