import sqlite3

conn = sqlite3.connect('projects.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT
)
""")

cursor.execute("DELETE FROM projects")

cursor.execute("INSERT INTO projects (title, description) VALUES (?, ?)",
               ("MyLife Hub", "Personal dashboard web application"))

cursor.execute("INSERT INTO projects (title, description) VALUES (?, ?)",
               ("Campus Bites", "College canteen app with live preparation status"))

cursor.execute("INSERT INTO projects (title, description) VALUES (?, ?)",
               ("Portfolio Website", "Full-stack personal portfolio"))

cursor.execute("INSERT INTO projects (title, description) VALUES (?, ?)",
               ("Mini Python Tool", "Utility-based Python project"))

conn.commit()
conn.close()

print("Database ready!")
