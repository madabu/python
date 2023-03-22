##Implementation of three methods of a class
#create a 'Store' class
#the init method should take an argument 'name' and initialise it
#create 'items', which should be an empty list
#create an add_item method, which should append a dictionary representing an item to the store's
#items property.
#the dictionary should have keys 'name' and 'price'
#the 'stock_price' method should be implemented and it should add up each item price
#inside self.items to come up with a total and return that

class Store:
	def __init__(self, name):
		self.name = name
		self.items = []

	def add_item (self, name, price):	
		self.item = {
		'name': name
		'price': price
		}
		return self.items.append(item)

	def stock_price (self, price)
		return sum([item['price'] for item in self.items])
		 #iterating over each item in the 'items' list, but we are including only the price in the list



input ()
