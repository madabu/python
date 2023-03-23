##Passing fucntions
#Functions are fist-class objects, which means they can be passed as args to other functions
#returned as values from functions and assigned to variables
#example:

#defining a function that prints a String

def my_function():
	print("Hello from my_function!")

#defining another function that has a parameter which can be switched with a function
#and that returns that function	

def other_function(some_function):
	some_function()

#using my second method to call or pass my first method which returns the function	

other_function(my_function) #output would be: Hello from my_function!

#or

def methodception(another):
	return another()

def add_two_numbers():
	return 35 + 77

print (methodception(add_two_numbers)) #output would be: 112

#Lambda functions are annonymous functions in Python
#shorthand way of defining simple functions
#example:

add = lambda x,y: x+y #a lambda function that takes two arguments (x and y) and returns their sum

result = add(2,3)
print(result) #output would be: 5

#another example:

#this:
(lambda x: x*3)(5) #where 5 takes the place of x

#is the same as this:
def f(x):
	return x*3

print(f(5)) #output would be: 15 in both cases

#lambda functions are often used in conjunction with other functions that take
#functions as arguments: map() (conversion) and filter() (filter a given iterable based on a
#certain condition, returning the elements that satisfy said condition)

#lambda + map() to convert a list of strings to a list of integers:

strings = ['1', '2', '3', '4', '5']
integers = list(map(lambda x: int(x), strings))
print(integers) #output would be: [1, 2, 3, 4, 5]

#^that is the same as this:
#def f(x):
#	return int (x)

#strings ['1', '2', '3', '4', '5']
#integers = list(map(f, strings))
#print(integers)

#lambda + filter () to filter out all the odd numbers from a list of integers:

numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x%2 == 0, numbers))
print(evens) #output would be: [2, 4, 6, 8, 10]

#^that is the same as this:
#def is_even(x):
#	return x%2 == 0

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#evens = list(filter(is_even, numbers))
#print(evens) 



input()

