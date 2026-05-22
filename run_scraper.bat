@echo off
setlocal enabledelayedexpansion

:: =====================================================================
::  Batch script to run scraper with automatic retry on rate limits (429)
:: =====================================================================

:loop
echo =====================================================================
echo  Running Kemenhub HubUD Scraper...
echo =====================================================================

:: Run the python scraper with a 6 second delay to be safe
python scraper.py --bandara UPG --category domestik --start 2020-01 --delay 6.0

if %errorlevel% neq 0 (
    echo.
    echo [WARNING] Scraper was rate limited (429) or encountered an error.
    echo Waiting 5 minutes (300 seconds) before retrying to let the IP block clear...
    echo.
    timeout /t 300 /nobreak
    goto loop
)

echo.
echo [OK] Scraping completed successfully!
pause
