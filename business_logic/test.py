import sqlite3 as s
import random

conn = s.connect("test.db")

# conn.execute("CREATE TABLE test_data (id INTEGER PRIMARY KEY AUTOINCREMENT, username LONGTEXT NOT NULL, all_tests LONGTEXT NOT NULL)")

print(conn.execute("select * from test_data").fetchall())