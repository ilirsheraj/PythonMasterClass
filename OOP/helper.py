class Item:
	@staticmethod
	def is_integer():
		"""
		This should do something that has a relationship with the class,
		but not something that must be unique per instance. It takes a regular
		parameter
		"""

	@classmethod
	def instantiate_from_something(cls):
		"""
		This should also do something that has a relationship with the class,
		but usually, those are used to manipulate different structures of the data
		to instantiate objects, like we did with the csv. It takes a mandatory
		parameter
		"""

item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()