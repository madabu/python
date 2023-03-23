#Decorators
#function that gets called before another function
#decorators should always call the function from within

import functools #importing a library which the decorator will use

def my_decorator(func): 
	#to create a decorator you must use a decorator:
	@functools.wraps(func)
	def function_that_runs_func(): #function wraps around the function that you pass as parameter
								   #then you can do things before or after the function
		print("In the decorator.")
		func()
		print("After the decorator.")
	return function_that_runs_func

@my_decorator #applying the decorator to my_function
def my_function():
	print ("In the function.")
#the decorator changes the function
#we pass my_function to the decorator as func
#then a function that wraps around it is created that says:
#I'm in the decorator
#then it runs the func(my_funtion) which says: In the function
#then the wrap around comes full circle and says: After the decorator
#extending the function with something in front of it and after it

my_function() #output would be: In the decorator.
							   #In the function.
							   #After the decorator.

#if we do not run my_function() it would be replaced by function_that_runs_func
#but the decorator should always call the function

input()