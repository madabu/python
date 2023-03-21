##Methods 
#uses two parameters and returns their multiplication

def my_method (number_1, number_2):
	return number_1 * number_2

#uses one parameter which it prints

def my_print_method(my_argument):
	print(my_argument)

#combining both methods to print the multiplication of two numbers

my_print_method(my_method(21, 21))

##Defining method using input, lists, split function, strip function, if statements and loops

#assigning to the 'people' variable the input function which prompts the user to provide a list of people they know separated by commas
#the input function accepts the user's input as a string

def who_do_you_know ():
	people = input("Please provide a list of people you know, having their first names only separated by commas: ")
	#spliting the input string into a list of individual names taking the comma as a delimiter
	#returns a list of substrings that are separated by the delimiter	
	people_list = people.split (",")

	#the user might use spaces where not asked to
	#creating a new list that contains the same elements in my previous list, without the whitespaces
	people_without_spaces = []
	for person in people_list:
		people_without_spaces.append(person.strip()) #iterating over each name in people_list using the strip() method
	return people_without_spaces #returning a cleaned up list
	
#combining two methods
def ask_user ():
	person = input ("Enter a name of someone you know: ")
	people = who_do_you_know() #calling previous method
	if person in who_do_you_know():
		print ("You know this {}!".format(person)) #prints value if found in list from previous method

ask_user() #calling method

input ()