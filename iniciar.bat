@echo off

cls
call criar_ambiente
call .venv\Scripts\activate
python src\main.py
pause