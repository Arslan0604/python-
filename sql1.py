import sqlite3

DB_NAME = "sqlite_db.db"



with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS courses (
        id integer PRIMARY KEY,
        title text NOT NULL,
        student_qty integer,
        reviews integer
    );"""
    sqlite_conn.execute(sql_request)
    
    
