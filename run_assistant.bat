@echo off
cd /d "%~dp0"
where py >nul 2>&1
if %errorlevel%==0 (
    py -3 voice_assist.py
) else (
    python voice_assist.py
)
pause
