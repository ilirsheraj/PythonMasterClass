def greet_pythons(items: list) -> None:
	greeting = "Hello"

	# This is a local function
	def make_greeting(item: str) -> str:
		# return f"Hello {item}"
		return f"{greeting} {item}"

	for item in items:
		print(make_greeting(item))


names = ["John", "Eric", "Graham", "Terry", "Terry", "Michael"]
greet_pythons(names)
