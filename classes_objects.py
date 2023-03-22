##Classes and Objects

#a dictionary only contains data
lottery_player_dict = {
	'name': 'Mada'
	'numbers': (5, 9, 12, 3, 1, 21)
}

#a class contains data/properties
class LotteryPlayer:
	def __init__(self, name): #init method
		self.name = name #"Mada"
		self.numbers = (5, 9, 12, 3, 1, 21)
#a class also contains actions (methods) 		
	def total(self):
		return sum(self.numbers)	

#creating an object from the previously defined class:

player_one = LotteryPlayer()
#this player has whatever properties were defined in my LotteryPlayer class
#whenever a new object is defined, that object is self

print(player.name)
print(player.total)

#a different entity sharing the same signature with player_one
player_two = LotteryPlayer()

#player_one is self, player_two is self, but they are different INSTANCES of self


#when adding the 'name' parameter to the init method, we can change the objects according to the new data
player_one = LotteryPlayer("John")
player_two = LotteryPlayer("Victor")

#self is automatically generated and the name is passed to the 'name' parameter

#we can change the numbers for different players
#in other words, the tuple is erased and replaced, not changed in the class
player_one.numbers = (1, 2, 3, 4, 5, 6)

#player_two has the same numbers as defined in the class





input()