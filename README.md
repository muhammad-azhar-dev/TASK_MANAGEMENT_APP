# 📋 Task Management System (FastAPI)

A robust **Task Management Application** built with FastAPI and SQLAlchemy. This project implements a secure multi-user environment where users can manage their own tasks with full CRUD (Create, Read, Update, Delete) capabilities.

---

## 🚀 Key Features

* **User Authentication:** Secure user registration and login system.
* **JWT Authorization:** Implements JSON Web Tokens (OAuth2 with Password flow) for session management.
* **Resource Protection:** Strict authorization logic ensuring users can **only** access, update, or delete tasks they created.
* **Database Migrations:** Managed via Alembic to handle schema changes without data loss.
* **Relational Database:** Powered by PostgreSQL for reliable data storage.

---

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Database:** [PostgreSQL](https://www.postgresql.org/)
* **Migration Tool:** [Alembic](https://alembic.sqlalchemy.org/)
* **Security:** Passlib (Bcrypt hashing), PyJWT

---

## 🛠️ Installation & Setup

Follow these steps to get your local development environment running.

### 1. Clone the Repository
```bash
git clone [https://github.com/muhammadazharshaikh/TASK_MANAGEMENT_APP.git](https://github.com/muhammadazharshaikh/TASK_MANAGEMENT_APP.git)
cd TASK_MANAGEMENT_APP
```

### 2. Set Up Virtual Environment
Creating a virtual environment keeps your project dependencies isolated.

```bash
# Create the virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
```

### 3. Install Required Packages
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## ⚙️ Environment Configuration

Create a `.env` file in the root directory and configure your PostgreSQL and Security settings:

```env
# Database Connection String
# Format: postgresql://username:password@localhost:5432/database_name
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/task_db

# JWT Security
SECRET_KEY=your_super_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🔄 Database Migrations (Alembic)

Use Alembic to sync your SQLAlchemy models with your PostgreSQL database:

```bash
# Generate the migration script
alembic revision --autogenerate -m "Initial migration"

# Apply the migration to the database
alembic upgrade head
```

---

## 🏃 Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

Once started, you can access the interactive API documentation at:
*   **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
*   **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---
