pip install pandasql

import pandas as pd
from pandasql import sqldf


file = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Music\\sample_-_superstore.csv", encoding='windows-1252')
file.info()
file.isnull()
print(file.isnull())
file.describe()
print(file.describe())


q2 = "SELECT avg(profit),State from file group by State"
r2 = sqldf(q2, globals())
print(r2)
print("\n")  # Adds a blank line

""" #*************************************ISSUE******************************
q3 = 'SELECT MONTH("Order Date") AS month, SUM(Sales) AS total_sales FROM Sales GROUP BY MONTH("Order Date")'
r3 = sqldf(q3, globals())
print(r3)
print("\n")  # Adds a blank line

q10 = "SELECT count(Sub-Category),Category from file group by Category"
r10 = sqldf(q10, globals())      r10 = sqldf(q10, globals())      
print(r10)

 (sqlite3.OperationalError) no such column: Sub
[SQL: SELECT count(Sub-Category),Category from file group by Category] """



q2 = "SELECT avg(profit),State from file group by State"
r2 = sqldf(q2, globals())
print(r2)
print("\n")  # Adds a blank line

q12 = "SELECT sum(Sales),State from file group by State"
r12 = sqldf(q12, globals())
print(r12)
print("\n")  # Adds a blank line

q1 = "SELECT avg(profit),Category from file group by Category"
r1 = sqldf(q1, globals())
print(r1)
print("\n")  # Adds a blank line

q9 = "SELECT sum(Quantity),Category from file group by Category"
r9 = sqldf(q9, globals())
print(r9)
print("\n")  # Adds a blank line
 


q4 = "SELECT avg(Sales),city from file group by city"
r4 = sqldf(q4, globals())
print(r4)
print("\n")  # Adds a blank line

q5 = "SELECT sum(Sales),city from file group by city"
r5 = sqldf(q5, globals())
print(r5)
print("\n")  # Adds a blank line


q7="select avg(profit),city from file group by city"
r7=sqldf(q7,globals())
print(r7)
q6 = "SELECT sum(Sales),Segment from file group by Segment"
r6 = sqldf(q6, globals())
print(r6)
print("\n")  # Adds a blank line

q8="select count(category),segment from file group by segment"
r8=sqldf(q8,globals())
print(r8)

q11 = 'select sum(sales) as total_sales, "product name", avg(profit) as average_profit from file group by "product name"'
r11 = sqldf(q11, globals())
print(r11)
print(file.shape)
