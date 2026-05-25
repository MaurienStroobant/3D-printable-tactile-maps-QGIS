@echo off
REM ============================================================
REM Tactiele Kaarten QGIS - Automatische Installatie (Windows)
REM ============================================================

echo.
echo ========================================
echo   Tactiele Kaarten QGIS Installatie
echo ========================================
echo.

REM Zoek QGIS profiel directory
set "QGIS_PROFILE=%APPDATA%\QGIS\QGIS3\profiles\default"

if not exist "%QGIS_PROFILE%" (
    echo [FOUT] QGIS profiel directory niet gevonden!
    echo.
    echo Verwachte locatie: %QGIS_PROFILE%
    echo.
    echo Zorg dat QGIS geinstalleerd is en minstens een keer geopend is.
    pause
    exit /b 1
)

echo [OK] QGIS profiel gevonden: %QGIS_PROFILE%
echo.

REM Maak directories aan indien nodig
set "SCRIPTS_DIR=%QGIS_PROFILE%\processing\scripts"
set "MODELS_DIR=%QGIS_PROFILE%\processing\models"

if not exist "%SCRIPTS_DIR%" (
    echo [INFO] Scripts directory bestaat niet, wordt aangemaakt...
    mkdir "%SCRIPTS_DIR%"
)

if not exist "%MODELS_DIR%" (
    echo [INFO] Models directory bestaat niet, wordt aangemaakt...
    mkdir "%MODELS_DIR%"
)

echo.
echo ========================================
echo   1. Python script kopieren
echo ========================================
echo.

if exist "scripts\text_and_braille_algorithm.py" (
    copy /Y "scripts\text_and_braille_algorithm.py" "%SCRIPTS_DIR%\"
    if %ERRORLEVEL% EQU 0 (
        echo [OK] Python script gekopieerd naar:
        echo     %SCRIPTS_DIR%\text_and_braille_algorithm.py
    ) else (
        echo [FOUT] Kon script niet kopieren!
    )
) else (
    echo [FOUT] Script niet gevonden: scripts\text_and_braille_algorithm.py
    echo Zorg dat je dit script uitvoert vanuit de 3D-printable-tactile-maps-QGIS directory!
)

echo.
echo ========================================
echo   2. Model paden aanpassen
echo ========================================
echo.

REM Fix model paths BEFORE copying to QGIS
call fix_model_paths.bat
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Kon model paden niet automatisch aanpassen
    echo Models worden gekopieerd met originele paden
    pause
)

echo.
echo ========================================
echo   3. QGIS models kopieren
echo ========================================
echo.

if exist "models\Model.model" (
    copy /Y "models\Model.model" "%MODELS_DIR%\"
    echo [OK] Model.model gekopieerd
)

if exist "models\Model.model3" (
    copy /Y "models\Model.model3" "%MODELS_DIR%\"
    echo [OK] Model.model3 gekopieerd
)

echo.
echo ========================================
echo   4. Stijlbestanden kopieren
echo ========================================
echo.

REM Maak styles directory aan
set "STYLES_DIR=%QGIS_PROFILE%\styles\tactile-maps"

if not exist "%STYLES_DIR%" (
    echo [INFO] Styles directory bestaat niet, wordt aangemaakt...
    mkdir "%STYLES_DIR%"
)

REM Kopieer alle QML bestanden
if exist "styles\*.qml" (
    copy /Y "styles\*.qml" "%STYLES_DIR%\"
    if %ERRORLEVEL% EQU 0 (
        echo [OK] Alle stijlbestanden gekopieerd naar:
        echo     %STYLES_DIR%\
    ) else (
        echo [FOUT] Kon stijlbestanden niet kopieren!
    )
) else (
    echo [FOUT] Geen stijlbestanden gevonden in styles\ directory
)

echo.
echo ========================================
echo   Stijlbestanden locatie
echo ========================================
echo.
echo [INFO] Stijlbestanden zijn gekopieerd naar:
echo     %STYLES_DIR%\
echo.

echo.
echo ========================================
echo   Installatie Compleet!
echo ========================================
echo   Installatie Compleet!
echo ========================================
echo.
echo Volgende stappen:
echo   1. Herstart QGIS (of klik Refresh in Processing Toolbox)
echo   2. Controleer of het script zichtbaar is:
echo      Processing Toolbox ^> Scripts ^> Tekst gereedschappen
echo   3. Open het model via:
echo      Processing Toolbox ^> Models of Model Designer
echo.
echo Documentatie: docs\installation.md
echo.
pause
