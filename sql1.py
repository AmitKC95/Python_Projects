import sqlite3

conn = sqlite3.connect("sqlite.db")

# ins = 'INSERT INTO student (st_name, st_class, st_email) VALUES ("Cymnt", "12th", "cymnt@gmail.com")'
# conn.execute(ins)
# st_id=input("Enter the Student ID: - ")
# conn.execute("DELETE FROM student where st_id="+st_id)
# conn.execute('''
#                update student set st_name='ramew' where st_id=1
                
#                '''
#                 )

ins = 'INSERT INTO student (st_name, st_class, st_email) VALUES ("Cymnt", "12th", "cymnt@gmail.com")'
conn.execute(ins)

conn.commit()
conn.close()
