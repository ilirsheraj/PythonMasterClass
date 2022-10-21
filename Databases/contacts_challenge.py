import sqlite3

# Check whether the email has been updated
# It will not be unless we have committed
# Create a database
conn = sqlite3.connect("contacts.sqlite")

for row in conn.execute("SELECT * FROM contacts"):
	print(row)

conn.close()
