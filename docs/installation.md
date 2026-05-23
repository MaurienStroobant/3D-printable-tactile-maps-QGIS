# Installatiehandleiding - Tactiele Kaarten QGIS Workflow

Deze handleiding leidt je stap-voor-stap door het installatieproces.

## Inhoudsopgave

1. [Vereisten Controleren](#1-vereisten-controleren)
2. [Repository Downloaden](#2-repository-downloaden)
3. [QGIS Model Importeren](#3-qgis-model-importeren)
4. [Python Script Installeren](#4-python-script-installeren)
5. [Stijlbestanden Configureren](#5-stijlbestanden-configureren)
6. [STL Generator Plugin](#6-stl-generator-plugin)
7. [Verificatie](#7-verificatie)
8. [Probleemoplossing](#8-probleemoplossing)

---

## 1. Vereisten Controleren

### QGIS Versie Controleren

1. Open QGIS
2. Ga naar **Help** → **About**
3. Controleer de versienummer:
   - ✅ Versie 3.28 of hoger = OK
   - ❌ Lager dan 3.28 = Update QGIS eerst

**QGIS downloaden/updaten:**
- Website: https://qgis.org/download/
- Kies de **Long Term Release (LTR)** versie voor stabiliteit
- Of de **Latest Release** voor nieuwste features

### Controleer je QGIS Profiel Locatie

**Windows:**
1. Open Verkenner
2. Typ in de adresbalk: `%APPDATA%\QGIS\QGIS3\profiles\default`
3. Noteer dit pad - je hebt het later nodig

**macOS:**
1. Open Finder
2. Ga naar menu → **Go** → **Go to Folder**
3. Typ: `~/Library/Application Support/QGIS/QGIS3/profiles/default`

**Linux:**
1. Open je bestandsbeheerder
2. Toon verborgen bestanden (Ctrl+H)
3. Ga naar: `~/.local/share/QGIS/QGIS3/profiles/default`

---

## 2. Repository Downloaden

### Optie A: Git Clone (als je Git hebt)

```bash
git clone https://github.com/MaurienStroobant/3D-printable-tactile-maps-QGIS.git
cd 3D-printable-tactile-maps-QGIS
```

### Optie B: ZIP Download (makkelijkste)

1. Ga naar de GitHub repository pagina
2. Klik op de groene **Code** knop
3. Selecteer **Download ZIP**
4. Pak het ZIP-bestand uit naar een locatie naar keuze, bijvoorbeeld:
   - Windows: `C:\Users\[jouw-naam]\Documents\3D-printable-tactile-maps-QGIS`
   - macOS: `~/Documents/3D-printable-tactile-maps-QGIS`
   - Linux: `~/Documents/3D-printable-tactile-maps-QGIS`

**✅ Na deze stap heb je een map met:**
```
3D-printable-tactile-maps-QGIS/
├── models/
├── scripts/
├── styles/
├── docs/
└── README.md
```

---

## 3. QGIS Model Importeren

### Stap-voor-stap

1. **Open QGIS**

2. **Open de Model Designer:**
   - Ga naar menu → **Processing** → **Model Designer**
   - Of gebruik het icoon in de Processing Toolbox

3. **Selecteer het juiste modelbestand:**
   
   **BELANGRIJK**: Kies op basis van je QGIS versie!
   
   | QGIS Versie | Te gebruiken bestand |
   |-------------|---------------------|
   | 3.28 - 3.38 | `Model.model3` |
   | 3.40 en hoger | `Model.model` |

4. **Importeer het model:**
   - Klik op het **Open Model** icoon (📁 map-icoon) in de toolbar
   - Navigeer naar `3D-printable-tactile-maps-QGIS/models/`
   - Selecteer `Model.model` of `Model.model3` (zie tabel hierboven)
   - Klik **Open**

5. **Sla het model op (optioneel):**
   - Menu → **Model** → **Save As**
   - Sla op in je QGIS models directory voor snelle toegang later
   - Locatie: `[QGIS profiel]/processing/models/`

**✅ Verificatie:**
- Je ziet nu het model-diagram in de Model Designer
- Het bevat meerdere connected boxes (processing stappen)

---

## 4. Python Script Installeren

Het braille-script moet in een specifieke map geplaatst worden zodat QGIS het kan vinden.

### Stap 1: Vind de Processing Scripts Map

**Windows:**
```
C:\Users\[jouw-naam]\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts
```

**macOS:**
```
~/Library/Application Support/QGIS/QGIS3/profiles/default/processing/scripts
```

**Linux:**
```
~/.local/share/QGIS/QGIS3/profiles/default/processing/scripts
```

**Als de `scripts` map niet bestaat:**
- Maak deze handmatig aan binnen de `processing` folder

### Stap 2: Kopieer het Script

1. **Vind het bronbestand:**
   - Ga naar je gedownloade repository
   - Open de `scripts/` map
   - Je ziet: `text_and_braille_algorithm.py`

2. **Kopieer het bestand:**
   - Kopieer `text_and_braille_algorithm.py`
   - Plak in de QGIS processing scripts map (zie Stap 1)

### Stap 3: QGIS Refresh

**Optie A: Herstart QGIS**
- Sluit QGIS volledig af
- Start QGIS opnieuw op

**Optie B: Refresh Processing (sneller)**
1. Open de **Processing Toolbox** (Ctrl+Alt+T)
2. Klik op het **Refresh** icoon (🔄) bovenaan de toolbox
3. Of: rechtermuisklik in de toolbox → **Refresh Algorithms**

**✅ Verificatie:**
- Open de Processing Toolbox
- Vouw **Scripts** uit
- Vouw **Tekst gereedschappen** uit
- Je ziet nu: **"Tekst en Braille combineren"**

---

## 5. Stijlbestanden Configureren

De stijlbestanden kunnen op twee manieren gebruikt worden:

### Optie A: Handmatig Selecteren (Basis)

Wanneer je het model uitvoert en gevraagd wordt om een stijl:
1. Navigeer naar `tactile-maps-qgis/styles/`
2. Selecteer het juiste `.qml` bestand
3. Herhaal voor elke stijlparameter in het model

**Voordeel:** Direct klaar voor gebruik  
**Nadeel:** Je moet elke keer naar de styles folder navigeren

### Optie B: Importeren in Style Manager (Aanbevolen)

Dit maakt de stijlen beschikbaar in alle projecten:

1. **Open de Style Manager:**
   - Menu → **Settings** → **Style Manager**

2. **Importeer items:**
   - Klik op de **Import/Export** knop (↓ icoon) onderaan
   - Selecteer **Import Items**

3. **Selecteer alle stijlbestanden:**
   - Navigeer naar `3D-printable-tactile-maps-QGIS/styles/`
   - Selecteer ALLE `.qml` bestanden (Ctrl+A / Cmd+A)
   - Klik **Open**

4. **Kies importopties:**
   - Selecteer **Symbol** als categorie
   - Klik **Import**

5. **Groepeer de stijlen (optioneel maar handig):**
   - Maak een nieuwe groep: **"Tactile Maps"**
   - Verplaats alle geïmporteerde stijlen naar deze groep

**✅ Verificatie:**
- Open een willekeurige laag properties
- Ga naar **Symbology**
- Klik op **Style** → je ziet de geïmporteerde stijlen

### Overzicht Stijlbestanden

| Bestand | Wanneer te gebruiken |
|---------|---------------------|
| `stijl_basislaag.qml` | Hoofd polygoonlaag (gebouwen, landgebruik) |
| `Stijl_polygoonlaag.qml` | Extra polygonen (parken, water) |
| `Stijl_lijnlaag.qml` | Lijnenelementen (wegen, rivieren) |
| `Stijl_puntlaag.qml` | Punt markers (POI's) |
| `Stijl_zwarte_achtergrond.qml` | Zwarte achtergrond voor contrast |
| `Tekst_kaartelementen.qml` | Tekst labels op kaart |
| `Tekst_legende.qml` | Tekst in de legenda |
| `Schaalbalk.qml` | Schaalweergave |
| `legende_achtergrond.qml` | Achtergrond legenda box |
| `Grenslaag_legende.qml` | Grenslijnen in legenda |
| `stijl_*_legende.qml` | Specifieke legenda items |

---

## 6. STL Generator Plugin

Deze plugin is nodig voor de finale export naar 3D-printbaar formaat.

### Installatie

1. **Open Plugin Manager:**
   - Menu → **Plugins** → **Manage and Install Plugins**

2. **Zoek de plugin:**
   - Typ in het zoekvenster: **"STL Generator"**
   - Klik op de plugin in de resultaten

3. **Installeer:**
   - Klik op **Install Plugin**
   - Wacht tot de installatie compleet is
   - Klik **Close**

**✅ Verificatie:**
- Ga naar menu → **Plugins**
- Je ziet nu: **"STL Generator"** in de lijst
- Of: rechterklik op een raster laag → je ziet **"Generate STL"** optie

---

## 7. Verificatie - Complete Installatie Check

Voer deze checklist uit om te verifiëren dat alles correct is geïnstalleerd:

### ✅ Checklist

- [ ] QGIS versie 3.28 of hoger
- [ ] Model zichtbaar in Model Designer (`Model.model` of `Model.model3`)
- [ ] Python script beschikbaar in Processing Toolbox onder Scripts
- [ ] Stijlbestanden toegankelijk (handmatig of via Style Manager)
- [ ] STL Generator plugin geïnstalleerd
- [ ] Je hebt geodata in een metrisch coördinatensysteem

**Als alles aangevinkt is: 🎉 Je bent klaar om te beginnen!**

Ga naar de [Gebruikershandleiding](user_guide.md) voor instructies over het daadwerkelijk gebruiken van het model.

---

## 8. Probleemoplossing

### Python Script Verschijnt Niet

**Probleem:** Script staat in de juiste map maar is niet zichtbaar in Processing Toolbox.

**Oplossingen:**
1. **Controleer bestandsnaam:**
   - Moet exact zijn: `text_and_braille_algorithm.py`
   - Geen extra spaties of karakters

2. **Controleer bestandslocatie:**
   - Windows: Controleer dat je in `AppData\Roaming` bent, NIET `AppData\Local`
   - Gebruik `%APPDATA%\QGIS` om zeker te zijn

3. **Python errors checken:**
   - Open QGIS
   - Ga naar **View** → **Panels** → **Log Messages**
   - Selecteer **Processing** tab
   - Kijk naar errors bij het laden van scripts

4. **Profiel controleren:**
   - Als je meerdere QGIS profielen hebt
   - Zorg dat je in het juiste profiel werkt
   - Menu → **Settings** → **User Profiles** → **Open Active Profile Folder**

### Model Laadt Niet

**Probleem:** Foutmelding bij het openen van het model.

**Oplossing:**
- Controleer je QGIS versie
- Gebruik `Model.model3` voor oudere versies (3.28-3.38)
- Gebruik `Model.model` voor nieuwere versies (3.40+)
- Update QGIS als je versie te oud is

### Stijlen Werken Niet

**Probleem:** Stijlen worden niet correct toegepast.

**Mogelijke oorzaken:**
1. **Verkeerde laagtype:**
   - Een polygoon-stijl werkt niet op een lijnlaag
   - Check dat je de juiste stijl voor het juiste laagtype gebruikt

2. **CRS mismatch:**
   - Sommige stijlen zijn CRS-afhankelijk
   - Zorg dat je project in een metrisch CRS staat

3. **QGIS versie:**
   - Stijlen zijn gemaakt in QGIS 3.40
   - Oudere versies kunnen compatibiliteitsproblemen hebben

### STL Generator Niet Beschikbaar

**Probleem:** Plugin installeert niet of werkt niet.

**Oplossingen:**
1. **Update QGIS:**
   - Oudere versies hebben mogelijk geen toegang tot deze plugin
   - Installeer minimaal QGIS 3.28

2. **Check plugin repository:**
   - **Settings** → **Options** → **Plugins**
   - Zorg dat plugin repository actief is
   - Klik **Check for Updates**

3. **Alternatief:**
   - Export als GeoTIFF
   - Gebruik externe software (Blender, CloudCompare) voor STL conversie

### Algemene Tips

1. **Log Messages gebruiken:**
   - Menu → **View** → **Panels** → **Log Messages**
   - Dit toont gedetailleerde foutmeldingen

2. **Community help:**
   - QGIS community forum: https://gis.stackexchange.com
   - Tag je vraag met `[qgis]` en `[processing]`

3. **GitHub Issues:**
   - Voor specifieke problemen met dit project
   - Open een issue op de repository pagina

---

## Volgende Stappen

Nu je installatie compleet is:
1. 📖 Lees de [Gebruikershandleiding](user_guide.md)
2. 🎯 Bekijk de [Voorbeelden](examples.md)
3. 🚀 Start met je eerste tactiele kaart!

---

**Vragen?** Open een issue op GitHub of check de documentatie in de `docs/` map.
