import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'mysql',
    # database = 'customers',
    auth_plugin = 'mysql_native_password'
	)

# Prepare a cursor object
cursor_object = database.cursor()

# Create a database
cursor_object.execute('CREATE DATABASE customers')

print('Database created')