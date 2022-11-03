def greet_pythons(items: list) -> None:

	for item in items:
		print(make_greeting(item))


# Make the function global, it will be the same
def make_greeting(item: str) -> str:
	return f"Hello {item}"


names = ["John", "Eric", "Graham", "Terry", "Terry", "Michael"]
greet_pythons(names)
