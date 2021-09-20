import psycopg2

connection = psycopg2.connect(database="example", port="5432", host= "127.0.0.1", user="postgres", password="boluwatife")

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table1;')

cursor.execute("CREATE TABLE table1( id INTEGER PRIMARY KEY, completed BOOLEAN NOT NULL DEFAULT False );")

cursor.execute('INSERT INTO table1(id, completed) VALUES(%s, %s)', (1, True))

SQL = 'INSERT INTO table1 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

cursor.execute('SELECT * FROM table1')
result = cursor.fetchall()
for row in result:
    print(f"({row[0]}, {row[1]})")
# print(result)

connection.commit()

cursor.close()

connection.close()



