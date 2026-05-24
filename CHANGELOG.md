# Changelog

Alle belangrijke wijzigingen aan dit project worden gedocumenteerd in dit bestand.

## [1.0.0] - 2026-05-23

### Toegevoegd
- Initiële release van het tactiele kaarten QGIS model
- QGIS Model voor geautomatiseerde workflow (Model.model en Model.model3)
- Python script voor braille en tekst combinatie (text_and_braille_algorithm.py)
- 13 QML stijlbestanden voor consistente visualisatie:
  - Basis-, polygoon-, lijn- en puntlaag stijlen
  - Tekst en legenda stijlen
  - Schaalbalk en achtergrond stijlen
- Uitgebreide documentatie:
  - Nederlandse en Engelse README
  - Installatiehandleiding
  - Gebruikershandleiding
  - Stijlbestanden overzicht
- Installatiescripts voor Windows, Linux en macOS
- MIT Licentie

### Kenmerken
- Volledig geautomatiseerde workflow van geodata naar STL
- ISO 11548-1 conforme braille implementatie (1.5mm punten)
- Ondersteuning voor Nederlands alfabet, cijfers en geaccentueerde letters
- Metrisch coördinatensysteem voor nauwkeurige 3D-prints
- Geen externe plugins vereist (behalve STL Generator voor finale export)
- Compatibel met QGIS 3.28+

---

## Toekomstige Versies

### [Planned]
- Voorbeeldprojecten met sample data
- Video tutorials
- Extra stijl varianten (hoogcontrast, kleurenblind-vriendelijk)
- Automatische schaalberekening
- Batch processing voor meerdere kaarten
- Ondersteuning voor 8-punts braille
- Meer talen (Engels, Frans, Duits braille varianten)
- Integratie met OpenStreetMap data fetching

---

## Versie Nummering

Dit project volgt [Semantic Versioning](https://semver.org/):
- **MAJOR**: Grote wijzigingen, mogelijk niet backwards compatible
- **MINOR**: Nieuwe features, backwards compatible
- **PATCH**: Bug fixes, backwards compatible

---

## Bijdragen

Zie [README.md](README.md#bijdragen) voor informatie over hoe bij te dragen aan dit project.
