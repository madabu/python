##@classmethod && @staticmethod
#mind the go_to_school method 
#@classmethod and @staticmethod are decorators that modify the behavior of a method inside a class


class Student:
	def __init__(self, name, school): 
		self.name = name
		self.school = school
		self.marks = []
	
	def average(self):
		return sum(self.marks)/len(self.marks)

	@classmethod	
	#not passing the object, we pass the class 'Student'
	#so, a class method is bound to the class and not the instance
	def go_to_school(cls):
	print("I am going to school.") #cls == 'Student'

#another example:

class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    @classmethod
    def from_dict(cls, data):
        return cls(data['arg1'], data['arg2'])

data = {'arg1': 'hello', 'arg2': 'world'}
obj = MyClass.from_dict(data)

	@staticmethod
	#not passing anything as an arg
	#doesn't take the class or instance as its first argument 
	#it's like a regular function, but inside the class
	#used when you want to define a function that logically belongs to a class,
	#but doesn't need access to the class or instance itself

class MyClass2:
    @staticmethod
    def add(x, y):
        return x + y

result = MyClass.add(3, 4)


#initializing an object of the Student class
anna = Student("Anna", "MIT")

anna.go_to_school()
Student.go_to_school() 



input()
