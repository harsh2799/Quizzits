import sqlite3 as sql


class DbOperations:

	def __init__(self) -> None:
		self.conn = sql.connect("test.db")

	# def get_connection(self):
	# 	conn = sql.connect("test.db")
	# 	return conn

	def user_exist_check(self, username=''):
		# conn = self.get_connection()
		cursor = self.conn.execute(f"select * from users where username = '{username}'")
		users = cursor.fetchall()
		return users

	def create_table_user(self):
		# conn = self.get_connection()
		self.conn.execute("CREATE TABLE USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
		USERNAME VARCHAR(45) UNIQUE NOT NULL, \
		PASSWORD VARCHAR(50) NOT NULL)")

	def get_table(self, table_name):
		# conn = self.get_connection()
		cursor = self.conn.execute(f"select * from {table_name}")
		print(cursor.fetchall())

	def validate_user(self, username="", password=""):

		cursor = self.conn.execute(f"select * from USERS as U where U.username='{username}' and U.password='{password}'")
		user = cursor.fetchall()
		print(user)
		return user

	def create_user(self, username="", password=""):
		self.conn.execute(f"insert into USERS(`username`,`password`) values('{username}', '{password}')")
		self.conn.commit()
		return True

	def view_all(self, username=""):
		cursor = self.conn.execute(f"select * from users")
		print(cursor.fetchall())




# DbOperations().create_table_user()
print(DbOperations().view_all())