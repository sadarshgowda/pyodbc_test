
import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=ABHISHEKGOWDAS\SQLEXPRESS;DATABASE=Northwind;UID=pyodbc;PWD=adarsh')
cursor= cnxn.cursor()

cursor.execute("select CategoryID,CategoryName from Categories")
row = cursor.fetchone()
if row:
    print(row)
    print('CategoryId: ', row[0])
    print('CategoryName:', row.CategoryName)

while True:
    row = cursor.fetchone()
    if not row:
        break
    print('CategoryId:', row.CategoryID)

cursor.execute("select CategoryID,CategoryName from Categories")
rows = cursor.fetchall()
for row in rows:
    print(row.CategoryID, row.CategoryName)

