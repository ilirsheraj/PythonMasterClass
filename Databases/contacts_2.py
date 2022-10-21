import sqlite3

# Create a database
db = sqlite3.connect("contacts.sqlite")

# for row in db.execute("SELECT * FROM contacts"):
# 	print(row)

# Update the database specific for phone number 1234
# update_sql = "UPDATE contacts SET email = 'update@update.com' WHERE contacts.phone = 1234"

# To change all emails
update_sql = "UPDATE contacts SET email = 'update@update.com'"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
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
