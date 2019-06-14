# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:33:26 2019

@author: user
"""

import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'db_university' )

c = conn.cursor()

c.execute ("""CREATE TABLE student(
          Student_Name TEXT, Student_Age INTEGER, Student_Roll_no INTEGER, Student_Branch TEXT
          )""")

c.execute("INSERT INTO student VALUES ('Sylvester',25, 50000, 'CSE')")
c.execute("INSERT INTO student VALUES ('Yogendra',22, 70000, 'EC')")
c.execute("INSERT INTO student VALUES ('Pradeep',23, 30000, 'CSE')")
c.execute("INSERT INTO student VALUES ('Kunal',26, 30000, 'CSE')")

c.execute("SELECT * FROM student")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM student")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Student_Name", "Student_Age", "Student_Roll_no", "Student_Branch"]


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()
