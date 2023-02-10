from pymysql import Connection

db = Connection(host='localhost', user='root', password='', database='demo')
cursor = db.cursor()

# cursor.execute("""
# Insert into users values(4, 'Eric', 'Sambo', 22, 'eric@gmail.com')
# """)
# db.commit()

# db.close()

cursor.execute("""
select * from users where age > 22
""")
result = cursor.fetchall()

for i in result:
    print('id ' + str(i[0]))
    print(f'first name is {i[1]}')
    print(f'last name is {i[2]}')
    print(f'age is {i[3]}')
    print(f'email is {i[4]}')

db.close()