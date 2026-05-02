# 🚀 AI-Powered Attendance Management System

An intelligent **face recognition-based attendance system** built using **FastAPI, InsightFace, MySQL, and React**.
This system automates attendance marking by identifying users through facial embeddings.

---

## 📌 Features

- 🔐 Face Recognition-based Authentication
- 👤 User Registration with Image Upload
- 🧠 AI Embedding Generation using InsightFace
- 📊 Attendance Tracking & Management
- ⚡ FastAPI Backend with REST APIs
- 🗄️ MySQL Database Integration
- 🌐 React Frontend (planned / in progress)

---

## 🧱 Tech Stack

### Backend

- FastAPI
- Python 3.10
- InsightFace (ONNX)
- OpenCV
- SQLAlchemy
- MySQL

### Frontend

- React.js (Vite)
- Tailwind CSS (planned)

### Tools

- Git & GitHub
- VS Code
- Docker (optional / future)

---

## 🏗️ Project Structure

```
Attendance Management system/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── ai/
│   │   ├── train.py
│   │   └── recognize.py
│   ├── routes/
│   │   ├── users.py
│   │   ├── attendance.py
│   │   └── auth.py
│
├── frontend/
│   └── (React app)
│
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone the repository

```bash
git clone https://github.com/Govind1732/attendence-management-system.git
cd attendance-management-system
```

---

### 🔹 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

---

### 🔹 3. Configure MySQL

- Create database:

```sql
CREATE DATABASE attendance_system;
```

- Update connection in `database.py`:

```python
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/attendance_system"
```

---

### 🔹 4. Run Backend

```bash
uvicorn main:app --reload
```

👉 Open API Docs:
http://127.0.0.1:8000/docs

---

## 🤖 How It Works

### 🔹 User Registration

1. Upload user image
2. Extract facial embedding using InsightFace
3. Store embedding in MySQL

---

### 🔹 Face Recognition

1. Upload image
2. Extract embedding
3. Compare with stored embeddings
4. Identify user

---

### 🔹 Attendance Marking

- Automatically logs attendance if match found
- Prevents duplicate entries (same day)

---

## 📡 API Endpoints

### 👤 Users

- `POST /users/register` → Register user with image

### 🧾 Attendance

- `POST /attendance/recognize` → Recognize & mark attendance

---

## 🧠 Core Concept

```
Image → Face Embedding → Store → Compare → Match
```

---

## ⚠️ Current Limitations

- No authentication (JWT) yet
- Embeddings stored as string (can be optimized to JSON)
- CPU-based inference (no GPU acceleration)

---

## 🚀 Future Improvements

- 🔐 JWT Authentication
- 📊 Attendance Analytics Dashboard
- 🎥 Real-time Webcam Integration
- 🐳 Docker Deployment
- ☁️ Cloud Hosting (AWS / GCP)
- ⚡ GPU acceleration support

---

## 🧪 Sample Workflow

1. Register user with image
2. Upload another image
3. System detects and marks attendance

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit pull requests.

---

## 📜 License

This project is for educational and personal use.

---

## 👨‍💻 Author

**Govind D**
Full Stack Developer | AI Enthusiast

---
