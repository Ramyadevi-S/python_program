import mysql.connector
import pandas as pd
conn = mysql.connector.connect(
    host="localhost",
    user="root",          
    password="root" )
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db") 

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    grade VARCHAR(10),
    city VARCHAR(255)
)
""")

cursor.execute("SELECT * FROM students")
fetched_data = cursor.fetchall()

df = pd.DataFrame(fetched_data, columns=["ID", "Name", "Age", "Grade", "City"])

excel_file = "student_data.xlsx"
df.to_excel(excel_file, index=False)
print("Data from Excel_File:")
df_from_excel = pd.read_excel(excel_file)
print(df_from_excel)

cursor.close()
conn.close()
