# Rewrite the following code to use a list comprehension, instead of a for loop.
# Add your solution below the loop, so that the resulting list is printed out
# below output - that makes it easier to check that it's producing exactly
# the same list (and avoids entering the input text twice).

text = input("Please enter your text: ")

output = []
for x in text.split():
	output.append(len(x))
print(output)

# type your solution here:
text_list = [len(x) for x in text.split()]
print(text_list)

# It could be useful to store the original words in the list, as well.
# The for loop would look like this (note the extra parentheses, so
# that we get tuples in the list):

output = []
for x in text.split():
	output.append((x, len(x)))
print(output)

# type the corresponding comprehension here:
list_tuple = [(x, len(x)) for x in text.split()]
print(list_tuple)

# List to set comprehension to avoid duplicates
set_tuple = {(x, len(x)) for x in text.split()}
print(set_tuple)
