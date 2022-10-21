import sqlite3

# Create a database
db = sqlite3.connect("contacts.sqlite")

# for row in db.execute("SELECT * FROM contacts"):
# 	print(row)

new_email = "newemail@update.com"
# phone = 1234

# To mak ethe phone customizable
phone = input("Please enter the phone number: ")

# Update the database specific for phone number 1234
update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
print(update_sql)

# # To change all emails
# update_sql = "UPDATE contacts SET email = 'update@update.com'"
update_cursor = db.cursor()
# update_cursor.execute(update_sql)
update_cursor.executescript(update_sql)
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
