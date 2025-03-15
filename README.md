# 📚 Library Management System

A Django-based Library Management System to manage books, users, and lending processes efficiently. The project is Dockerized for simplified deployment and consistent development environments.

---

## 🚀 Features
- **Django Framework**: Robust and scalable backend.
- **Dockerized**: Simplified deployment with Docker.
- **User Authentication**: Secure login for admins and members.
- **Book Management**: Add, update, and delete book records.
- **Lending Management**: Track borrowing, returns, and due dates.
- **Admin Dashboard**: Easy-to-use interface for managing library operations.

---

## 🐳 Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started) installed on your system.
- [Docker Compose](https://docs.docker.com/compose/) (optional but recommended).

### Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Build and Run with Docker**
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**
   - Open your browser and navigate to `http://localhost:8000`

4. **Create a Superuser** (for admin access)
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

---

## ⚙️ Project Structure
```
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── library_management
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── app
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── ...
└── README.md
```

---

## 🛠️ Usage
- **Admin Panel**: `http://localhost:8000/admin/`
- **User Dashboard**: Manage personal book records and borrowing status.
- **Book Management**: Add or remove books from the admin panel.

---

## 🧰 Technologies Used
- Python 3
- Django
- Docker & Docker Compose
- SQLite (default, can be configured for PostgreSQL or MySQL)

---

## 📝 Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact
For any inquiries or feedback, please contact gerashrey77@gmail.com.

