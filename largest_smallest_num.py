# Write a Python program that takes a list of numbers as input
# and outputs the largest and smallest numbers in the list.

list_of_numbers_from_user = input("Give me a list of numbers separated by commas and\n"
                                  "I will tell you which number is the largest"
                                  " and which number is the smallest:"
                                  "\n")
#option 1

# optimal_list_of_numbers = list(map(int, list_of_numbers_from_user.split(',')))
#
# largest_number = max(optimal_list_of_numbers)
# smallest_number = min(optimal_list_of_numbers)
#
# print("The largest number from your list is: ", largest_number)
# print("The smallest number from your list is: ", smallest_number)

#option 2

optimal_list_of_numbers = list_of_numbers_from_user.split(',')

largest_number = int(optimal_list_of_numbers[0])
smallest_number = int(optimal_list_of_numbers[0])

for number in optimal_list_of_numbers:
    number = int(number)
    if number > largest_number:
        largest_number = number
    if number < smallest_number:
        smallest_number = number

print("The largest number from your list is: ", largest_number)
print("The smallest number from your list is: ", smallest_number)