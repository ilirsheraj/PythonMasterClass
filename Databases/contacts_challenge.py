import sqlite3

# Check whether the email has been updated
# It will not be unless we have committed
# Create a database
conn = sqlite3.connect("contacts.sqlite")

# # for row in conn.execute("SELECT * FROM contacts"):
# for row in conn.execute("SELECT * FROM sqlite_master"):
# 	print(row)
#
# conn.close()

# Challenge 2
person = input("Please enter a name: ")

# Pass a tuple
# for row in conn.execute("SELECT * FROM contacts WHERE name = ?", (person,)):
# To make it case insensitive use `LIKE`
for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (person,)):
	print(row)

conn.close()
