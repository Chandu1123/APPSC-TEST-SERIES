@echo off
title APPSC Test Series Website - Push to GitHub Pages
color 0B
echo ============================================================================
echo   APPSC GROUP-I ^& GROUP-II WEBSITE - PUSH TO GITHUB PAGES
echo   Target Repository: https://github.com/Chandu1123/APPSC-TEST-SERIES
echo   Live Website URL : https://chandu1123.github.io/APPSC-TEST-SERIES/
echo ============================================================================
echo.
cd /d "%~dp0"

echo [1/4] Checking Git repository status...
git status -s
echo.

echo [2/4] Staging all website files (index.html, data/tests_db.js, scripts, workflow)...
git add -A
git commit -m "Deploy APPSC Group 1 & 2 CBT Website (33+ Exams, Live PIB Scraper, GitHub Pages)" 2>nul
echo.

echo [3/4] Setting remote origin to https://github.com/Chandu1123/APPSC-TEST-SERIES.git ...
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/Chandu1123/APPSC-TEST-SERIES.git
echo.

echo [4/4] Pushing website to GitHub (A browser login window may pop up if needed)...
git push -u origin main --force

if %ERRORLEVEL% EQU 0 (
    color 0A
    echo.
    echo ============================================================================
    echo   SUCCESS! Your website code has been pushed to GitHub!
    echo.
    echo   FINAL STEP TO ACTIVATE YOUR LIVE WEBSITE:
    echo   1. Go to: https://github.com/Chandu1123/APPSC-TEST-SERIES/settings/pages
    echo   2. Under "Build and deployment" ^> "Branch", select "main" and "/ (root)"
    echo   3. Click Save. Your website will be live in 1 minute at:
    echo      https://chandu1123.github.io/APPSC-TEST-SERIES/
    echo ============================================================================
) else (
    color 0E
    echo.
    echo ============================================================================
    echo   NOTE: If git push asked for authentication or failed due to corporate proxy,
    echo   you can also upload via GitHub Desktop or drag-and-drop into:
    echo   https://github.com/Chandu1123/APPSC-TEST-SERIES
    echo ============================================================================
)
echo.
pause
