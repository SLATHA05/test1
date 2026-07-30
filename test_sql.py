import sqlite3
import os

def test_department_table():

    # Remove existing database
    if os.path.exists("CollegeDB.db"):
        os.remove("CollegeDB.db")

    conn = sqlite3.connect("CollegeDB.db")
    cursor = conn.cursor()

    # Read student's SQL
    with open("college.sql", "r") as f:
        sql = f.read()

    # Execute SQL
    cursor.executescript(sql)

    # Check table exists
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

    names = [c[1] for c in columns]

    assert "DepartmentID" in names
    assert "DepartmentName" in names
    assert "HOD" in names

    conn.close()
