#!/bin/bash
# ============================================================
# Tactiele Kaarten QGIS - Automatische Installatie (Linux/Mac)
# ============================================================

set -e  # Stop bij fouten

echo ""
echo "========================================"
echo "  Tactiele Kaarten QGIS Installatie"
echo "========================================"
echo ""

# Detecteer OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    QGIS_PROFILE="$HOME/Library/Application Support/QGIS/QGIS3/profiles/default"
else
    # Linux
    QGIS_PROFILE="$HOME/.local/share/QGIS/QGIS3/profiles/default"
fi

# Controleer of QGIS profiel bestaat
if [ ! -d "$QGIS_PROFILE" ]; then
    echo "[FOUT] QGIS profiel directory niet gevonden!"
    echo ""
    echo "Verwachte locatie: $QGIS_PROFILE"
    echo ""
    echo "Zorg dat QGIS geïnstalleerd is en minstens één keer geopend is."
    exit 1
fi

echo "[OK] QGIS profiel gevonden: $QGIS_PROFILE"
echo ""

# Maak directories aan indien nodig
SCRIPTS_DIR="$QGIS_PROFILE/processing/scripts"
MODELS_DIR="$QGIS_PROFILE/processing/models"

mkdir -p "$SCRIPTS_DIR"
mkdir -p "$MODELS_DIR"

echo ""
echo "========================================"
echo "  1. Python script kopiëren"
echo "========================================"
echo ""

if [ -f "scripts/text_and_braille_algorithm.py" ]; then
    cp "scripts/text_and_braille_algorithm.py" "$SCRIPTS_DIR/"
    echo "[OK] Python script gekopieerd naar:"
    echo "    $SCRIPTS_DIR/text_and_braille_algorithm.py"
else
    echo "[FOUT] Script niet gevonden: scripts/text_and_braille_algorithm.py"
    echo "Zorg dat je dit script uitvoert vanuit de 3D-printable-tactile-maps-QGIS directory!"
    exit 1
fi

echo ""
echo "========================================"
echo "  2. QGIS models kopiëren"
echo "========================================"
echo ""

if [ -f "models/Model.model" ]; then
    cp "models/Model.model" "$MODELS_DIR/"
    echo "[OK] Model.model gekopieerd"
fi

if [ -f "models/Model.model3" ]; then
    cp "models/Model.model3" "$MODELS_DIR/"
    echo "[OK] Model.model3 gekopieerd"
fi

echo ""
echo "========================================"
echo "  3. Stijlbestanden locatie"
echo "========================================"
echo ""
echo "[INFO] Stijlbestanden blijven in: $(pwd)/styles"
echo ""
echo "Je kunt deze:"
echo "  A. Handmatig selecteren wanneer het model ernaar vraagt"
echo "  B. Importeren via QGIS Settings > Style Manager"
echo ""

echo ""
echo "========================================"
echo "  Installatie Compleet!"
echo "========================================"
echo ""
echo "Volgende stappen:"
echo "  1. Herstart QGIS (of klik Refresh in Processing Toolbox)"
echo "  2. Controleer of het script zichtbaar is:"
echo "     Processing Toolbox > Scripts > Tekst gereedschappen"
echo "  3. Open het model via:"
echo "     Processing Toolbox > Models of Model Designer"
echo ""
echo "Documentatie: docs/installation.md"
echo ""
