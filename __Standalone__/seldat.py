import sqlite3

conn = sqlite3.connect("sqlite.db")
# data = conn.execute("SELECT * FROM student LIMIT 4, 2")
data=conn.execute("SELECT * FROM student")
print("STUDENT ID", "STUDENT NAME", "STUDENT CLASS", "STUDENT EMAIL")
for n in data:
    print(n[0],"    ",n[1],"    ", n[2],"   ", n[3])

# conn.close()
print(" ")
st_name=input("Enter the Student Name: - ")
# data=conn.execute("SELECT * FROM student where st_name='cymnt'")

data=conn.execute("SELECT * FROM student where st_name='"+st_name+"'")
print("STUDENT ID", "STUDENT NAME", "STUDENT CLASS", "STUDENT EMAIL")
for n in data:
    print(n[0],"    ",n[1],"    ", n[2],"   ", n[3])
