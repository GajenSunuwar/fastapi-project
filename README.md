## ⚠️ Work in Progress

This project is still under active development.  
Features like authentication, additional routes, and more comprehensive test coverage are being added step by step.  
Stay tuned for updates 🚀

# FastAPI Project

A simple FastAPI application with user management (sign up, authentication, etc.) and a testing setup using **pytest** and **SQLAlchemy**.

---

## 🚀 Features
- FastAPI backend with modular `app/` structure
- PostgreSQL database (SQLAlchemy ORM)
- User registration endpoint
- Password hashing with Passlib
- Testing setup with a dedicated **test database**
- Environment variables support via `.env`

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/gajensunuwar/fastapi-project.git
cd fastapi-project
```
### 2. Create a virtual environment
```bash
python -m venv venv
# Activate
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
``` 
### 4. Set up environment variables
Create a `.env` file in the root directory with the following content:
```plaintext
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=yourpassword
DATABASE_NAME=fastapi
DATABASE_USERNAME=yourusername
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
### 5. For tests, you can configure a separate test database:
```plaintext
TEST_DATABASE_HOSTNAME=localhost
```

### 6. Run the application
```bash
uvicorn app.main:app --reload
```
### 7. Run tests
```bash
pytest
```
