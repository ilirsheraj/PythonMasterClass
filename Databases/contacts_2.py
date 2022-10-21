import sqlite3

# Create a database
db = sqlite3.connect("contacts.sqlite")

# for row in db.execute("SELECT * FROM contacts"):
# 	print(row)

# Unpack the tuple
for name, phone, email in db.execute("SELECT * FROM contacts"):
	print(name)
	print(phone)
	print(email)
	print("-" * 20)

db.close()
