# Stijlbestanden Overzicht

Dit document beschrijft elk stijlbestand en wanneer het te gebruiken.

## 📁 Alle Stijlbestanden

```
styles/
├── stijl_basislaag.qml              # Hoofdlaag (gebouwen, landgebruik)
├── Stijl_polygoonlaag.qml           # Extra polygonen (parken, water)
├── Stijl_lijnlaag.qml               # Lijnelementen (wegen, rivieren)
├── Stijl_puntlaag.qml               # Puntelementen (POI's)
├── Stijl_zwarte_achtergrond.qml     # Zwarte achtergrond voor contrast
├── Tekst_kaartelementen.qml         # Tekst op de kaart
├── Tekst_legende.qml                # Tekst in de legenda
├── Schaalbalk.qml                   # Schaalweergave
├── legende_achtergrond.qml          # Achtergrond van legenda blok
├── Grenslaag_legende.qml            # Grenslijnen in legenda
├── stijl_puntlaag_legende.qml       # Puntelementen in legenda
├── stijl_lijnlaag_legende.qml       # Lijnelementen in legenda
└── stijl_polygoonlaag_legende.qml   # Polygonen in legenda
```

---

## 🗺️ Kaart Stijlen (Hoofdweergave)

### `stijl_basislaag.qml`
**Doel:** Hoofdpolygoonlaag van de kaart

**Kenmerken:**
- Grijze vulling (RGB: 145, 145, 145)
- Zwarte outline (1mm dik)
- Geschikt voor gebouwen, administratieve grenzen, landgebruik

**Wanneer gebruiken:**
- Als je primaire/basis polygoonlaag
- Voor de achtergrond waarop andere elementen komen

**Laagtype:** Polygon

---

### `Stijl_polygoonlaag.qml`
**Doel:** Secundaire polygonen die bovenop de basislaag komen

**Kenmerken:**
- Aangepaste kleuren voor contrast met basislaag
- Duidelijke rand
- Bedoeld voor elementen die moeten opvallen

**Wanneer gebruiken:**
- Parken en groengebieden
- Waterlichamen
- Specifieke gebouwen die aandacht nodig hebben
- Zones met speciale functie

**Laagtype:** Polygon

---

### `Stijl_lijnlaag.qml`
**Doel:** Lineaire elementen op de kaart

**Kenmerken:**
- Variabele lijndikte (afhankelijk van schaal)
- Hoge contrast kleur
- Bedoeld voor tactiel voelbare lijnen

**Wanneer gebruiken:**
- Wegen en straten
- Rivieren en waterlopen
- Spoorlijnen
- Grenzen en routes
- Paden en trails

**Laagtype:** Line

**Tips:**
- Voor hoofdwegen: gebruik dikkere lijnen (3-5mm in print)
- Voor kleine paden: 1.5-2mm
- Zorg voor minimaal 2mm ruimte tussen parallelle lijnen

---

### `Stijl_puntlaag.qml`
**Doel:** Puntelementen op de kaart

**Kenmerken:**
- Cirkelvormige markers
- Vaste grootte of schaal-afhankelijk
- Hoog contrast

**Wanneer gebruiken:**
- POI's (Points of Interest)
- Bushokjes, tramhaltes
- Bomen, lantaarnpalen
- Ingangen van gebouwen
- Parkeerplaatsen
- Oriëntatiepunten

**Laagtype:** Point

**Tips:**
- Gebruik voor belangrijke locaties die tactieel voelbaar moeten zijn
- Minimum diameter: 3mm in print
- Plaats niet te dicht op elkaar (min. 5mm afstand)

---

### `Stijl_zwarte_achtergrond.qml`
**Doel:** Zwarte achtergrond voor maximaal contrast

**Kenmerken:**
- Volledig zwarte vulling
- Geen outline
- Bedoeld als ondergrond

**Wanneer gebruiken:**
- Als contrast-achtergrond voor lichte elementen
- Voor preview/presentatie doeleinden
- Wanneer je de kaart wilt tonen op scherm met hoog contrast
- Niet voor de finale 3D-print (tenzij je specifiek een zwarte base wilt)

**Laagtype:** Polygon

**Let op:** Voor 3D-printing is dit meestal niet nodig - de printbed is je "achtergrond"

---

## 📝 Tekst Stijlen

### `Tekst_kaartelementen.qml`
**Doel:** Tekst labels op de kaart zelf

**Kenmerken:**
- Leesbare fontgrootte
- Hoog contrast kleur
- Positioning regels voor optimale plaatsing

**Wanneer gebruiken:**
- Straatnamen
- Gebouwnamen
- Pleinaanduidingen
- Belangrijke locatienamen
- Korte labels

**Laagtype:** Polygon (gegenereerde tekst)

**Tips:**
- Houd tekst kort (max 15-20 karakters)
- Plaats niet over complexe geometrie
- Laat minimaal 3mm ruimte rondom voor braille
- Voor 3D-print: minimaal 72pt lettergrootte

---

### `Tekst_legende.qml`
**Doel:** Tekst in de legenda/verklaring

**Kenmerken:**
- Mogelijk andere font/grootte dan kaart-tekst
- Uitlijning voor legenda-structuur
- Geoptimaliseerd voor uitleg-teksten

**Wanneer gebruiken:**
- Legenda titels
- Symbool verklaringen
- Notenlijsten
- Schaal-indicaties (tekst)

**Laagtype:** Polygon (text)

---

## 🏷️ Legenda Stijlen

### `legende_achtergrond.qml`
**Doel:** Achtergrondvlak voor de legenda

**Kenmerken:**
- Lichte kleur of patroon
- Duidelijk afgebakend gebied
- Onderscheidt legenda van kaart

**Wanneer gebruiken:**
- Als de legenda op de kaart zelf staat
- Om legenda-gebied visueel te scheiden
- Voor gestructureerde presentatie

**Laagtype:** Polygon

**Tips:**
- Plaats legenda op rustig gebied (bijv. water of buitengebied)
- Houd minimaal 5mm afstand tot kaart-elementen
- Voor 3D-print: overweeg een licht verhoogde of verlaagde base

---

### `Grenslaag_legende.qml`
**Doel:** Grenslijnen weergave in de legenda

**Kenmerken:**
- Duidelijke lijnstijl
- Mogelijk gestippeld of met patroon
- Representatief voor administratieve grenzen

**Wanneer gebruiken:**
- In legenda om te tonen hoe grenzen op kaart worden weergegeven
- Als voorbeeld-symbool voor grenstypen

**Laagtype:** Line

---

### `stijl_puntlaag_legende.qml`
**Doel:** Puntelementen in de legenda

**Kenmerken:**
- Zelfde stijl als `Stijl_puntlaag.qml` maar voor legenda-context
- Mogelijk vaste grootte (niet schaal-afhankelijk)

**Wanneer gebruiken:**
- Om in de legenda te tonen welke symbolen voor welke punt-features staan
- Voorbeelden van POI symbolen

**Laagtype:** Point

---

### `stijl_lijnlaag_legende.qml`
**Doel:** Lijnelementen in de legenda

**Kenmerken:**
- Zelfde stijl als `Stijl_lijnlaag.qml` maar voor legenda-context
- Vaste lijndikte (niet schaal-afhankelijk)

**Wanneer gebruiken:**
- Om verschillende lijn-types uit te leggen
- Voorbeeld van wegen/rivieren in legenda

**Laagtype:** Line

---

### `stijl_polygoonlaag_legende.qml`
**Doel:** Polygonen in de legenda

**Kenmerken:**
- Zelfde stijl als `Stijl_polygoonlaag.qml` maar voor legenda
- Kleine voorbeeldvlakken

**Wanneer gebruiken:**
- Om te tonen hoe verschillende gebieden op de kaart worden weergegeven
- Kleur/patroon voorbeelden

**Laagtype:** Polygon

---

## 📏 Speciale Stijlen

### `Schaalbalk.qml`
**Doel:** Visuele schaalweergave

**Kenmerken:**
- Lineaire schaalbalk
- Met afstandsmarkeringen
- Mogelijk met tekst-labels

**Wanneer gebruiken:**
- Om schaal van de kaart aan te geven
- Essentieel voor tactiele kaarten (gebruikers kunnen niet "inzoomen")
- Plaats op vaste locatie op elke kaart

**Laagtype:** Mixed (Line + mogelijk Text)

**Tips:**
- Gebruik ronde getallen (100m, 500m, 1km)
- Maak de schaalbalk tactieel voelbaar (verhoogd of verdiept)
- Voeg braille toe bij getallen
- Minimum lengte: 30mm
- Plaats op rustige plek (meestal onderaan of zijkant)

---

## 🎨 Stijlen Aanpassen

### Kleuren Wijzigen

1. Rechterklik op laag → **Properties**
2. Ga naar **Symbology** tab
3. Klik op de kleur → kies nieuwe kleur
4. **Style** → **Save Style** → save als nieuw .qml bestand

### Nieuwe Stijl Maken

1. Stel je laag in zoals gewenst
2. **Layer Properties** → **Symbology**
3. Pas aan (kleur, dikte, patroon, etc.)
4. **Style** → **Save Style**
5. Kies locatie en geef duidelijke naam
6. Documenteer het gebruik!

---

## 📋 Snelle Referentie Tabel

| Stijl | Laagtype | Primair Gebruik | Voor Legenda? |
|-------|----------|----------------|---------------|
| `stijl_basislaag.qml` | Polygon | Hoofdlaag (gebouwen) | Nee |
| `Stijl_polygoonlaag.qml` | Polygon | Extra polygonen (parken, water) | Nee |
| `Stijl_lijnlaag.qml` | Line | Wegen, rivieren | Nee |
| `Stijl_puntlaag.qml` | Point | POI's, markers | Nee |
| `Stijl_zwarte_achtergrond.qml` | Polygon | Contrast achtergrond | Nee |
| `Tekst_kaartelementen.qml` | Polygon (text) | Labels op kaart | Nee |
| `Tekst_legende.qml` | Polygon (text) | Tekst in legenda | Ja |
| `Schaalbalk.qml` | Mixed | Schaalweergave | Nee |
| `legende_achtergrond.qml` | Polygon | Legenda achtergrond | Ja |
| `Grenslaag_legende.qml` | Line | Grenzen in legenda | Ja |
| `stijl_puntlaag_legende.qml` | Point | Punt-voorbeelden legenda | Ja |
| `stijl_lijnlaag_legende.qml` | Line | Lijn-voorbeelden legenda | Ja |
| `stijl_polygoonlaag_legende.qml` | Polygon | Polygon-voorbeelden legenda | Ja |

---

## 💡 Tips voor Gebruik

### Algemeen
1. **Test eerst met kleine dataset** - stijlen kunnen er anders uitzien op grote schaal
2. **Bewaar aangepaste stijlen** - geef ze duidelijke namen
3. **Gebruik consistente kleuren** - door hele project
4. **Documenteer wijzigingen** - vooral als je stijlen deelt

### Voor Tactiele Kaarten Specifiek
1. **Contrast is belangrijker dan kleur** - denk in hoogteverschillen
2. **Vermijd te veel detail** - houdt het simpel en voelbaar
3. **Test met gebruikers** - indien mogelijk
4. **Denk aan printbeperkingen** - te dunne features printen niet goed

---

## ❓ Veelgestelde Vragen

**Q: Kan ik een stijl herbruiken voor een ander laagtype?**  
A: Nee, een polygon-stijl werkt niet op een lijn-laag. Je moet een nieuwe stijl maken voor elk laagtype.

**Q: Waarom zijn er aparte legenda-stijlen?**  
A: Legenda-elementen hebben vaak vaste groottes en vereenvoudigde weergave, terwijl kaart-elementen schaal-afhankelijk kunnen zijn.

**Q: Kan ik deze stijlen in andere QGIS projecten gebruiken?**  
A: Ja! Importeer ze via Style Manager of laad ze handmatig via Layer Properties → Symbology → Style → Load Style.

**Q: Hoe maak ik een stijl geschikt voor 3D-printing?**  
A: Focus op:
- Duidelijke hoogteverschillen (min. 0.5mm)
- Voldoende lijndiktes (min. 1.5mm)
- Geen te complexe patronen
- Test altijd eerst op kleine schaal

---

**Meer informatie:** Zie de [Gebruikershandleiding](../docs/user_guide.md) voor praktische voorbeelden.
