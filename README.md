![Alt](https://repobeats.axiom.co/api/embed/e642ea350cb1f8a87055bdce821432ae2f4ba9f9.svg "Repobeats analytics image")

# 🚀 FastAPI Learning Journey: From Basics to Mastery

Welcome to my **FastAPI Learning Project**! This repository tracks my journey as I explore and master web development with [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

---

## 🏗️ Project Overview

This is an ongoing project where I document my progress, starting with basic "Hello World" endpoints and gradually building up to complex API structures, database integrations, and authentication patterns.

### 🎯 Current Progress
- [x] **Getting Started**: Basic installation and "Hello World" implementation.
- [x] **Path & Query Parameters**: BMI Calculator endpoint with logic.
- [x] **Request Body & Models**: Using Pydantic for Student data validation.
- [x] **CRUD Operations**: Complete RESTful API for Student management.
- [ ] **Database Integration**: Connecting with SQLAlchemy.

---

## 🛠️ Stack & Technologies

- **Language:** [Python 3.8+](https://www.python.org/)
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Data Validation:** [Pydantic](https://docs.pydantic.dev/)
- **Server:** [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- **Documentation:** Built-in Swagger UI and ReDoc.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed. You can check this by running:
```bash
python --version
```

### 2. Installation
Install the necessary dependencies:
```bash
pip install fastapi uvicorn pydantic
```

### 3. Running the Apps

#### A. Basic "Hello World" & BMI Calculator
```bash
python -m uvicorn Getting_Started.Hello:app --reload
```
- **New Feature:** Test the BMI calculator at `/calculate_bmi?weight=70&height=1.75`

#### B. RESTful Student API (CRUD)
```bash
python -m uvicorn RestFul.main:app --reload
```
- **Features:** Full GET, POST, PUT, DELETE operations for student records.

---

## 📂 Project Structure

```text
Starting-FastAPI/
├── Getting_Started/
│   ├── Hello.py        # Initial API + BMI Calculator
│   └── __pycache__/    # Compiled python files
├── RestFul/
│   └── main.py         # Students CRUD API (RESTful)
├── README.md           # Project documentation
└── .git/               # Git repository configuration
```

---

## 🛡️ Documentation & Testing

FastAPI automatically generates interactive documentation for your API. Once the server is running, you can test endpoints directly in your browser using the Swagger UI at `/docs`.

---

## 📈 Learning Roadmap
- [ ] Error handling + validation
- [ ] JWT Authentication
- [ ] Dependency Injection
- [ ] Middleware & CORS
- [ ] Testing with Pytest

---

## 📬 Contact & Feedback

If you have any suggestions or just want to follow my progress, feel free to reach out or star this repository!

---
*Happy Coding!* 🐍✨
