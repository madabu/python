##Dictionary exercise
#create a dictionary variable called student
#the dictionary must contain three keys:'name','school','grades'
#the values for each must be 'John','Computing', and a tuple with the valuea 66,77, and 88

student = {
	'name': 'John'
	'school': 'Computing'
	'grades': (66, 77, 88)
}

#implement a function calculating a total average grade for a class of students
#modify the 'grades' variable from the average_grade(data) method
#so it accesses the 'grades' key of the 'data' dictionary
#assume that the data argument is a dictionary

def average_grade(data):
	grades = data['grades']
	#using the method's argument 'data' instead of the 'student' dictionary because it helps 
	#with reusing the method for different dictionaries, not just for 'student'
	return sum(grades)/len(grades)

#implement a function that calculates a total average grade for a class of students
#you must add all the grades of all the students together
#you must also count how many grades there are in total in the entire list

def average_grade_all_students(student_list):
	#total of all grades; creating an empty variable
	total = 0
	#number of grades found in the entire list
	count = 0
	for student in student_list: #for each student in student_list
		total = total + sum(student['grades']) #the sum modifies the existing total variable
		#but we can use '+=' to avoid redundancy
		#because x+=y is the same as x = x+y
		count += len(student['grades'])

		return total / count


input ()