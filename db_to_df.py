import mysql.connector
import pandas as pd

# Step 1: Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root",           # Replace with your MySQL username
    password="root" )
cursor = conn.cursor()

# Step 2: Create Database (Only if it doesn't exist)
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")  # Select the database

# Step 3: Create Table (Only if it doesn't exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    grade VARCHAR(10),
    city VARCHAR(255)
)
""")

# Step 4: Insert Student Data


# Step 5: Fetch Data from MySQL
cursor.execute("SELECT * FROM students")
fetched_data = cursor.fetchall()

# Step 6: Convert Fetched Data to DataFrame
df = pd.DataFrame(fetched_data, columns=["ID", "Name", "Age", "Grade", "City"])

# Step 7: Save Data to Excel File
excel_file = "student_data.xlsx"
df.to_excel(excel_file, index=False)

# Step 8: Read and Print Data from Excel File
print("Data from Excel File:")
df_from_excel = pd.read_excel(excel_file)
print(df_from_excel)

# Close Connection
cursor.close()
conn.close()
