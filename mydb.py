import sqlite3
db=sqlite3.connect('mydb.sqlite')

db.execute('Create table if not exists Cal_history (id int, expression text,result float)')
db.commit()
db.close()
