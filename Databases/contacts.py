import sqlite3

# Create a database
db = sqlite3.connect("contacts.sqlite")
# create a table
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 46966, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@email.com')")

# Query the DB in python
# No need to add semicolon at the end
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())  # returns a list of tuples
print(cursor.fetchone())  # first row
print(cursor.fetchone())  # second row
print(cursor.fetchone())  # None, there are only two rows

# In this case this loop will not print anything because of generator
for name, phone, email in cursor:
	print(name)
	print(phone)
	print(email)
	print("-" * 20)

cursor.close()
# Commit changes
db.commit()
db.close()
