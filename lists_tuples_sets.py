##List:
grades = [77,80,90] #using square brakets

print(sum(grades)/len(grades)) 
#to find the average of the list we print the sum of the elements divided by the length of the list, which is the number of elements contained in the list

#lists can be dynamically modified by using append:
grades.append(108)

#or by using the index or the position of the values/items from the list (counting starts at 0)
grades[0] = 60
print(grades[0]) 

##Tuple: immutable, cannot modify once created:
tuple_grades = (77,80,90) #using round brakets

#you can create a new tuple using the elements from the previous tuple (concatenating) as well as the element between the round brakets
tuple_grades = tuple_grades + (100,) 

#must use comma when doing this because python needs the "," in order to recognize that the tuple is indeed a tuple and not a mathematical operation that uses ()

#when defining a tuple with a single value in it the format should be:
my_tuple = (15,)
#BUT, we can also just do this: 
my_tuple2 = 15,
print(tuple_grades)

##Set: collection of unique and unordered values:
set_grades = {77,88,99} #using curly brakets

#cannot access index for sets because they are unordered

##Set operations:
your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

##INTERSECTION: printing only the numbers that can be found in both sets:
print(your_lottery_numbers.intersection(winning_numbers))

##UNION: printing numbers from both sets, but not with duplicates because every element is unique
print(your_lottery_numbers.union(winning_numbers))

##DIFFERENCE: printing the set without the values of {1,2}
print({1,2,3,4}.difference({1,2}))



input()