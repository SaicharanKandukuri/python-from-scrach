import mysql.connector

mydb = mysql.connector.connect(
    user="zman", password="Sai.k123089" )
print(mydb)

mycorsor = mydb.cursor()
mycorsor.execute("use zman")
#mycorsor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('peter', "Lowstreet 4"),
    ('Amy', "Apple st 652"),
    ('Hannah', "Mountain 21"),
    ('Sandy', "Valley 345"),
    ('Betty', "Lowstreet 4"),
]
mycorsor.executemany(sql, val)
print(mycorsor.execute("SELECT * FROM customers"))