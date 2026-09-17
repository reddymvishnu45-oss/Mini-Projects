@echo off

echo Starting FastAPI...

start "FastAPI" cmd /k ".venv\Scripts\activate && python -m uvicorn backend.main:app --reload"

timeout /t 3 /nobreak > nul

echo Starting Streamlit...

start "Streamlit" cmd /k ".venv\Scripts\activate && streamlit run frontend/app.py"

echo.
echo FastAPI and Streamlit started!