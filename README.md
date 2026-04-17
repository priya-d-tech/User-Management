# 🚀 User Management Web Application

A modern **SaaS-style User Management System** built using **Flask, SQLite, HTML, CSS, and Chart.js**.
This application allows users to register, log in, and manage user data with a clean dashboard UI and analytics.

---

## 🌟 Features

### 🔐 Authentication

* User Registration (with password hashing)
* Secure Login system
* Session-based authentication
* Logout functionality

### 👥 User Management (CRUD)

* Add new users
* View all users
* Edit user details
* Delete users

### 📊 Dashboard Analytics

* Total users count
* Admin vs User distribution
* Interactive charts using Chart.js

### 🎨 Modern UI (SaaS Style)

* Sidebar navigation with icons
* Top navbar with logged-in username
* Clean card-based layout
* Responsive table design

### 🔔 Notifications

* Toast-style success and error messages using Flask flash system

### 🗄️ Database

* SQLite database integration

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Charts:** Chart.js
* **Authentication:** Werkzeug (password hashing)

---

## 📂 Project Structure

```
user_app/
│
├── app.py
├── users.db
├── requirements.txt
├── Procfile
│
├── static/
│   └── style.css
│
└── templates/
    ├── base.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── add_user.html
    ├── edit_user.html
    └── profile.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/priya-d-tech/User-Management.git
cd user_app
```

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🔑 Default Flow

1. Register a new user
2. Login with credentials
3. Access dashboard
4. Perform CRUD operations
5. View analytics & charts
6. Logout

---

## 🌐 Deployment

This project can be deployed using:

* Render (Recommended)
* Railway / Heroku alternatives

### Deployment Steps (Render)

1. Push code to GitHub
2. Create Web Service in Render
3. Add:

   * Build Command: `pip install -r requirements.txt`
   * Start Command: `gunicorn app:app`
4. Deploy 🚀

---

## 📌 Future Enhancements

* Role-based access control (Admin/User)
* REST API integration
* Pagination improvements
* Search functionality enhancements
* Dark mode (theme toggle)
* Email notifications
* PostgreSQL integration (production-ready DB)
* Timestamp tracking for user creation
---

## 👨‍💻 Author

Developed by *Priya Dharshini*
