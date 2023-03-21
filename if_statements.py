#assigning some string elements to my list
known_people = ["John","Anna","Mary"]

#assigning to a 'person' variable using the input function, prompting the user to specify the name of a person they know
person = input("Enter the person you know: ")	

#if the input they provided matches a name in the 'known-people' list then the if statement will be printed
if person in known_people:
	print("You know {}!}".format(person)) 
#string formatting used to insert variables or values into the string
#{} is a placeholder to be filled by the format method and its parameter 'person' passed as an argument

#if the input provided does not match with any name from the list, the else statement is executed
else:
	print ("You don't know this {}!".format(person))

##Method to print only even numbers

numbers = [1,2,3,4,5,6,7,8,9]

def even_numbers():
	evens = [] #creating an empty list for the even numbers
	for number in numbers: #for each number from the list called 'numbers'
		if number == 2 or number == 4 or number == 6 or number == 8: #as long the number is one of these specified
			evens.append(number) #populate the list with those numbers
	return evens #return the list of even numbers

##A more optimal manner of doing the same thing
def even_numbers_optimal ():
	evens = []
	for number in numbers: # for each number from the list called 'numbers'
		if number % 2 == 0: # if each of the number variables can be divided by 2 
			evens.append (number) #add the numbers to the list of even numbers
	return evens #and return it

##Defining a method using if and elif statements
def user_menu (choice):
	if choice == "a":
		return "Add"
	elif choice == "q"
		return "Quit"	


input()