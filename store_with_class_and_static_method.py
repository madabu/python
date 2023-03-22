##Store exercise using @classmethod and @staticmethod
#define a Store class
#create a franchise method using @classmethod which takes in a store as an argument
#it should return a new Store object, with a name equal to the argument + " - franchise"
#create a store_details method using @staticmethod, which should also take in a store as argument
#the store_details method should return a string representing the argument
#in the following format 'NAME, total stock price: TOTAL'

class Store:
	def __init__ (self, name):
		self.name = name
		self.items = []

	def add_item (self, name, price):
	self.items.append ({
		'name': name
		'price': price
		})	
	def stock_price (self):
		total = 0
		for item in self.items:
			total += item ['price']
			return total

	@classmethod
	def franchise (cls, store)
		return cls(store.name + " - franchise") #using cls, but 'Store' can also be used because
												#cls is a reference to the class itself

	@staticmethod
	def store_details (store)
		return '{}, total stock price: {}'.format(store.name, int(store.stock_price))

store1 = Store ("Emag")
store2 = Store ("Altex") 
store.add_item("mouse", 70)

store.franchise(store1)
store.franchise(store2)

store.store_details(store1)




input()