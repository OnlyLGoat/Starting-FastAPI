![Alt](https://repobeats.axiom.co/api/embed/e642ea350cb1f8a87055bdce821432ae2f4ba9f9.svg "Repobeats analytics image")

# 🚀 FastAPI Learning Journey: From Basics to Mastery

Welcome to my **FastAPI Learning Project**! This repository tracks my journey as I explore and master web development with [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

---

## 🏗️ Project Overview

This is an ongoing project where I document my progress, starting with basic "Hello World" endpoints and gradually building up to complex API structures, database integrations, and authentication patterns.

### 🎯 Current Progress
- [x] **Getting Started**: Basic installation and "Hello World" implementation.
- [ ] **Path & Query Parameters**: Handling user input.
- [ ] **Request Body & Models**: Using Pydantic for data validation.
- [ ] **CRUD Operations**: Building a complete API flow.
- [ ] **Database Integration**: Connecting with SQLAlchemy.

---

## 🛠️ Stack & Technologies

- **Language:** [Python 3.8+](https://www.python.org/)
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
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
pip install fastapi uvicorn
```

### 3. Running the "Hello World" App
To launch the initial API, navigate to the project root and run:
```bash
python -m uvicorn Getting_Started.Hello:app --reload
```

- **Interactive API Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative API Docs:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📂 Project Structure

```text
Starting-FastAPI/
├── Getting_Started/
│   ├── Hello.py        # Initial API implementation
│   └── __pycache__/    # Compiled python files
├── README.md           # Project documentation
└── .git/               # Git repository configuration
```

---

## 🛡️ Documentation & Testing

FastAPI automatically generates interactive documentation for your API. Once the server is running, you can test endpoints directly in your browser using the Swagger UI at `/docs`.

---

## 📈 Learning Roadmap
- [ ] Dependency Injection
- [ ] Middleware & CORS
- [ ] JWT Authentication
- [ ] Testing with Pytest
- [ ] Deployment to Production

---

## 📬 Contact & Feedback

If you have any suggestions or just want to follow my progress, feel free to reach out or star this repository!

---
*Happy Coding!* 🐍✨
