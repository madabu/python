#Write a function called find_max that takes a list of numbers as input
#and returns the maximum number in the list.
#Use a for loop to iterate through the list
#and compare each number to the current maximum value.
#If the number is greater than the current maximum,
#update the maximum value. Finally, return the maximum value.

def find_max (numbers_list):
    max_value = numbers_list[0]

    for value in numbers_list:
        if value > max_value:
            max_value = value
    return max_value

numbers_list_from_user = input("Please give me a list of numbers separated by commas: ")
optimal_list_from_user = [int(n) for n in numbers_list_from_user.split(',')]

max_num = find_max(optimal_list_from_user)

print("The maximum value from your list is: {}".format(max_num))