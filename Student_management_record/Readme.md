# Student Record Manager

Basic learning project using Streamlit + FastAPI + PostgreSQL + SQLAlchemy.

## 1. Create PostgreSQL database
Create a database named `project_db` in PostgreSQL.

## 2. Configure
Copy `.env.example` to `.env` and change the PostgreSQL username/password if needed.

## 3. Install
```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Run backend
From this project folder:
```bash
uvicorn backend.main:app --reload
```
API docs: http://127.0.0.1:8000/docs

## 5. Run Streamlit
Open another terminal in this project folder:
```bash
streamlit run frontend/app.py
```

## Learning flow
Streamlit form -> requests -> FastAPI -> Pydantic -> SQLAlchemy -> PostgreSQL.

The project intentionally stays basic so you can understand every layer.
