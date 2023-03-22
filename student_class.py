##Student exercise with Classes in Python
#create a student class with 'name' and 'school' as arguments
#initialize an empty 'marks' list
#define a method that calculates the average of marks
#initialize an object named 'anna'
#add marks to anna's list of marks
#calculate and print the average of anna's marks


class Student:
	def __init__(self, name, school): #self is the object that we are creating, same for the other args/param
		self.name = name
		self.school = school
		self.marks = []

	#method to calculate average of the marks	
	def average(self):
		return sum(self.marks)/len(self.marks)

#initializing an object of the Student class
anna = Student("Anna", "MIT")
#adding a mark to the 'marks' list
anna.marks.append(56)
anna.marks.append(100)
anna.marks.append(90)

print(anna.average())




input()

