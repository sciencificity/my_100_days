# 2020-03-15

import sqlite3
from day87_employee import Employee

# conn = sqlite3.connect(':memory:') # nice for testing

conn = sqlite3.connect('employee.db')

# create a cursor that allows us to execute SQL commands
c = conn.cursor()

# Now we can run employees tbl
# Commented out since we've already created the tbl
# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#             )""")
# conn.commit()

def insert_emp(emp):
    with conn: # manage setup and shutdown of resources
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
        {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", 
              {'last': lastname})
    return c.fetchall()

def get_emps_by_fname(firstname):
    c.execute("SELECT * FROM employees WHERE first=:first", 
              {'first': firstname})
    return c.fetchall()
    
def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
emp_3 = Employee('Corey', 'Schafer', 50000)
emp_4 = Employee('K', 'Schafer', 100000)



insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)
insert_emp(emp_4)

emps = get_emps_by_name('Doe')
print(emps)

c.execute('''
SELECT * FROM employees WHERE last like 'Sch%'
''')
# Gets the next row in our result
c.fetchone()
# Fetches the number specified as a list
c.fetchmany(5)

c.execute('''
SELECT * FROM employees WHERE last = :last
''', {'last': 'Doe'})
# Gets all rows in our result
c.fetchall()

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

get_emps_by_fname('Corey')

conn.close()

# Another db
conn = sqlite3.connect('Training.db')

# create a cursor that allows us to execute SQL commands
c = conn.cursor()


