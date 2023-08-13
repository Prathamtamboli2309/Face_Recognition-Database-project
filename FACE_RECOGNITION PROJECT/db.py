import sqlite3 as sq;


conn=sq.connect("database/student.db")
cur=conn.cursor()

# create a table

cur.execute("""create table if not exists student_details
            (
                s_id primary key,
                f_name text,
                m_name text,
                l_name text,
                contact number,
                exam_name text,
                exam_mark number
            );  
            """)

# enter data in database

cur.execute("select * from student_details")
print(cur.fetchall())
conn.commit()
conn.close()

