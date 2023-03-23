##Inheritance

#Superclass
class Student:
	def __init__ (self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average (self):
		return sum(self.marks)/len(self.marks)	

	#def friend (self, friend_name): leaving method like this would cause an attribute error
									#when trying to print friend.salary because this method in
									#the superclass does not have the salary parameter
	@classmethod
	def friend (cls, origin, friend_name, salary) #adding salary as a parameter because the subclass
												  # has 3 parameters (other than self)								
		return cls(friend_name, origin.school, salary) #instead of self.school, because we no longer
											   #have access to the self

#Subclass
class WorkingStudent (Student):
	def __init__ (self, name, school, salary) #passing the same args as superclass 
											  #with an added parameter only used in this subclass	
		
		super().__init__(name, school)		  #calling the superclass init method to set the
											  #simmilar parameters:name and school

		self.salary = salary				  #setting only the new parameter
		



#anna = Student("Anna","Oxford")		
anna = WorkingStudent("Anna", "Oxford", "2000")

#friend = anna.friend("John")
friend = WorkingStudent.friend(anna, "John", "2000") #anna is the origin, John is the friend_name

print(friend.name)
print(friend.school)

print(friend.salary)


input()