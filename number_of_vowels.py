#Write a program that takes a string as input
#and prints out the number of vowels in the string.

string_from_user = input("Hello, give me a word and I will tell you how many vowels there are in it: ")

vowels = ['a','e','i','o','u']
vowels_from_user = []

for vowel in string_from_user:
    if vowel in vowels:
        vowels_from_user.append(vowel)

print("The vowels from your word are: ", vowels_from_user)
print("And that means there are {} vowels in your word".format(len(vowels_from_user)))