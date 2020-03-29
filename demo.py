import psycopg2

connection = psycopg2.connect('dbname=example2')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (3,False))

cursor.execute('SELECT * from table2;')

result2 = cursor.fetchall()
print('fetchall ', result2)

result = cursor.fetchone()
print('fetchone ',result)

connection.commit()

connection.close()
cursor.close()