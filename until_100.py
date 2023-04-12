#Write a program that asks the user to enter their name and age,
#and then prints out a message saying how many years they have until they turn 100.

name = input("Hello, what is your name? ")
age = int(input("If you tell me how old you are, I will tell you how long you have until you turn 100: "))

until_100 = 100 - age

print(name + ", you have {} years until you turn 100.".format(until_100))