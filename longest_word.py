#Write a program that takes in a list of words from the user,
#and prints out the longest word in the list.
#If there are two or more words with the same length that are the longest, print all of them.

list_of_words_from_user = input("Please give me a list of words separated by commas: ").split(',')

longest_words_list = []
max_length = 0

for word in list_of_words_from_user:
    if len(word) > max_length:
        longest_words_list = [word]
        max_length = len(word)
    elif len(word) == max_length:
        longest_words_list.append(word)

print("The longest word(s) is/are: ", ", ".join(longest_words_list))
