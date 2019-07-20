import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=ABHISHEKGOWDAS\SQLEXPRESS;DATABASE=Northwind;UID=pyodbc;PWD=adarsh')
cursor = cnxn.cursor()

cursor.execute("select CategoryID,CategoryName from Categories")
#rows = cursor.fetchone()
while True:
    row = cursor.fetchone()
    if not row:
        break
    print('id:', row.CategoryID)
    print('id:', row.CategoryName)

cursor.execute("select CategoryID,CategoryName from Categories")
rows = cursor.fetchall()
for i in rows:
    print(i.CategoryID, i.CategoryName)
    print(i[0], i[1])
