from tabulate import tabulate
import mysql.connector

# Connect to MySQL server
con = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Prem@2277',
    database='python_db'  # Use 'python_db' instead of 'python.db'
)

# Perform database operations here...


if con:
    print(con)
    print('Connected')
else:
    print('Not connected')
3

def insert(name, age, city):
    res = con.cursor()
    sql = "insert into users (NAME, AGE, CITY) values (%s, %s, %s)"
    user = (name,age,city)
    res.execute(sql, user)
    con.commit()
    print('data insert successfully')


def update(id, name, age,city):
    res = con.cursor()
    sql = "update  users set name=%s, age=%s, city=%s where id=%s"
    user = (name, age, city,id)
    res.execute(sql, user)
    con.commit()
    print('data update successfully')


def select():
    res = con.cursor()
    sql = 'SELECT * FROM users;'
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result,headers=['ID', 'NAME', 'AGE', 'CITY']))


def delete(id):
    res = con.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print('data deleted successfully')


while True:
    print('1.insert data')
    print('2.update data')
    print('3.select data')
    print('4.delete data')
    print('5.exit program')
    choice = input('Enter your choice: ')
    if choice == '1':
        name = input('Enter your name: ')
        age = input('Enter your age: ')
        city = input('Enter your city: ')
        insert(name=name, age=age, city=city)
    elif choice == '2':
        id = input('Enter your id: ')
        name = input('Enter your name: ')
        age = input('Enter your age: ')
        city = input('Enter your city: ')
        update(id, name, age, city)
    elif choice == '3':
        select()
    elif choice == '4':
        id = input('Enter your id: ')
        delete(id)
    elif choice == '5':
        quit()
    else:
        print('Wrong input,enter correct input')
