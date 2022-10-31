menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"],
]

# meals = []
# for meal in menu:
# 	if "spam" not in meal:
# 		meals.append(meal)
# 	else:
# 		meals.append("a meal was skipped")
# print(meals)
#
# meals = [meal for meal in menu if "spam" not in meal]
# print(meals)
#
# meals = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
# print(meals)
#
# # Conditional expressions in comprehension
# # x = 12
# x = 13
# expression = "Twelve" if x == 12 else "unknown"
# print(expression)

for meal in menu:
	print(meal, "contains chicken" if "chicken" in meal else "contains beacon" if "beacon" in meal else "contains eggs")

