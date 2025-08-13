@echo off

cls
python -m venv .venv
call .venv\Scripts\activate
python -m pip install -U -q pip
pip install -U -q -r requirements.txt