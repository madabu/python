def who_do_you_know ():
	people = input("Please provide a list of people you know, having their first names only separated by commas: ")
	people_list = people.split (",")

	people_without_spaces = []
	for person in people_list:
		people_without_spaces.append(person.strip()) #stripping white spaces
	return people_without_spaces

def ask_user ():
	person = input ("Enter a name of someone you know: ")
	#people = who_do_you_know()
	if person in who_do_you_know():
		print ("You know this {}!".format(person))

ask_user()

input()
