@echo off

cls
call criar_ambiente
call .venv\Scripts\activate
python main.py
pause