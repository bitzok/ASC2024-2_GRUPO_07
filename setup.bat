@echo off

IF NOT EXIST "venv" (
    python -m venv venv
    echo Entorno virtual creado
)

call venv\Scripts\activate.bat

pip install --upgrade pip==22.0.4
pip install --upgrade setuptools==58.1.0

pip install -r requirements.txt

echo Instalación completada
pause
