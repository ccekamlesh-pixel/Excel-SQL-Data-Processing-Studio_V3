@echo off
title Excel SQL Data Processing Studio
cd /d "%~dp0"

echo ============================================
echo  Excel SQL Data Processing Studio
echo ============================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo [1/2] Installing required packages...
pip install PySide6 duckdb pandas openpyxl sqlalchemy rapidfuzz --quiet
echo Done.
echo.

echo [2/2] Starting application...
echo.
python main.py

if errorlevel 1 (
    echo.
    echo ============================================
    echo  APPLICATION ERROR - See above for details
    echo ============================================
    pause
)
