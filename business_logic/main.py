from db_operations import DbOperations

class Main:

	def __init__(self) -> None:
		pass

	def set_username(self, username):
		self.username = username


	def login(self, username, password):
		
		user_list = DbOperations().user_exist_check(username=username)
		print(f"user lsit: {user_list}")
		if user_list:
			is_valid = DbOperations().validate_user(username=username, password=password)
			if is_valid:
				return True, "User Logged In Successfully"
			else:
				return False, "Incorrect Username or Password"

		else:
			return False, "User Doesn't Exist"


	def sign_up(self):
		username = input("Enter Username: ")
		password = input("Enter Password: ")
		user_list = DbOperations().user_exist_check(username=username)
		if user_list:
			return False, "User Already Exist"
		
		DbOperations().create_user(username=username, password=password)
		return True, "User Created"







logged_in = False
while not logged_in:
	print("""
	=========================================
			Let's Begin
	=========================================
			
	1. Login
	2. Sign Up\n\n
	""")

	try:
		
		auth_choice = int(input("Enter your choice: "))
		username = input("Enter Username: ")
		password = input("Enter Password: ")
		if auth_choice == 1:
			logged_in, message = Main().login()
		elif auth_choice == 2:
			logged_in, message = Main().sign_up()

		print(f"Message: {message}\n\n")


	except Exception as e:
		print(e)


x = Main()
x.set_username(username)

		
