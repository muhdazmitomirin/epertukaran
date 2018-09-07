from django.test import TestCase

# Create your tests here.
#How to Connect Python and SQL Server
import pyodbc
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=10.101.1.100;"
                      "Database=MCDB;"
                      "Trusted_Connection=yes;")
 
cursor = conn.cursor()
cursor.execute('SELECT * FROM MCDB.dbo.tblpersonel')
 
for row in cursor:
    print('row = %r' % (row,))