# while True:
#	n = input("Please enter 'hello':")
#	if n.strip() == 'hello':
#		break

class Psychologist:
	_solution_found = 0;

	def __init__(self):
		self._solution_found = 0;

	def print_solution(self, x):
		print(x)
		self._solution_found = 1;

	def ask(self):
		while True:
			n = input("How can I help you? Please describe your problem.\n")

			if n.find("hungry") != -1:
				self.print_solution("Visit Mensa.")
			if n.find("tired") != -1:
				self.print_solution("Go get some sleep.")
			if n.find("party") != -1 or n.find("Friday") != -1 or n.find("Saturday") != -1 or n.find("love") != -1:
				self.print_solution("Go to a party and dance.")
			if n.find("unhappy") != -1 or n.find("full") != -1 or n.find("depressed") != -1: 
				self.print_solution("Go to the gym.")
			if n.find("sick") != -1:
				self.print_solution("I'm so sorry to hear that. See a doctor and get some rest.")
			if n.find("alone") != -1:
				self.print_solution("Call a friend.")
			if n.find("money") != -1:
				self.print_solution("Get a job.")
			if n.find("touched") != -1:
				self.print_solution("Get a massage.")

			if self._solution_found == 1:
				print("I assume your problem to be solved. See you soon.");
				break;
			else:
				print("I cannot understand you. Please redefine your problem.") 

p1 = Psychologist()

p1.ask();

