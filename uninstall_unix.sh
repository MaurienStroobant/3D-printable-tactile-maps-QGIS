#!/bin/bash
# ============================================================
# Tactiele Kaarten QGIS - Deïnstallatie (Linux/Mac)
# ============================================================

echo ""
echo "========================================"
echo "  Tactiele Kaarten QGIS Deïnstallatie"
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
    echo "Niets te deïnstalleren."
    exit 1
fi

echo "[INFO] QGIS profiel: $QGIS_PROFILE"
echo ""

# Verwijder Python script
SCRIPT="$QGIS_PROFILE/processing/scripts/text_and_braille_algorithm.py"
if [ -f "$SCRIPT" ]; then
    rm "$SCRIPT"
    echo "[OK] Python script verwijderd"
else
    echo "[INFO] Python script niet gevonden (al verwijderd?)"
fi

# Verwijder models
MODEL1="$QGIS_PROFILE/processing/models/Model.model"
MODEL2="$QGIS_PROFILE/processing/models/Model.model3"

if [ -f "$MODEL1" ]; then
    rm "$MODEL1"
    echo "[OK] Model.model verwijderd"
else
    echo "[INFO] Model.model niet gevonden"
fi

if [ -f "$MODEL2" ]; then
    rm "$MODEL2"
    echo "[OK] Model.model3 verwijderd"
else
    echo "[INFO] Model.model3 niet gevonden"
fi

# Verwijder stijlbestanden directory
STYLES_DIR="$QGIS_PROFILE/styles/tactile-maps"
if [ -d "$STYLES_DIR" ]; then
    rm -rf "$STYLES_DIR"
    echo "[OK] Stijlbestanden directory verwijderd"
else
    echo "[INFO] Stijlbestanden directory niet gevonden"
fi

echo ""
echo "========================================"
echo "  Deïnstallatie Compleet!"
echo "========================================"
echo ""
echo "Alle tactiele kaarten bestanden zijn verwijderd."
echo ""
echo "⚠️  BELANGRIJK: Herstart QGIS om de wijzigingen door te voeren!"
echo ""
