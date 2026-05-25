@echo off
REM ============================================================
REM Fix QGIS Model Paths - Simple Working Version
REM ============================================================

setlocal enabledelayedexpansion

echo.
echo ========================================
echo   Model Paden Aanpassen
echo ========================================
echo.

REM Get QGIS profile path
set "PROFILE_PATH=%APPDATA%\QGIS\QGIS3\profiles\default"

echo [INFO] QGIS profiel: %PROFILE_PATH%
echo [INFO] Nieuwe stijl locatie: %PROFILE_PATH%\styles\tactile-maps\
echo.

REM OLD PATH to replace
set "OLD_PATH=C:\Users\mauri\OneDrive - UGent\Masterproef\Stijlen\"

REM NEW PATH
set "NEW_PATH=%PROFILE_PATH%\styles\tactile-maps\"

REM Use PowerShell with proper escaping
echo [INFO] Processing Model.model...
powershell -Command "$content = Get-Content 'models\Model.model' -Raw; $content = $content -replace [regex]::Escape('C:\Users\mauri\OneDrive - UGent\Masterproef\Stijlen\'), '%NEW_PATH:\=\\%'; Set-Content 'models\Model.model' -Value $content -NoNewline"

if exist "models\Model.model" (
    findstr /C:"styles\tactile-maps" "models\Model.model" >nul
    if !ERRORLEVEL! EQU 0 (
        echo [OK] Model.model succesvol bijgewerkt
    ) else (
        echo [WARNING] Model.model mogelijk niet correct bijgewerkt
    )
)

echo.
echo [INFO] Processing Model.model3...
powershell -Command "$content = Get-Content 'models\Model.model3' -Raw; $content = $content -replace [regex]::Escape('C:\Users\mauri\OneDrive - UGent\Masterproef\Stijlen\'), '%NEW_PATH:\=\\%'; Set-Content 'models\Model.model3' -Value $content -NoNewline"

if exist "models\Model.model3" (
    findstr /C:"styles\tactile-maps" "models\Model.model3" >nul
    if !ERRORLEVEL! EQU 0 (
        echo [OK] Model.model3 succesvol bijgewerkt
    ) else (
        echo [WARNING] Model.model3 mogelijk niet correct bijgewerkt
    )
)

echo.
echo ========================================
echo   Paden Aangepast!
echo ========================================
echo.
echo Van: C:\Users\mauri\OneDrive - UGent\Masterproef\Stijlen\
echo Naar: %NEW_PATH%
echo.

endlocal
