# 🐞 Bug Tracker

A simple yet powerful **bug tracking system** built with Django. This application allows users to create, manage, and track software bugs efficiently.

## 🚀 Features (MVP)

- ✅ **User Authentication** (Registration & Login)
- ✅ **Ticket Management** (Create, Edit, View, Delete)
- ✅ **Filtering & Sorting** (By status, priority)
- ✅ **User Roles & Permissions**
  - 👨‍💻 **Admin**: Full control over tickets & users
  - 🧑‍🔬 **Tester**: Can report bugs
  - 🛠️ **Developer**: Can update ticket status

---

## 📂 Project Structure

bug_tracker/
│── bug_tracker/ # Django project settings
│── tickets/ # Ticket management app
│── users/ # User authentication & roles
│── templates/ # HTML templates
│── static/ # CSS & JS files
│── db.sqlite3 # Database (SQLite by default)
│── manage.py # Django CLI tool
│── requirements.txt # Dependencies list
│── README.md # This file

## 🛠 Installation & Setup

### 1️⃣ **Clone the repository**

`git clone https://github.com/yourusername/bug_tracker.git`

`cd bug_tracker`

### 2️⃣ **Create & activate a virtual environment**

`python -m venv venv`

`source venv/bin/activate  # macOS/Linux `

`venv\Scripts\activate     # Windows`

### 3️⃣ Install dependencies

`pip install -r requirements.txt`

### 4️⃣ Apply database migrations

`python manage.py migrate`

### 5️⃣ **Create a superuser**

`python manage.py createsuperuser`

### 6️⃣ **Run the development server**

`python manage.py runserver `

### 7️⃣ **Access the app**

* Open: `http://127.0.0.1:8000/`
* Admin panel: `http://127.0.0.1:8000/admin/`

## 📌 Future Enhancements

* 📊 **Reports & Analytics**
* 📢 **Email Notifications**
* 🔗 **API for external integrations**
* 🎨 **Improved UI with React**

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

---

## 📜 License

This project is licensed under the  **MIT License** .
