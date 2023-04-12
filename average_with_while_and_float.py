#Exercise: Create a program that calculates the average of a list of numbers

# Create an empty list to store the numbers
# Prompt the user to enter a series of numbers, one at a time, until they are done
# Convert each input to a float and add it to the list
# Use a for loop to iterate through the list and calculate the sum of all the numbers
# Divide the sum by the length of the list to get the average
# Print the average to the console

numbers_from_user = []

while True:
    num_input = input("Please enter a number or type 'done' to finish: ")
    if num_input == 'done':
        break
    numbers_from_user.append(float(num_input))

sum = 0

for number in numbers_from_user:
    sum += number

average = sum/len(numbers_from_user)

print("The average of your list is: ", average)

