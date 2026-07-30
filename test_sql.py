import sqlite3
import os

# Remove old database if it exists
if os.path.exists("CollegeDB.db"):
    os.remove("CollegeDB.db")

# Create database
conn = sqlite3.connect("CollegeDB.db")
cursor = conn.cursor()

# Read student's SQL file
with open("college.sql", "r") as f:
    sql = f.read()

# Execute SQL
cursor.executescript(sql)

# Check if Department table exists
cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
AND name='Department';
""")

table = cursor.fetchone()

assert table is not None, "Department table was not created."

# Check columns
cursor.execute("PRAGMA table_info(Department);")
columns = cursor.fetchall()

expected = [
    ("DepartmentID", "INTEGER"),
    ("DepartmentName", "VARCHAR(20)"),
    ("HOD", "VARCHAR(20)")
]

actual = [(c[1], c[2].upper()) for c in columns]

assert actual[0][0] == expected[0][0]
assert actual[1][0] == expected[1][0]
assert actual[2][0] == expected[2][0]

print("All tests passed.")
