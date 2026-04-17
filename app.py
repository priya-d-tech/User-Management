from flask import Flask, render_template, request, redirect, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import logging
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.secret_key = "secret123"

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)    

    conn.commit()
    conn.close()

init_db()

@app.route("/register", methods=["GET", "POST"])
def register():
    
    if request.method == "POST":
        username = request.form["username"]
        role = "admin" if username == "admin" else "user"
        password = generate_password_hash(request.form["password"])
       
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        #cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        cursor.execute(
         "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
         (username, password, role)
        )
        logging.info(
        f"Running query Register: INSERT INTO users (username, password, role) VALUES (?, ?, ?) "
        f"with values: {username}, {password}, {role}"
        )
        conn.commit()
        conn.close()

        flash("Registered successfully")
        return redirect("/")

    return render_template("register.html")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session["user"] = username
            return redirect("/dashboard")
        else:
            flash("Invalid login")

    return render_template("login.html")

"""@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    search = request.args.get("search")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    if search:
        cursor.execute("SELECT * FROM users WHERE username LIKE ?", ('%' + search + '%',))
    else:
        cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()
    conn.close()

    return render_template("dashboard.html", users=users)"""

@app.route("/dashboard")
def dashboard():
     if "user" not in session:
       redirect("/")
     page = int(request.args.get("page", 1))
     per_page = 5
     offset = (page - 1) * per_page
     conn = sqlite3.connect("users.db")
     cursor = conn.cursor()

     """cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?", (per_page, offset))
     users = cursor.fetchall()

     conn.close()

     return render_template("dashboard.html", users=users, page=page)"""
     cursor.execute("SELECT * FROM users")
     users = cursor.fetchall()

     cursor.execute("SELECT COUNT(*) FROM users")
     total_users = cursor.fetchone()[0]

     cursor.execute("SELECT COUNT(*) FROM users WHERE role='admin'")
     admin_count = cursor.fetchone()[0]

     cursor.execute("SELECT COUNT(*) FROM users WHERE role='user'")
     user_count = cursor.fetchone()[0]

     conn.close()

     return render_template(
        "dashboard.html",
        users=users,
        total_users=total_users,
        admin_count=admin_count,
        user_count=user_count
    )

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        flash("User added")
        return redirect("/dashboard")

    return render_template("add_user.html")

@app.route("/delete/<int:id>")
def delete(id):
    if session.get("user") != "admin":
     return "Access Denied"
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()

    flash("User deleted")
    return redirect("/dashboard")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    if request.method == "POST":
        username = request.form["username"]
        cursor.execute("UPDATE users SET username=? WHERE id=?", (username, id))
        conn.commit()
        conn.close()
        return redirect("/dashboard")

    cursor.execute("SELECT * FROM users WHERE id=?", (id,))
    user = cursor.fetchone()
    conn.close()

    return render_template("edit_user.html", user=user)
    
@app.route("/profile")
def profile():
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=?", (session["user"],))
            user = cursor.fetchone()
            if "user" not in session:
              return redirect("/")
              conn.close()
            return render_template("profile.html", user=user)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run()