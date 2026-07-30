import sqlite3
import os
import pytest

# Remove old database
if os.path.exists("CollegeDB.db"):
    os.remove("CollegeDB.db")

conn = sqlite3.connect("CollegeDB.db")
cursor = conn.cursor()

# Read student's SQL file
with open("college.sql", "r") as file:
    sql = file.read()

# Execute SQL
try:
    cursor.executescript(sql)
except Exception as e:
    pytest.fail(f"SQL Execution Error:\n{e}")

# Check whether Department table exists
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

column_names = [c[1] for c in columns]

assert "DepartmentID" in column_names
assert "DepartmentName" in column_names
assert "HOD" in column_names

print("All tests passed.")
