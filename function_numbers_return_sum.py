#write a  function that takes a list of numbers as input
#and returns the sum of all the numbers in the list.

def add_numbers (list_of_numbers):
    sum = 0

    for number in list_of_numbers:
        sum += number
        return sum

list = [1,2,3,4,5]
sum_of_numbers = add_numbers(list)

print(sum_of_numbers)
