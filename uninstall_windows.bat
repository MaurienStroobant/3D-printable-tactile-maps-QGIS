@echo off
REM ============================================================
REM Tactiele Kaarten QGIS - Deïnstallatie (Windows)
REM ============================================================

echo.
echo ========================================
echo   Tactiele Kaarten QGIS Deïnstallatie
echo ========================================
echo.

REM QGIS profiel directory
set "QGIS_PROFILE=%APPDATA%\QGIS\QGIS3\profiles\default"

if not exist "%QGIS_PROFILE%" (
    echo [FOUT] QGIS profiel directory niet gevonden!
    echo Niets te deïnstalleren.
    pause
    exit /b 1
)

echo [INFO] QGIS profiel: %QGIS_PROFILE%
echo.

REM Verwijder Python script
set "SCRIPT=%QGIS_PROFILE%\processing\scripts\text_and_braille_algorithm.py"
if exist "%SCRIPT%" (
    del "%SCRIPT%"
    echo [OK] Python script verwijderd
) else (
    echo [INFO] Python script niet gevonden (al verwijderd?)
)

REM Verwijder models
set "MODEL1=%QGIS_PROFILE%\processing\models\Model.model"
set "MODEL2=%QGIS_PROFILE%\processing\models\Model.model3"

if exist "%MODEL1%" (
    del "%MODEL1%"
    echo [OK] Model.model verwijderd
) else (
    echo [INFO] Model.model niet gevonden
)

if exist "%MODEL2%" (
    del "%MODEL2%"
    echo [OK] Model.model3 verwijderd
) else (
    echo [INFO] Model.model3 niet gevonden
)

REM Verwijder stijlbestanden directory
set "STYLES_DIR=%QGIS_PROFILE%\styles\tactile-maps"
if exist "%STYLES_DIR%" (
    rmdir /S /Q "%STYLES_DIR%"
    echo [OK] Stijlbestanden directory verwijderd
) else (
    echo [INFO] Stijlbestanden directory niet gevonden
)

echo.
echo ========================================
echo   Deïnstallatie Compleet!
echo ========================================
echo.
echo Alle tactiele kaarten bestanden zijn verwijderd.
echo.
echo ⚠️  BELANGRIJK: Herstart QGIS om de wijzigingen door te voeren!
echo.
pause
