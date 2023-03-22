##Dictionaries
#unique and unordered
#storing data 
#KEY VALUE set:

my_dict = {'name': 'Mada', 'age': 90, 'grades': [100, 90, 80]}

#KEYS:name, age, grades
#VALUES:Mada, 90, [100, 90, 80]
#we can assign anything for the value: lists, tuples etc.

lottery_player = {
	'name': 'Mada'
	'numbers': (1,12,34,56)
}

#using the numbers from the lottery_player dictionnaire, which is a variable, we can calculate their sum 
#with dictionaries, we can access specific keys
sum (lottery_player['numbers'])

#we can dynamically change the key 
lottery_player['name'] = 'John'

universities = [
{
	'name': 'Transylvania'
	'location': 'Romania'
}
{
	'name':'MIT'
	'location': 'US'
	}
]

another_dict_in_dict = {
	'key':{
	'name':'Mada'
	}
}

