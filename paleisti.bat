@echo off
echo ========================================
echo   Paveikslėlių analizės programa
echo ========================================
echo.

echo 1. Tikrinamas Python...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo KLAIDA: Python nerastas. Įdiekite Python iš python.org
    pause
    exit /b 1
)

echo.
echo 2. Tikrinami paketai...
python -c "import streamlit, ollama, PIL; print('Visi paketai įdiegti')"
if %ERRORLEVEL% NEQ 0 (
    echo Įdiegiami trūkstami paketai...
    pip install -r requirements.txt
)

echo.
echo 3. Paleidžiama programa...
echo Programa bus prieinama: http://localhost:8501
echo.
echo Norėdami sustabdyti programą, spauskite Ctrl+C
echo.

streamlit run app.py

pause