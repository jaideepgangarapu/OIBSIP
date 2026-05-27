@echo off
cd /d "%~dp0"
where py >nul 2>&1
if %errorlevel%==0 (
    py -3 -m pip install -e .
) else (
    python -m pip install -e .
)
echo.
echo Installed. You can now run:
echo     mini-voice-assistant
echo from any folder.
pause
