##Advanced decorators
#=decorators that can accept arguments

import functools

def my_decorator(func): 
	@functools.wraps(func)
	def function_that_runs_func(): 
		print("In the decorator.")
		func()
		print("After the decorator.")
	return function_that_runs_func

@my_decorator 
def my_function():
	print ("In the function.")

def my_decorator_with_arguments(number): #takes in a single argument, the number (57)
	def my_decorator_with_arguments (func):
		@functools.wraps(func) #the function bellow is replacing my_function_two
		def function_that_runs_func(*args, **kwargs) #using functools to wrap the func with the other function
		print("In the decorator.")
		if number == 56:
			print("Not running the function.")
		else:
			func(*args, **kwargs) #this represents my_function_two
			#if a function we want to use has parameters 
			#they will first be passed to the function in my decorator (function_that_runs_func)
			#and then to this func
			print("After the decorator.")
		return	function_that_runs_func
	return my_decorator	

@my_decorator_with_arguments(57)
def my_function_two(x,y):
	print (x+y)	#output would be: In the decorator.
								 #124
								 #After the decorator.


#in a decorator with arguments we can pass something like the user's permissions
#if we are creating a website that has an admin page
#we can pass the user's permissions and if the user does not match the appropriate permissions
#we don't show them the admin page

my_function_two(57, 67)	

input()