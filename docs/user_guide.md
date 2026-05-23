# Gebruikershandleiding - Tactiele Kaarten Workflow

Deze handleiding legt uit hoe je het QGIS model gebruikt om 3D-printbare tactiele kaarten te genereren.

## Inhoudsopgave

1. [Voorbereiding](#1-voorbereiding)
2. [Data Vereisten](#2-data-vereisten)
3. [Het Model Uitvoeren](#3-het-model-uitvoeren)
4. [Braille Tekst Genereren](#4-braille-tekst-genereren)
5. [Export naar STL](#5-export-naar-stl)
6. [Best Practices](#6-best-practices)
7. [Veelvoorkomende Scenario's](#7-veelvoorkomende-scenarios)
8. [Probleemoplossing](#8-probleemoplossing)

---

## 1. Voorbereiding

### Nieuw Project Aanmaken

1. **Start QGIS**
2. **Maak een nieuw project:**
   - Menu → **Project** → **New**
   - Of gebruik Ctrl+N (Cmd+N op Mac)

3. **Stel Project CRS in:**
   - Klik rechtsonder op het CRS (bijv. "EPSG:4326")
   - OF: Menu → **Project** → **Properties** → **CRS**
   - **BELANGRIJK:** Kies een METRISCH coördinatensysteem!

### Aanbevolen CRS per Land/Regio

| Land/Regio | CRS Code | Naam |
|------------|----------|------|
| 🇧🇪 België | EPSG:31370 | Belgian Lambert 72 |
| 🇳🇱 Nederland | EPSG:28992 | Amersfoort / RD New |
| 🇩🇪 Duitsland (West) | EPSG:25832 | ETRS89 / UTM zone 32N |
| 🇫🇷 Frankrijk | EPSG:2154 | Lambert-93 |
| 🇬🇧 UK | EPSG:27700 | British National Grid |
| Europa (algemeen) | EPSG:3035 | ETRS89-extended / LAEA Europe |

**⚠️ NOOIT gebruiken:** EPSG:4326 (WGS84) - dit is in graden, niet meters!

---

## 2. Data Vereisten

### Minimale Vereisten

Wat je nodig hebt:
- ✅ **Basislaag**: Een polygoonlaag (gebouwen, landgebruik, etc.)
- ✅ **Data in metrisch CRS**: Alle lagen in dezelfde metrische projectie
- ✅ **Geografisch beperkt gebied**: Ideaal 100m - 5km voor één kaart

### Optionele Lagen

Voor rijkere kaarten kun je toevoegen:
- 🗺️ **Lijnlaag**: Wegen, rivieren, paden
- 📍 **Puntlaag**: POI's, landmarks
- 🏷️ **Labels**: Straatnamen, gebouwnamen

### Data Importeren

1. **Voeg je data toe:**
   - Sleep bestanden naar QGIS, OF
   - Menu → **Layer** → **Add Layer** → kies type (Vector/Raster)

2. **Controleer CRS:**
   - Rechterklik op laag → **Properties** → **Information**
   - Check "CRS" veld
   - **MOET metrisch zijn!** (bijv. EPSG:31370, niet EPSG:4326)

3. **Herproject indien nodig:**
   - Rechterklik op laag → **Export** → **Save Features As**
   - Selecteer het juiste metrische CRS
   - Sla op als nieuwe laag

### CRS Matching Controleren

**KRITIEKE REGEL:** Alle lagen EN het project moeten HETZELFDE CRS hebben!

**Snelle check:**
```
Laag 1: EPSG:31370 ✅
Laag 2: EPSG:31370 ✅
Project: EPSG:31370 ✅
RESULTAAT: Perfect! 🎉

Laag 1: EPSG:31370 ❌
Laag 2: EPSG:4326  ❌
Project: EPSG:31370 ❌
RESULTAAT: Vervormingen! Herprojecteer laag 2!
```

---

## 3. Het Model Uitvoeren

### Model Openen

1. **Open Processing Toolbox:**
   - Menu → **Processing** → **Toolbox**
   - Of druk Ctrl+Alt+T (Cmd+Option+T op Mac)

2. **Vind je model:**
   - Als je het hebt opgeslagen in models directory:
     - Vouw **Models** uit
     - Dubbelklik op je model
   - OF open via Model Designer:
     - **Processing** → **Model Designer**
     - Open het modelbestand
     - Klik op **Run** (▶ icoon)

### Model Parameters Invullen

Het model vraagt om verschillende inputs. Hieronder de belangrijkste:

#### 1. Basislaag (Verplicht)

- **Wat:** Je hoofd-polygoonlaag
- **Voorbeelden:** Gebouwen, landgebruik, administratieve grenzen
- **Tip:** Kies de laag met de meeste detail voor je kaartgebied

#### 2. Lijnlaag (Optioneel)

- **Wat:** Lineaire features
- **Voorbeelden:** Wegen, rivieren, spoorlijnen
- **Stijl:** Selecteer `Stijl_lijnlaag.qml` uit de styles folder

#### 3. Puntlaag (Optioneel)

- **Wat:** Punt-locaties
- **Voorbeelden:** Bushokjes, bomen, landmarks
- **Stijl:** Selecteer `Stijl_puntlaag.qml`

#### 4. Stijlbestanden Toewijzen

Voor elke laag moet je de juiste stijl selecteren:

| Parameter | Selecteer Bestand |
|-----------|------------------|
| Basislaag stijl | `stijl_basislaag.qml` |
| Polygoonlaag stijl | `Stijl_polygoonlaag.qml` |
| Lijnlaag stijl | `Stijl_lijnlaag.qml` |
| Puntlaag stijl | `Stijl_puntlaag.qml` |
| Achtergrond | `Stijl_zwarte_achtergrond.qml` |
| Legende achtergrond | `legende_achtergrond.qml` |

**Waar stijlen te vinden:**
- Als je ze hebt geïmporteerd: dropdown menu
- Anders: klik op **...** en navigeer naar `styles/` folder

#### 5. Tekst & Braille Parameters

| Parameter | Beschrijving | Aanbevolen Waarde |
|-----------|--------------|------------------|
| Invoertekst | De tekst voor labels | bijv. "Centraal Station" |
| Lettergrootte | Grootte van zichtbare tekst | 72 pt |
| Letter spacing | Extra ruimte tussen letters | 0-2 px |
| Layout | Positie braille t.o.v. tekst | Braille boven tekst |

#### 6. Output Parameters

- **Output locatie:** Kies waar tijdelijke files worden opgeslagen
- **Gebruik:** `[Save to temporary file]` voor testen
- **Voor eindresultaat:** Kies een vaste locatie

### Model Uitvoeren

1. **Alle parameters ingevuld?** Controleer bovenaan het dialoogvenster
2. **Klik op RUN** (onderaan rechts)
3. **Wacht:** Processing kan 30 seconden tot enkele minuten duren
4. **Check het Log venster** voor voortgang en eventuele waarschuwingen

### Resultaat Beoordelen

Na voltooiing:
- ✅ Nieuwe lagen verschijnen in je Layers panel
- ✅ Kaart toont de tactiele versie met contrast
- ✅ Braille en tekst zijn zichtbaar (zoom in om details te zien)

**Controleer:**
1. Zijn alle elementen zichtbaar?
2. Is de braille leesbaar (punten groot genoeg)?
3. Is er genoeg contrast tussen elementen?

---

## 4. Braille Tekst Genereren

### Standalone Braille Script Gebruiken

Je kunt ook losse braille-tekst genereren zonder het volledige model.

1. **Open Processing Toolbox**
2. **Navigeer naar:**
   - Scripts → Tekst gereedschappen → **"Tekst en Braille combineren"**

3. **Parameters:**

| Parameter | Uitleg | Voorbeeld |
|-----------|--------|-----------|
| Invoertekst | Tekst om te converteren | "Station Gent" |
| Lettergrootte tekst | Grootte normale tekst | 72 pt |
| Extra spatering tekst | Ruimte tussen letters | 0 px |
| Layout | Waar braille t.o.v. tekst | Braille boven, tekst onder |
| Coördinatenstelsel | CRS voor output | EPSG:31370 |

4. **Klik RUN**

### Braille Specificaties

Het script gebruikt **6-punts braille** volgens ISO 11548-1:

```
Braille cel (2 kolommen x 3 rijen):
  1  4
  2  5
  3  6

Afmetingen:
- Puntdiameter: 1.5 mm (tactieel leesbaar)
- Horizontale afstand: 2.5 mm
- Verticale afstand: 2.5 mm
- Celbreedte: 6.0 mm
- Celhoogte: 10.0 mm
```

### Ondersteunde Karakters

- ✅ **Letters:** a-z (klein en hoofdletters)
- ✅ **Cijfers:** 0-9 (met cijferteken prefix)
- ✅ **Accenten:** é, è, ê, ë, ç, ñ, etc.
- ✅ **Spaties:** Lege braille cel
- ❌ **Niet ondersteund:** Complexe interpunctie, speciale symbolen

**Voorbeeld conversie:**
```
Input:  "Rue de la Gare 15"
Braille: ⠗⠥⠑ ⠙⠑ ⠇⠁ ⠛⠁⠗⠑ ⠼⠁⠑
         (cijferteken vóór "15")
```

---

## 5. Export naar STL

### Voorbereiding

1. **Selecteer de juiste laag:**
   - Meestal de finale raster output van het model
   - Of een gecombineerde polygoonlaag

2. **Controleer de laag:**
   - Zoom naar je kaartgebied
   - Controleer of alles correct is weergegeven
   - Let op overlappende elementen

### Export Proces

1. **Rechterklik op de te exporteren laag**
2. **Selecteer "Generate STL" of "Export to STL"**
   - Dit is de functie van de STL Generator plugin

3. **Stel export parameters in:**

| Parameter | Aanbevolen Waarde | Uitleg |
|-----------|------------------|--------|
| Scale (Z-axis) | 1.0 - 3.0 | Verticale vergroting voor reliëf |
| Model spacing | 0.1 - 1.0 mm | Detailniveau (lager = meer detail) |
| Base height | 2-5 mm | Dikte van de basis |
| Invert Z | Nee | Tenzij je een mal wilt |

4. **Kies output locatie en klik OK**

### STL Verificatie

**Voor 3D-printen moet je het STL bestand controleren:**

1. **Open in STL viewer:**
   - Gratis tools: MeshLab, Windows 3D Viewer, Blender
   - Online: viewstl.com, 3dviewer.net

2. **Check voor problemen:**
   - ✅ Gesloten geometrie (manifold mesh)
   - ✅ Geen gaten of overlappingen
   - ✅ Binnen printbed grootte
   - ✅ Voldoende wanddikte (min. 2mm)

3. **Repareer indien nodig:**
   - Tools: Meshmixer, MeshLab, Microsoft 3D Builder
   - Online: cloud.netfabb.com

---

## 6. Best Practices

### Planning

📋 **Voor je begint:**
1. Bepaal je kaartschaal (bijv. 1:1000, 1:5000)
2. Bepaal kaartgrootte (max printbed grootte)
3. Selecteer essentiële features (niet alles erbij!)
4. Test eerst met een klein gebied

### Data Voorbereiding

🗺️ **Optimaliseer je data:**
1. **Vereenvoudig geometrie:**
   - Menu → Vector → Geometry Tools → **Simplify**
   - Tolerantie: 0.5-2 meter (afhankelijk van schaal)

2. **Clip naar je gebied:**
   - Gebruik alleen data binnen je interessegebied
   - Menu → Vector → Geoprocessing Tools → **Clip**

3. **Categoriseer features:**
   - Groepeer vergelijkbare elementen
   - Gebruik attribuut-gebaseerde filtering

### Tactiele Design Principes

👆 **Voor tastbare kaarten:**

1. **Hoogteverschillen:**
   - Minimum verschil: 0.5 mm (voelbaar)
   - Aanbevolen: 1-2 mm tussen niveaus
   - Maximum: 5-8 mm (printability)

2. **Lijndiktes:**
   - Minimum: 1.5 mm breed
   - Wegen: 2-3 mm
   - Hoofdwegen: 3-5 mm

3. **Braille leesbaarbeid:**
   - Standaard 1.5 mm punten (niet wijzigen!)
   - Minimale afstand tot andere elementen: 3 mm
   - Plaats braille niet over complexe geometrie

4. **Contrast:**
   - Gebruik duidelijk verschillende hoogtes
   - Vermijd te veel detail op één plek
   - Laat "witte ruimte" voor oriëntatie

### Printinstellingen

🖨️ **Voor optimale 3D-print:**

| Parameter | Waarde | Reden |
|-----------|--------|-------|
| Layer height | 0.2-0.3 mm | Balans detail/snelheid |
| Infill | 20-30% | Voldoende sterk, niet te zwaar |
| Materiaal | PLA of PETG | Makkelijk te printen |
| Support | Minimaal | Alleen indien echt nodig |
| Bed adhesion | Brim (5mm) | Voorkomt warping |

---

## 7. Veelvoorkomende Scenario's

### Scenario 1: Stadscentrum Kaart

**Doel:** Tactiele kaart van binnenstad met belangrijkste gebouwen en straten.

**Stappen:**
1. **Data:** OSM gebouwen + wegen voor je stad
2. **Schaal:** 1:2000 (50x50m gebied)
3. **Lagen:**
   - Basislaag: Gebouwen (3mm hoog)
   - Lijnlaag: Hoofdwegen (2mm breed, 1mm hoog)
   - Tekst: Belangrijkste straatnamen + braille
4. **Stijlen:** Gebruik contrast (donkere gebouwen, lichte wegen)
5. **Print:** 150x150mm kaart op A4 printbed

### Scenario 2: Campus/Terrein Kaart

**Doel:** Overzichtskaart van universiteitscampus of park.

**Stappen:**
1. **Data:** Gebouwen, paden, groengebieden
2. **Schaal:** 1:1000
3. **Features:**
   - Gebouwen als volumes (4-5mm)
   - Paden als lijnen (2mm breed)
   - Groen als textuur (0.5mm patroon)
   - Ingangen als punten (3mm cilinders)
4. **Legenda:** Aparte braille legenda met symbooluitleg

### Scenario 3: Route Kaart

**Doel:** Een specifieke route (bijv. wandelroute, evacuatieroute).

**Stappen:**
1. **Data:** Route-lijn + omgeving voor context
2. **Emphasis:** Route zeer dik (5mm) en verhoogd (2mm)
3. **Context:** Gebouwen/straten lichter (1mm hoog)
4. **Waypoints:** Belangrijke punten als verhoogde markers
5. **Braille:** Start/eind labels + richtingaanwijzingen

---

## 8. Probleemoplossing

### Model Geeft Foutmelding

**"CRS mismatch" Error:**
- ❌ Probleem: Lagen hebben verschillende CRS
- ✅ Oplossing: Herprojecteer alle lagen naar hetzelfde metrische CRS

**"Invalid geometry" Error:**
- ❌ Probleem: Geometrie bevat fouten (overlaps, gaps)
- ✅ Oplossing:
  1. Vector → Geometry Tools → **Fix Geometries**
  2. Of: Vector → Geometry Tools → **Check Validity**

**"Out of memory" Error:**
- ❌ Probleem: Dataset te groot
- ✅ Oplossing:
  1. Vereenvoudig geometrie (Simplify tool)
  2. Clip naar kleiner gebied
  3. Verhoog raster resolutie (grotere pixels)

### Braille Niet Leesbaar

**Punten te klein:**
- Controleer Z-scale bij STL export (verhoog naar 2.0-3.0)
- Controleer dat script standaard 1.5mm diameter gebruikt

**Braille vervormd:**
- Probleem: Niet-metrische CRS gebruikt
- Herstart met metrisch CRS vanaf het begin

### Stijlen Werken Niet

**Stijl wordt niet toegepast:**
1. Controleer laagtype (polygoon/lijn/punt) matcht stijltype
2. Refresh laag (rechterklik → Refresh)
3. Herlaad stijl handmatig via Layer Properties

**Kleuren fout:**
- Sommige stijlen zijn schaal-afhankelijk
- Zoom naar juiste schaalniveau

### STL Export Faalt

**Plugin niet gevonden:**
- Herinstalleer STL Generator plugin
- Check QGIS versie compatibiliteit

**Leeg STL bestand:**
- Controleer dat laag daadwerkelijk geometrie bevat
- Zoom naar extent van de laag
- Check dat laag zichtbaar is

**Te groot bestand:**
- Verhoog model spacing (minder detail)
- Vereenvoudig geometrie voor export
- Clip naar kleiner gebied

---

## Volgende Stappen

🎓 **Je kunt nu:**
- Eigen tactiele kaarten maken
- Experimenteren met verschillende datasets
- Stijlen aanpassen naar eigen wensen

📚 **Meer leren:**
- Bekijk [Voorbeelden](examples.md) voor inspiratie
- Check QGIS documentatie voor geavanceerde features
- Deel je resultaten en krijg feedback!

---

**Hulp nodig?** Open een issue op GitHub of raadpleeg de FAQ in de documentatie.
