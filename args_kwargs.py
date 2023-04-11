##args & kwargs
#args & kwargs are special parameters that can be used in function definitions
#to pass a variable number of arguments to a function

#*args = arguments
#used to pass a variable number of non-keyword arguments to a function
#the args will be collected into a tuple
#example:

def my_func1(*args):
	for arg in args:
		print(arg)

my_func(1,2,3)
my_func("hello","world")

#**kwargs = keyword arguments
#used to pass a variable number of arguments (i.e., arguments that are named) to a function
#the kwargs will be collected into a dictionary 
#example:

def my_func2(**kwargs):
	for key, value in kwargs.items():
		print(key, value)

my_func2(name="Alina", age = 20)

#example based on inheritance exercise:

class Student:
	def __init__ (self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average (self):
		return sum(self.marks)/len(self.marks)	

	@classmethod
	def friend (cls, origin, friend_name, *args) #substituting salary with args 
						     #which means that we can take and pass any number of args							
		return cls(friend_name, origin.school, *args) 

class WorkingStudent (Student):
	def __init__ (self, name, school, salary, job_title) #adding another parameter
		
		super().__init__(name, school)		  

		self.salary = salary	
		self.job_title = job_title #setting the new parameter
		
anna = WorkingStudent("Anna", "Oxford", "2000","Lifeguard")

friend = WorkingStudent.friend(anna, "John", "2000", "Cashier") 
#we can add a job title or whatever other arg
#without implementing it in the @classmethod

#if we were to use **kwargs, we would use: salary = 2000 and job_title = "Cashier"
#we could pass both *args and **kwargs 

print(friend.name)
print(friend.school)

print(friend.salary)  







input()

