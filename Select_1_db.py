import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=ABHISHEKGOWDAS\SQLEXPRESS;DATABASE=Northwind;UID=pyodbc;PWD=adarsh')
cursor = cnxn.cursor()

cursor.execute("select CategoryID,CategoryName from Categories")
row = cursor.fetchone()
print(row)
row = cursor.fetchall()
print(row)
cursor.execute("select CategoryID,CategoryName from Categories")
row = cursor.fetchone()
print("category ID",row[0])
print("category name",row[1])
print("category ID",row.CategoryID)
print("category name",row.CategoryName)