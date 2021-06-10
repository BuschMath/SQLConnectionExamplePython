import pyodbc 
# Some other example server values are
server = 'localhost\sqlexpress,50100' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# server = 'tcp:myserver.database.windows.net' 
database = 'SampleHR' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

cursor.execute("select * from Employees")
row = cursor.fetchone()
while row:
    print(row[0])
    print(row[1])
    print(row[2])
    print("\n")
    row = cursor.fetchone()