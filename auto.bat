@echo off
call auto-commit.bat
call py readme.py
call git push -u origin main
pause