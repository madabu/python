##Declaring variables:
a = 5
b = 10
my_variable = 56
any_variable_name = 10


string_variable = "hello"
single_quotes = 'strings can have single quotes'


##Printing
print(my_variable)
print("hello, world!")
print(123)

##Methods
##1.Define method no.1
def my_print_method(my_argument): #method with parameter
	print(my_argument)

##2.Call and use method
my_print_method("hello, world!")

##Defining method no.2

def my_multiply_method (number_one, number_two): #uses two parameters 
	return number_one * number_two #returns the multiplication of the parameters

##Assigning a variable using previously defined method
result = my_multiply_method (5, 3)
##Using method no.1 in order to print the variable called 'result' which uses method no.2 to multiply the two parameters provided
my_print_method(result)	

##Two methods used together in another manner
my_print_method(my_multiply_method(5,3))


input ()
