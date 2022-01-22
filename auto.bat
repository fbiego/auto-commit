@echo off
auto-commit.bat
::auto-commit.py
py readme.py
git push -u origin main
pause