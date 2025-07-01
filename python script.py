
import mysql.connector
import pandas as pd

#DB connection

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Pratu@0125',
    database = 'dev_db'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM employees WHERE department = 'IT'")
rows = cursor.fetchall()

#convert to Dataframe

df = pd.DataFrame(rows, columns = ['ID', 'Name', 'Department', 'Salary'])

#save to excel

df.to_excel("filtered_employees.xlsx", index = False)

print('Excel file saved successfully.')

cursor.close()
conn.close()