import sqlite3

# Create a database
db = sqlite3.connect("contacts.sqlite")

# for row in db.execute("SELECT * FROM contacts"):
# 	print(row)

new_email = "newemail@update.com"

# To mak ethe phone customizable
phone = input("Please enter the phone number: ")

# Use parameter substitution
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()

# use parameter substitution
update_cursor.execute(update_sql, (new_email, phone))

print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

# Unpack the tuple
for name, phone, email in db.execute("SELECT * FROM contacts"):
	print(name)
	print(phone)
	print(email)
	print("-" * 20)

db.close()

# when requested phone number, type: 1234;drop table contacts
