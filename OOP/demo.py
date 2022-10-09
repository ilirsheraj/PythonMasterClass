a_string = 'this is\na string split\t\tand tabbed'
print(a_string)

raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

# We can do the same as a_string
# In window this sucks even more
b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

# strange character will appear
backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

# with single \ it gives error because it means the string is not finished yet
error_string = r"this string ends with \\"
print(error_string)
