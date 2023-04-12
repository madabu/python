# Exercise: Create a program that counts the occurrences of each word in a given string

# Prompt the user to enter a string
# Convert the string to lowercase and split it into a list of words using the split() method
# Create an empty dictionary to store the word counts
# Use a for loop to iterate through each word in the list
# If the word is already in the dictionary, increment its count by 1
# If the word is not in the dictionary, add it with a count of 1
# Print out the dictionary of word counts

string_from_user = input("Please give me a list of words separated by one space,\n"
                         "I will tell you how many times a word is repeated if you do that:  ")

word_list = string_from_user.lower().split()
word_counts = {}

for word in word_list:
    if word in word_counts: #if the word has already been entered in the dict as a key, move to the next line and
        word_counts[word] += 1 #raise its count (increment) by 1
    else:
        word_counts[word] = 1 #otherwise, just count it once

print(word_counts)

#the dict is empty to begin with
#the first if statement will be false and the loop will move on to the else statement
#when the if statement is true, the key is incremented by 1