import sqlite3

#connection allows us to connect 
#python to a SQL database 
connection = sqlite3.connect("./2.db")
#cursor allows us to interact with the SQl DB
cursor = connection.cursor()

query = """

SELECT product_name FROM Products; 
"""

result = cursor.execute(query).fetchall()
print(f"OUR SQL RESULT: {result}")

#BORROM/END OF OUR CODE
connection.commit() #this commits out changes 
connection.close() # this dissconnects our conenction 