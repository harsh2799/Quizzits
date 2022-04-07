from db_operations import DbOperations
import json

class Main:

	def __init__(self) -> None:
		pass

	def set_username(self, username):
		self.username = username

	def get_username(self):
		return self.username

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


	def sign_up(self, username, password):
		user_list = DbOperations().user_exist_check(username=username)
		if user_list:
			return False, "User Already Exist"
		
		DbOperations().create_user(username=username, password=password)
		return True, "User Created"

	def print_question(self, question):
		options = eval(question[2])
		print(options)
		print(f"""\n\n
		Question: {question[1]}
		A. {options[0]}\t\tB. {options[1]}

		C. {options[2]}\t\tD. {options[3]}
		""")
	
	def take_test(self):
		correct_counter = 0
		options = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
		print(""" There will be 5 questions. Try to answer all of them correctly. All the Best.\n================================================================================= \n	
		  """)
		questions, indexes = DbOperations().get_questions()
		print(indexes)
		for i in indexes:
			self.print_question(questions[i])
			choice = input("\nEnter Your Choice: ")
			if(questions[i][2][options[choice.upper()]] == questions[i][3]):
				correct_counter += 1
		
		print("\n\n*******  End Of Test  *******\n\n")
		self.print_result(correct_counter)
		if correct_counter < 3:
			retake = input("Retake the test? (Y/N)")
			if retake == 'Y' or retake == 'y':
				self.take_test()
		
		DbOperations().store_result(correct_counter, self.username)



	def print_result(self, cc):
		if cc < 3:
			print("Please Try Again....")
		elif cc == 3:
			print("Good Job!")
		elif cc == 4:
			print("Excellent Work!")
		elif cc == 5:
			print("You are a genius!")
		    







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
			logged_in, message = Main().login(username=username, password=password)
		elif auth_choice == 2:
			logged_in, message = Main().sign_up(username=username, password=password)

		print(f"Message: {message}\n\n")


	except Exception as e:
		print(e)


x = Main()
x.set_username(username)
print(x.get_username())

exit = False
try:
	while not exit:
		print("""
		=========================================
				        Options
		=========================================
				
		1. Take Test
		2. Past Results
		3. Test Stats\n\n
		""")

		option = int(input("Enter Your Choice: "))
		if option == 1:
			x.take_test()
		elif option == 2:
			results = DbOperations().get_all_scores(x.get_username())
			scores = json.loads(results) if results else print("No Exams Taken Yet")
			if scores:
				for _ in scores:
					print(f"{_}/5", end=", ")
		elif option == 3:
			results = DbOperations().get_all_scores(x.get_username())
			scores = json.loads(results) if results else print("No Exams Taken Yet")
			if scores:
				print(f"""
					Maximum Score: {max(scores)}/5
					Minimum Score: {min(scores)}/5
					Average Score: {sum(scores)/len(scores)}/5
				""")

		e = input("Want to Exit? (Y/N) : ")
		if e == 'y' or e == 'Y':
			exit = True

	print(" --------------------   BYE   -------------------- ")
except Exception as e:
		print(e)
		
