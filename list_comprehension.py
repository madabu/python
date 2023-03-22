##List comprehension
#a way to build lists programatically
my_list = [0, 1, 2, 3, 4]

an_equal_list = [x for x in range(5)] #for x in range 5, iterate over range 5 which is a list such as [0, 1, 2, 3, 4]
#including x on the list for each of the elements in range 5

multiply_list = [x * 3 for x in range(5)]
#each element multiplied by 3
print(multiply_list)

#8 / 3 == 6 remainder 2, so what will be printed is the remainder (8%3==2)
print(8 % 3)

#useful for determining if a number is odd or even
print(9 % 2)

#printing the even numbers in the range from 0 to 9
print([n for n in range(10) if n % 2 == 0])

#some values have uppercase letters, others do not. Some have unnecessary spaces, others don't.
people_you_know = ["Rolf", " John", "anna", "GREG"]
#creating a new list to overcome the issues using a new variable and a loop, 
#strip() to remove whitespaces and lower() to turn all values to lowercase
normalised_people = [person.strip().lower() for person in people_you_know]
print(normalised_people)

def who_do_you_know ():
	people = input("Please provide a list of people you know, having their first names only separated by commas: ")
	#spliting the input string into a list of individual names taking the comma as a delimiter
	#returns a list of substrings that are separated by the delimiter	
	people_list = people.split (",")

	#BEFORE

	#people_without_spaces = [] #created a new empty list
	#for person in people_list:
		#people_without_spaces.append(person.strip()) #iterating over each name in people_list using the strip() method
	#return people_without_spaces

	#AFTER 

	#creating a new list using a for loop, where people is my variable representing each person 
	#in my people_list stripped of unnecessary whitespace and taken to lower case
	normalised_people_you_know = [people.strip().lower() for people in people_list]
	return normalised_people_you_know 
	
def ask_user ():
	person = input ("Enter a name of someone you know: ")
	if person in who_do_you_know():
		print ("You know this {}!".format(person)) #prints value if found in list from previous method

ask_user()

input ()