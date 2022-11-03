def greet_pythons(items: list) -> None:
	greeting = "Hello"
	print(f"The ID of greeting in outer function is {id(greeting)}")
	print(f"local namespace in 'greet_pythons'(1): {locals()}")

	# This is a local function
	def make_greeting(item: str) -> str:
		# Introduce nonlocal variable: rebind the outer greeting variable
		nonlocal greeting
		print(f"local namespace in 'greet_pythons'(2): {locals()}")
		# Bind greeting to a new string locally
		greeting = "Hi"
		print(f"The ID of greeting in inner function is {id(greeting)}")
		print(f"local namespace in 'greet_pythons'(3): {locals()}")
		return f"{greeting} {item}"

	for item in items:
		print(make_greeting(item))
	# THis will print the outer function value of greeting
	print(f"Inside greet_pythons, 'greeting' is {greeting}")
	print(f"The ID of greeting in greet_pythons is {id(greeting)}")
	print(f"local namespace in 'greet_pythons'(3): {locals()}")

names = ["John"]
# names = ["John", "Eric", "Graham", "Terry", "Terry", "Michael"]
greet_pythons(names)
