from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_conn():
    conn = sqlite3.connect('todolist.db')
    return conn

def create_table():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 task TEXT NOT NULL
                 )""")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    create_table()
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    task_count = len(tasks)
    conn.close()
    return render_template("index.html", tasks=tasks, task_count=task_count)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE id=?", (id,))
    task = c.fetchone()
    if request.method == 'POST':
        task_text = request.form['task']
        c.execute("UPDATE tasks SET task=? WHERE id=?", (task_text, id))
        conn.commit()
        return redirect('/')
    conn.close()
    return render_template("update.html", task=task)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query']
        conn = get_conn()
        c = conn.cursor()
        c.execute("SELECT * FROM tasks WHERE task LIKE ?", ('%' + search_query + '%',))
        tasks = c.fetchall()
        conn.close()
        return render_template("index.html", tasks=tasks)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
