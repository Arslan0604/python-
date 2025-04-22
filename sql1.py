import sqlite3

DB_NAME = "sqlite_db.db"
# napolnenie bazy dannyh
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    sqlite_conn.execute(sql_request, (23, "Python course", 100, 4))
    sqlite_conn.commit()

# Create a new table in the database:

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         student_qty integer,
#         reviews integer
#     );"""
#     sqlite_conn.execute(sql_request)
    
    
