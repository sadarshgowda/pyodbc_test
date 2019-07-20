import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=ABHISHEKGOWDAS\SQLEXPRESS;DATABASE=Northwind;UID=pyodbc;PWD=adarsh')
cursor= cnxn.cursor()

SET IDENTITY_INSERT Categories ON
cursor.execute("insert into Categories(CategoryID,CategoryName) values (0,'Adarsh')")
cnxn.commit()
SET IDENTITY_INSERT Categories OFF