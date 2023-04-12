#Write a program that takes in a list of numbers
#and calculates their average.
#The program should first ask the user how many numbers are in the list,
#then prompt the user to enter each number one by one,
#and finally print out the average of the numbers.


#this is the length of the list which we need to calculate the average
how_many_numbers = int(input("If you had to give me a list of numbers, how many would there be on your list: "))

#we also need the total sum of all of the numbers from the list to calculate the average
#and we initialize it with 0 since we do not know what numbers there are on the list yet
sum = 0

#for each number in the range between the first number and the last number, the length of the user's list
for number in range(how_many_numbers):
    #the loop prompts the user to enter each number one by one after declaring how many they want to enter
   number = int(input("Please enter number {}: ".format(number+1)))
                      #number {1},{2},{3} until the reaching the end of the range/length of the list4
   #then to the sum add each number the user adds to their list
   sum += number

average = sum/how_many_numbers #the user enters an int to hold the number of elements, no need to use len

print("The average of the numbers from the list you've given me is: {} ".format(average))