@echo off

cls
echo Configurando Ambiente...
python -m venv .venv
call .venv\Scripts\activate
echo Verificando dependencias...
python -m pip install -U -q pip
pip install -U -q -r requirements.txt