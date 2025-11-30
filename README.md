# Auth API DevOps Project

This project is a simple user authentication API built with **Python (Flask)** and extended with a modern **Bootstrap-based frontend UI**.  
The application supports user registration, login, password change, deletion, and listing all users.  
The goal of this project is to demonstrate essential **DevOps practices**, including:

- Dockerization  
- Continuous Integration (CI)  
- Artifact creation  
- Automated Docker image build  
- Uploading the image to a public container registry  
- Using GitHub Actions to automate everything  

This project fulfills the requirements of the university DevOps assignment.

---

## 📌 Features

### 🔐 API Capabilities
- User registration  
- Secure password hashing (SHA-256)  
- Login authentication  
- Password change  
- User deletion  
- List all registered users  
- Lightweight JSON storage  

### 🎨 Frontend Capabilities
- Clean, modern Bootstrap 5 UI  
- Docker/Local runtime status badge  
- Real-time API response viewer  
- Responsive card-based layout  

---

## 📦 Technologies Used

| Category | Technology |
|---------|------------|
| Backend | Python 3.12, Flask |
| Frontend | HTML, CSS, Bootstrap 5, JavaScript |
| Testing | Pytest |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Registry | GitHub Container Registry (GHCR) |
| Storage | JSON file |

---

## 🚀 How to Run Locally (Python)

Create virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows PowerShell:**
```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m app.main
```

Open in browser:

👉 http://localhost:8080

---

## 🐳 How to Run with Docker

Build the image:

```bash
docker build -t auth-api-devops .
```

Run the container:

```bash
docker run -p 8080:8080 auth-api-devops
```

Then visit:

👉 http://localhost:8080

The UI will automatically detect that it is running inside Docker.

---

## 🧪 Running Tests

Tests are written using **pytest**.

Run manually:

```bash
pytest
```

The CI pipeline also creates an artifact:

```
pytest-report.txt
```

This file is uploaded in every pipeline run.

---

## 🔄 CI/CD Pipeline (GitHub Actions)

The project contains a full CI workflow located at:

```
.github/workflows/ci.yml
```

The pipeline performs:

### ✔ 1. Test Stage
- Install Python dependencies  
- Run pytest  
- Upload test report as an artifact  

### ✔ 2. Build & Push Stage
- Build Docker image using the project’s Dockerfile  
- Log in to GHCR  
- Push image automatically to a public registry:

```
ghcr.io/nemodamark/auth-api-devops:latest
```

This fully satisfies the assignment requirements of:
- test execution  
- artifact generation  
- Docker build  
- public Docker registry push  

---

## 📤 Public Docker Image

You can pull the image using:

```bash
docker pull ghcr.io/nemodamark/auth-api-devops:latest
```

---

## 🗂 Project Structure

```
auth-api-devops/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── storage.py
│   └── tests/
│       └── test_auth.py
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── users.json
├── Dockerfile
├── requirements.txt
└── .github/workflows/ci.yml
```

---

## 🧠 Assignment Requirement Mapping

| Requirement | Status |
|------------|--------|
| CI pipeline created | ✔ |
| Unit test executed in pipeline | ✔ |
| Artifact produced | ✔ |
| Docker image built | ✔ |
| Docker image pushed to public registry | ✔ |
| Dockerfile included | ✔ |
| Working application | ✔ |

All requirements of the university DevOps assignment are completed.

---

## 👤 Author

**Nemoda Márk Levente**  
2025 – DevOps University Assignment  
GitHub Profile: https://github.com/NemodaMark

---

## 🎉 Final Notes

This project demonstrates real DevOps CI/CD practices in a practical, understandable way.  
The automated GitHub Actions pipeline and Docker integration make this app fully production-ready.

