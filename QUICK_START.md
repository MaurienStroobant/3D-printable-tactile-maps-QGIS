# Snelstart Gids - Tactiele Kaarten QGIS

⚡ **Snel aan de slag in 5 stappen**

## Voordat je Begint

✅ QGIS 3.28+ geïnstalleerd  
✅ Geodata in **metrisch** coördinatensysteem (bijv. EPSG:31370 voor België)

## Installatie (5 minuten)

### Windows
1. Pak `3D-printable-tactile-maps-QGIS.zip` uit
2. Dubbelklik `install_windows.bat`
3. Herstart QGIS

### Mac/Linux
1. Pak `3D-printable-tactile-maps-QGIS.zip` uit
2. Open Terminal in de uitgepakte map
3. Run: `./install_unix.sh`
4. Herstart QGIS

### Handmatig (alle platforms)
Kopieer naar je QGIS profiel map:
- `scripts/text_and_braille_algorithm.py` → `[profiel]/processing/scripts/`
- `models/Model.model*` → `[profiel]/processing/models/`

**QGIS profiel locaties:**
- Windows: `%APPDATA%\QGIS\QGIS3\profiles\default`
- Mac: `~/Library/Application Support/QGIS/QGIS3/profiles/default`
- Linux: `~/.local/share/QGIS/QGIS3/profiles/default`

## Eerste Kaart Maken (10 minuten)

### 1. Nieuw Project
- Open QGIS
- Stel Project CRS in op **metrisch** (bijv. EPSG:31370)

### 2. Data Toevoegen
- Sleep je vector data (gebouwen, wegen, etc.) naar QGIS
- Controleer dat CRS metrisch is (rechterklik laag → Properties → Information)

### 3. Model Uitvoeren
- Open **Processing Toolbox** (Ctrl+Alt+T)
- Vind je model onder **Models**
- Dubbelklik om te openen
- Vul parameters in:
  - **Basislaag**: je polygoonlaag
  - **Stijlen**: selecteer uit `styles/` folder
  - **Tekst**: voeg labels toe (wordt automatisch naar braille geconverteerd)
- Klik **Run**

### 4. Export naar STL
- Installeer **STL Generator** plugin (Plugins → Manage and Install)
- Rechterklik op output laag → **Generate STL**
- Stel parameters in:
  - Z-scale: 2.0 (voor reliëf)
  - Base height: 3mm
- Save als .stl

### 5. 3D Printen
- Open STL in viewer (MeshLab, 3D Builder, etc.)
- Controleer op errors
- Print met PLA, 0.2mm layer height

## Belangrijkste Bestanden

```
3D-printable-tactile-maps-QGIS/
├── models/
│   ├── Model.model      # Voor QGIS 3.40+
│   └── Model.model3     # Voor QGIS 3.28-3.38
├── scripts/
│   └── text_and_braille_algorithm.py  # Braille generator
├── styles/
│   ├── stijl_basislaag.qml
│   ├── Stijl_lijnlaag.qml
│   ├── Stijl_puntlaag.qml
│   └── ... (13 stijlbestanden)
└── docs/
    ├── installation.md   # Gedetailleerde installatie
    └── user_guide.md     # Volledige handleiding
```

## 🆘 Problemen?

### Script Verschijnt Niet
- Herstart QGIS of klik Refresh in Processing Toolbox
- Check dat bestand in juiste map staat (zie locaties hierboven)

### Model Laadt Niet
- Gebruik `Model.model3` voor QGIS 3.28-3.38
- Gebruik `Model.model` voor QGIS 3.40+

### CRS Errors
- **BELANGRIJK**: Gebruik altijd metrisch CRS!
- ❌ NIET: EPSG:4326 (graden)
- ✅ WEL: EPSG:31370 (België), EPSG:28992 (Nederland)

### Stijlen Werken Niet
- Navigeer handmatig naar `styles/` folder bij eerste gebruik
- OF: importeer stijlen via Settings → Style Manager

## 📚 Meer Info

- **Volledige handleiding**: `docs/user_guide.md`
- **Installatie details**: `docs/installation.md`
- **Stijlen uitleg**: `styles/STIJLEN.md`

## ⚙️ Aanbevolen Instellingen

### QGIS Project
- **CRS**: Metrisch (bijv. EPSG:31370)
- **Units**: Meters

### Braille Parameters
- **Lettergrootte**: 72pt
- **Layout**: Braille boven tekst
- **Puntdiameter**: 1.5mm (standaard, niet wijzigen!)

### STL Export
- **Z-scale**: 1.5 - 3.0
- **Base height**: 2-5mm
- **Model spacing**: 0.5-1.0mm

### 3D Print
- **Materiaal**: PLA of PETG
- **Layer height**: 0.2-0.3mm
- **Infill**: 20-30%
- **Supports**: Minimaal

## 🎯 Volgende Stappen

1. ✅ Maak je eerste test-kaart (klein gebied!)
2. 📖 Lees de volledige handleiding
3. 🧪 Experimenteer met verschillende stijlen
4. 🖨️ Print een test op kleine schaal
5. 🔧 Verfijn en optimaliseer

**Succes met je tactiele kaarten!** 🗺️✨
