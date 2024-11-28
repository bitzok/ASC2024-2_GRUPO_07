#!/bin/bash

if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Entorno virtual creado"
fi

source venv/bin/activate

pip install --upgrade pip==22.0.4
pip install --upgrade setuptools==58.1.0

pip install -r requirements.txt

echo "Instalación completada"
