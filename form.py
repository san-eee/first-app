from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll TEXT,
        dept TEXT,
        year TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json

    name = data['name']
    roll = data['roll']
    dept = data['dept']
    year = data['year']

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (name, roll, dept, year)
        VALUES (?, ?, ?, ?)
    """, (name, roll, dept, year))

    conn.commit()
    conn.close()

    return jsonify({"status": "saved"})

if __name__ == "__main__":
    app.run(debug=True)
    from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")
import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
