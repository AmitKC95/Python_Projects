import sqlite3

# Establish connection to SQLite database
conn = sqlite3.connect("sqlite.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute SQL query to create a table
cursor.execute('''
    CREATE TABLE student (
        st_id INTEGER PRIMARY KEY AUTOINCREMENT,
        st_name VARCHAR(50),
        st_class VARCHAR(10),
        st_email VARCHAR(30)
    )
''')

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
