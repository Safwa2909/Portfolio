from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

def get_projects():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    conn.close()
    return projects

@app.route('/')
def home():
    projects = get_projects()
    return render_template(
        'index.html',
        name="Safwa M",
        title="Web Developer",
        bio="Computer Science Engineering student passionate about building web applications and learning full-stack development.",
        email="safwa2909@gmail.com",
        linkedin="https://www.linkedin.com/in/safwa-m-230575338",
        skills=["HTML", "CSS", "JavaScript", "Python", "SQL", "Java"],
        projects=projects
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

