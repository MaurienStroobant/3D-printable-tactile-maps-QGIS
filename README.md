# Automatisch Stappenplan voor 3D-Printbare Tactiele Kaarten

[English version](#english-version)

Een geautomatiseerde workflow in QGIS voor het genereren van 3D-printbare tactiele kaarten, ontwikkeld als onderdeel van een thesis over toegankelijke cartografie.

## Overzicht

Dit project biedt een compleet QGIS-model voor het automatisch genereren van tactiele kaarten die geschikt zijn voor 3D-printing. Het combineert geografische data met braille-annotaties en stijlen om kaarten te produceren die tastbaar zijn voor mensen met een visuele beperking.

### Belangrijkste Features

- ✅ **Volledig geautomatiseerd QGIS-model** - van ruwe geodata tot printklaar STL-bestand
- ✅ **Braille en tekst combinatie** - custom Python-script voor het samenvoegen van braille en reguliere tekst
- ✅ **Voorgedefinieerde stijlen** - 13 QGIS-stijlbestanden (QML) voor consistente visualisatie
- ✅ **Metrisch coördinatensysteem** - optimaal voor 3D-printnauwkeurigheid

## Vereisten

### Software
- **QGIS 3.28 of hoger** (getest op QGIS 3.40.5 en 3.44.10)
  - QGIS 3.28-3.40: gebruik `Model.model3`
  - QGIS 3.44+: gebruik `Model.model`
- **STL Generator Plugin** (voor finale 3D-export)

### Data Vereisten
- Geodata in een **metrisch coördinatensysteem** (bijv. EPSG:31370 voor België, EPSG:28992 voor Nederland)
- Project CRS moet **identiek** zijn aan de CRS van de basislaag om vervormingen te voorkomen

## Installatie

### Stap 1: Repository Downloaden

```bash
git clone https://github.com/MaurienStroobant/3D-printable-tactile-maps-QGIS.git
cd 3D-printable-tactile-maps-QGIS
```

Of download als ZIP via de groene "Code" knop → "Download ZIP"

### Stap 2: QGIS Model Importeren

1. Open QGIS
2. Ga naar **Processing** → **Model Designer**
3. Klik op **Open Model** (map-icoon)
4. Selecteer:
   - `models/Model.model` (QGIS 3.44+)
   - `models/Model.model3` (QGIS 3.28-3.40)

### Stap 3: Python Script Installeren

Het braille-script moet in de QGIS Processing scripts map geplaatst worden:

**Windows:**
```
C:\Users\<jouw-naam>\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\
```

**macOS/Linux:**
```
~/.local/share/QGIS/QGIS3/profiles/default/processing/scripts/
```

**Installatie stappen:**
1. Kopieer `scripts/text_and_braille_algorithm.py` naar bovenstaande locatie
2. Herstart QGIS of klik op **Refresh** in de Processing Toolbox
3. Het script verschijnt onder **Scripts** → **Tekst gereedschappen** → **Tekst en Braille combineren**

### Stap 4: Stijlbestanden Klaarzetten

De stijlbestanden in de `styles/` map moeten toegepast worden tijdens het gebruik van het model. Er zijn twee opties:

#### Optie A: Handmatig toepassen
1. Wanneer het model vraagt om een stijl te selecteren
2. Navigeer naar de `styles/` map in deze repository
3. Selecteer het juiste `.qml` bestand

#### Optie B: Stijlen importeren in QGIS (aanbevolen)
1. Ga naar **Settings** → **Style Manager**
2. Importeer alle stijlen uit de `styles/` map
3. De stijlen zijn nu beschikbaar in alle projecten

### Stap 5: STL Generator Plugin

1. Ga naar **Plugins** → **Manage and Install Plugins**
2. Zoek naar **"STL Generator"**
3. Klik op **Install Plugin**

## Gebruik

### Basis Workflow

1. **Open het model** in Processing Model Designer
2. **Stel je basislaag in** (moet in metrisch CRS zijn!)
3. **Controleer Project CRS** - moet overeenkomen met basislaag CRS
4. **Voer het model uit**:
   - Selecteer je input lagen (polygonen, lijnen, punten)
   - Kies de juiste stijlen uit de `styles/` map
   - Voeg tekst/labels toe (wordt automatisch naar braille geconverteerd)
5. **Export naar STL** met de STL Generator plugin

### Belangrijke Parameters

| Parameter | Beschrijving | Voorbeeld |
|-----------|--------------|-----------|
| Basislaag | Hoofdpolygoonlaag | Gebouwen, landgebruik |
| Lijnlaag | Wegen, rivieren | Stratennetwerk |
| Puntlaag | POI's | Landmarks, voorzieningen |
| Project CRS | Moet metrisch zijn | EPSG:31370, EPSG:28992 |
| Tekstgrootte | Lettergrootte (pt) | 72 pt (standaard) |

### Stijlbestanden Overzicht

| Bestand | Doel | Toepassing |
|---------|------|------------|
| `stijl_basislaag.qml` | Hoofdlaag achtergrond | Gebouwen, landgebruik |
| `Stijl_polygoonlaag.qml` | Polygonen op kaart | Parken, waterlichamen |
| `Stijl_lijnlaag.qml` | Lijnenelementen | Wegen, rivieren |
| `Stijl_puntlaag.qml` | Puntelementen | POI markers |
| `Stijl_zwarte_achtergrond.qml` | Contrast achtergrond | Print preview |
| `Tekst_kaartelementen.qml` | Tekst op kaart | Labels |
| `Tekst_legende.qml` | Legenda tekst | Legende annotaties |
| `Schaalbalk.qml` | Schaalweergave | Afstandsreferentie |
| `legende_achtergrond.qml` | Legenda achtergrond | Legenda blok |
| `Grenslaag_legende.qml` | Grenslijnen in legenda | Administratieve grenzen |
| `stijl_*_legende.qml` | Legenda-specifieke stijlen | Verschillende legenda items |

## Documentatie

Gedetailleerde documentatie is beschikbaar in de `docs/` map:

- **[Installatiehandleiding](docs/installation.md)** - Stapsgewijze installatie-instructies
- **[Gebruikershandleiding](docs/user_guide.md)** - Hoe het model te gebruiken
- **[Voorbeelden](docs/examples.md)** - Praktische use cases en resultaten

## Technische Details

### Braille Implementatie

Het script `text_and_braille_algorithm.py` implementeert:
- **6-punts braille** volgens ISO 11548-1 standaard
- **Puntdiameter**: 1.5 mm (tactieel leesbaar)
- **Horizontale/verticale spacing**: 2.5 mm
- **Celdimensies**: 6.0 × 10.0 mm
- **Ondersteuning voor**:
  - Nederlands alfabet (a-z)
  - Cijfers (0-9) met cijferteken-prefix
  - Geaccentueerde letters (é, è, ê, ë, enz.)
  - Spaties en basisinterpunctie

### Model Workflow

Het QGIS-model voert de volgende stappen uit:

1. **Data validatie** - Controleert CRS-compatibiliteit
2. **Geometrie processing** - Vereenvoudigt en combineert lagen
3. **Stijl toepassing** - Past voorgedefinieerde QML-stijlen toe
4. **Tekst rendering** - Genereert braille + reguliere tekst
5. **Rasterisatie** - Converteert naar hoogtemodel
6. **Export voorbereiding** - Clipt en schaalt voor 3D-print

## Belangrijke Opmerkingen

### CRS Configuratie
**KRITIEK**: Gebruik altijd een metrisch coördinatensysteem!

- ❌ **VERKEERD**: WGS84 (EPSG:4326) - geografische graden
- ✅ **CORRECT**: 
  - België: Lambert 72 (EPSG:31370)
  - Nederland: Amersfoort RD New (EPSG:28992)
  - Algemeen: UTM zones (EPSG:326xx)

**Project CRS moet identiek zijn aan basislaag CRS** om vervormingen te voorkomen!

### Stijlen en Paden

De stijlbestanden bevatten relatieve paden. Bij het eerste gebruik moet je mogelijk:
1. De stijlen handmatig selecteren uit de `styles/` map
2. OF de stijlen importeren in je QGIS Style Manager (aanbevolen)

## Bijdragen

Dit project is ontwikkeld voor onderzoeksdoeleinden. Suggesties en verbeteringen zijn welkom!

1. Fork het project
2. Maak een feature branch (`git checkout -b feature/geweldige-feature`)
3. Commit je wijzigingen (`git commit -m 'Voeg geweldige feature toe'`)
4. Push naar de branch (`git push origin feature/geweldige-feature`)
5. Open een Pull Request

## Licentie

Dit project is gelicenseerd onder de MIT License - zie het [LICENSE](LICENSE) bestand voor details.

## Citatie

Als je dit project gebruikt in je onderzoek, citeer dan:

```
Maurien Stroobant (2026). Automatisch Stappenplan voor 3D-Printbare Tactiele Kaarten. 
Thesis [Universiteit]. GitHub repository: https://github.com/MaurienStroobant/3D-printable-tactile-maps-QGIS
```

## Contact

Voor vragen of ondersteuning:
-  **Issues**: [GitHub Issues](https://github.com/MaurienStroobant/3D-printable-tactile-maps-QGIS/issues)

---

# English Version

# Automated Workflow for 3D-Printable Tactile Maps

An automated QGIS workflow for generating 3D-printable tactile maps, developed as part of a thesis on accessible cartography.

## Overview

This project provides a complete QGIS model for automatically generating tactile maps suitable for 3D printing. It distributes regional data with Braille annotations and styles to produce maps that are tactile for people with visual impairments.

### Key Features

- ✅ **Fully automated QGIS model** - from raw geodata to print-ready STL file
- ✅ **Braille and text combination** - custom Python script for merging braille and regular text
- ✅ **Predefined styles** - 13 QGIS style files (QML) for consistent visualization
- ✅ **Metric coordinate system** - optimal for 3D printing accuracy

## Requirements

### Software
- **QGIS 3.28 or higher** (tested on QGIS 3.40.5 and 3.44.10)
  - QGIS 3.28-3.40: use `Model.model3`
  - QGIS 3.44+: use `Model.model`
- **STL Generator Plugin** (for final 3D export)

### Data Requirements
- Geodata in a **metric coordinate system** (e.g., EPSG:31370 for Belgium, EPSG:28992 for Netherlands)
- Project CRS must be **identical** to base layer CRS to prevent distortions

## Installation

### Step 1: Download Repository

```bash
git clone https://github.com/MaurienStroobant/3D-printable-tactile-maps-QGIS.git
cd 3D-printable-tactile-maps-QGIS
```

Or download as ZIP via the green "Code" button → "Download ZIP"

### Step 2: Import QGIS Model

1. Open QGIS
2. Go to **Processing** → **Model Designer**
3. Click **Open Model** (folder icon)
4. Select:
   - `models/Model.model` (QGIS 3.44+)
   - `models/Model.model3` (QGIS 3.28-3.40)

### Step 3: Install Python Script

The braille script must be placed in the QGIS Processing scripts folder:

**Windows:**
```
C:\Users\<your-name>\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\
```

**macOS/Linux:**
```
~/.local/share/QGIS/QGIS3/profiles/default/processing/scripts/
```

**Installation steps:**
1. Copy `scripts/text_and_braille_algorithm.py` to the location above
2. Restart QGIS or click **Refresh** in the Processing Toolbox
3. The script appears under **Scripts** → **Text Tools** → **Combine Text and Braille**

### Step 4: Prepare Style Files

The style files in the `styles/` folder must be applied when using the model. Two options:

#### Option A: Manual Application
1. When the model asks to select a style
2. Navigate to the `styles/` folder in this repository
3. Select the appropriate `.qml` file

#### Option B: Import Styles into QGIS (Recommended)
1. Go to **Settings** → **Style Manager**
2. Import all styles from the `styles/` folder
3. Styles are now available in all projects

### Step 5: STL Generator Plugin

1. Go to **Plugins** → **Manage and Install Plugins**
2. Search for **"STL Generator"**
3. Click **Install Plugin**

## Usage

### Basic Workflow

1. **Open the model** in Processing Model Designer
2. **Set your base layer** (must be in metric CRS!)
3. **Check Project CRS** - must match base layer CRS
4. **Run the model**:
   - Select your input layers (polygons, lines, points)
   - Choose appropriate styles from the `styles/` folder
   - Add text/labels (automatically converted to braille)
5. **Export to STL** using the STL Generator plugin

### Important Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| Base layer | Main polygon layer | Buildings, land use |
| Line layer | Roads, rivers | Street network |
| Point layer | POIs | Landmarks, facilities |
| Project CRS | Must be metric | EPSG:31370, EPSG:28992 |
| Text size | Font size (pt) | 72 pt (default) |

## Documentation

Detailed documentation is available in the `docs/` folder:

- **[Installation Guide](docs/installation.md)** - Step-by-step installation instructions
- **[User Guide](docs/user_guide.md)** - How to use the model
- **[Examples](docs/examples.md)** - Practical use cases and results

## Important Notes

### CRS Configuration
**CRITICAL**: Always use a metric coordinate system!

- ❌ **WRONG**: WGS84 (EPSG:4326) - geographic degrees
- ✅ **CORRECT**: 
  - Belgium: Lambert 72 (EPSG:31370)
  - Netherlands: Amersfoort RD New (EPSG:28992)
  - General: UTM zones (EPSG:326xx)

**Project CRS must be identical to base layer CRS** to prevent distortions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support:
- **Issues**: [GitHub Issues](https://github.com/MaurienStroobant/3D-printable-tactile-maps-QGIS/issues)
