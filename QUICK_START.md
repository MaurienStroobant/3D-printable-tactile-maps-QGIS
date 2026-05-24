# Snelstart Gids - Tactiele Kaarten QGIS

**Snel aan de slag in 5 stappen**

## Voordat je Begint

✅ QGIS 3.28+ geïnstalleerd  
✅ **STL Generator Plugin** geïnstalleerd (Plugins → Manage and Install Plugins → "STL Generator")  
✅ Geodata beschikbaar

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

---

## Eerste Kaart Maken (10 minuten)

### 1. Data Voorbereiden - BELANGRIJK!

**Belangrijke STAP - Lees dit goed!**

1. **Laad je data in QGIS**
   - Voeg je vector lagen toe (gebouwen, wegen, etc.)

2. **Controleer CRS van je basislaag:**
   - Rechterklik op je hoofdlaag → Properties → Information
   - Kijk naar "CRS" 
   - **MOET metrisch zijn!** (bijv. EPSG:31370, EPSG:28992)
   - ❌ **NIET** EPSG:4326 (WGS84) - dat is in graden

3. **Stel Project CRS in op DEZELFDE als je basislaag:**
   - Klik rechtsonder in QGIS op het CRS (bijv. "EPSG:4326")
   - Selecteer **exact dezelfde CRS** als je basislaag
   - **Waarom?** Anders krijg je vervormingen in je kaart

**Voorbeeld:**
```
Basislaag CRS: EPSG:31370 (Lambert 72)
→ Stel Project CRS in op: EPSG:31370

NIET:
Basislaag: EPSG:31370
Project: EPSG:4326  ← Dit geeft vervormingen!
```

### 2. Model Uitvoeren

1. **Open het model:**
   - Ga naar menu → **Processing** → **Toolbox**
   - Vouw **Models** uit
   - Dubbelklik op je model

2. **Vul parameters in:**
   - **Basislaag**: je polygoonlaag
   - **Lijnlaag** (optioneel): wegen, rivieren
   - **Puntlaag** (optioneel): POI's
   - **Stijlen**: klik op **...** en navigeer naar de `styles/` map
   - **Tekst**: voeg labels toe (wordt automatisch naar braille geconverteerd)

3. **Klik RUN**
   - Wacht tot processing klaar is
   - Het model exporteert automatisch naar STL via de STL Generator plugin
   - ✅ Je krijgt een .stl bestand!

### 3. STL Controleren

**Het model doet de STL export automatisch** - jij hoeft niks te doen met de STL Generator!

1. Open het gegenereerde STL bestand in een viewer:
   - Gratis tools: MeshLab, Windows 3D Viewer, Blender
   - Online: viewstl.com

2. Controleer:
   - ✅ Gesloten geometrie (geen gaten)
   - ✅ Binnen printbed grootte
   - ✅ Braille punten zijn zichtbaar

### 4. 3D Printen

**Let op bij schalen:**
- Als je het model schaalt om op je printbed te passen:
  -  **Schaal alleen X en Y** (bijvoorbeeld 80%)
  -  **Laat Z op 100%** (anders worden braille punten te laag)
  - **Gebruik "non-uniform scaling"** in je slicer

**Aanbevolen print-technieken:**
- 🔗 Gebruik **zwaluwstaartverbindingen** als je kaart te groot is voor één print
- 📐 Dit maakt het mogelijk om meerdere delen stevig aan elkaar te bevestigen


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

---

## Problemen?

### Script Verschijnt Niet
- Herstart QGIS of klik Refresh in Processing Toolbox (🔄 icoon)
- Check dat bestand in juiste map staat (zie locaties hierboven)

### Model Verschijnt Niet in Processing Toolbox
- Klik op het **Refresh** icoon (🔄) bovenaan de Processing Toolbox
- Of: ga naar **Processing** → **Toolbox** → klik rechts bovenaan op 🔄

### Model Laadt Niet
- **QGIS 3.28-3.38**: gebruik `Model.model3`
- **QGIS 3.40+**: gebruik `Model.model`

### CRS Errors / Vervormingen
- **Controleer:**
  1. Is je basislaag in een metrisch CRS? (EPSG:31370, EPSG:28992, etc.)
  2. Is je Project CRS **exact hetzelfde** als je basislaag?
- **NOOIT gebruiken:** EPSG:4326 (WGS84) - dit is in graden, niet meters!

### STL Export Faalt
- Controleer dat **STL Generator plugin** geïnstalleerd is
- Het model gebruikt deze plugin automatisch


## Meer Info

- **Volledige handleiding**: `docs/user_guide.md`
- **Installatie details**: `docs/installation.md`
- **Stijlen uitleg**: `styles/STIJLEN.md`

---

**Succes met je tactiele kaarten!** 
