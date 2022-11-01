burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)
print("=" * 40)

meals = []
for burger in burgers:
	for topping in toppings:
		meals.append((burger, topping))

print(meals)
print("=" * 40)

# Another option
for meals in [(burger, topping) for burger in burgers for topping in toppings]:
	print(meals)

print("=" * 40)

for burger in burgers:
	for topping in toppings:
		print((burger, topping))

print("=" * 40)

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
	print(nested_meals)

print("=" * 40)

for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
	print(nested_meals)
