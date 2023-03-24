#ITERABLES: you can iterate over them using a loop or other iterable operations.
my_string = "hello" #each character holds its own index(position)
print(my_string[0])

for character in my_string: 
	print(character)

#where 'character' is my variable that,through the loop, is equal to each character (and its index) from my_string one at a time

##For-loop
my_list = [1,3,5,7,9]
for number in my_list:
	print (number ** 2) #multiply to the power of (2 in this case), 
			    #so 1 to the pwr of 2; 3 to the pwr of 2 etc.

##While-loop
#assigning a boolean value of true to a variable
user_wants_number = True

while user_wants_number == True: 
	print(10) #while the value remains true, print '10'

#using the input method to assign a variable 
user_input = input("Should we print again? (y/n)") #() parameter to the input method
	if user_input == 'n':
		user_wants_number = False
	#if we enter anything other than 'n', then the loop will keep running, otherwise it will stop


input ()
