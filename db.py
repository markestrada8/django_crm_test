import mysql.connector

database = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
    # database = "customers",
    auth_plugin = "mysql_native_password"
	)

# prepare a cursor object
cursor_object = database.cursor()

# Create a database
cursor_object.execute("CREATE DATABASE customers")

print("Database created")