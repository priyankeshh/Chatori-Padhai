@echo off
echo ========================================
echo    Evihian Launcher
echo ========================================
echo.

REM Check if we're in the right directory
if not exist "streamlit_app.py" (
    echo ERROR: streamlit_app.py not found!
    echo Please run this script from the AITutorAgent directory.
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please make sure your .env file with API keys is present.
    pause
    exit /b 1
)

echo Starting Evihian...
echo.
echo The app will open in your default browser.
echo Press Ctrl+C to stop the server.
echo.

REM Try different ports in case 8501 is busy
streamlit run streamlit_app.py --server.port 8501 --server.headless false
if errorlevel 1 (
    echo Port 8501 busy, trying 8502...
    streamlit run streamlit_app.py --server.port 8502 --server.headless false
)
if errorlevel 1 (
    echo Port 8502 busy, trying 8503...
    streamlit run streamlit_app.py --server.port 8503 --server.headless false
)

pause
