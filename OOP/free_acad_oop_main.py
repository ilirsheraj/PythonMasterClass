# We will use this to instantiate instances only
from item import Item

item1 = Item("MyItem", 750)

# Private attribute
item1.name = "OtherItem"

print(item1.name)