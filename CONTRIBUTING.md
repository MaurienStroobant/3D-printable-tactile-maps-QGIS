# Bijdragen aan Tactiele Kaarten QGIS

Bedankt voor je interesse om bij te dragen! Dit document legt uit hoe je kan helpen.

## 🎯 Manieren om Bij te Dragen

### 1. Bug Reports
Heb je een probleem gevonden?
- Check eerst de [bestaande issues](https://github.com/MaurienStroobant/3D-printable-tactile-maps-QGIS/issues)
- Open een nieuwe issue met:
  - Duidelijke titel
  - QGIS versie
  - Stappen om het probleem te reproduceren
  - Screenshots indien relevant
  - Error messages (uit Log Messages panel)

### 2. Feature Requests
Heb je een idee voor een nieuwe feature?
- Open een issue met tag `enhancement`
- Beschrijf:
  - Wat je wilt kunnen doen
  - Waarom dit nuttig zou zijn
  - Eventuele alternatieven die je hebt overwogen

### 3. Documentatie
Help de documentatie te verbeteren:
- Typefouten corrigeren
- Onduidelijkheden verduidelijken
- Voorbeelden toevoegen
- Vertalingen (Engels/Nederlands)

### 4. Code Bijdragen
Wil je code bijdragen?
- Fork het project
- Maak een feature branch
- Schrijf duidelijke commit messages
- Test je wijzigingen
- Open een Pull Request

## 📝 Code Richtlijnen

### Python Code (scripts)
- Volg PEP 8 stijlgids
- Voeg docstrings toe aan functies
- Commentaar in Nederlands of Engels
- Test met minimaal QGIS 3.28

### QGIS Models
- Gebruik duidelijke component namen
- Documenteer complexe stappen
- Test met verschillende datasets
- Check backwards compatibility

### Stijlbestanden (QML)
- Gebruik duidelijke naming
- Documenteer in STIJLEN.md
- Test op verschillende schalen
- Overweeg printability (3D)

## 🔄 Pull Request Process

1. **Fork & Clone**
   ```bash
   git clone https://github.com/[jouw-username]/3D-printable-tactile-maps-QGIS.git
   cd 3D-printable-tactile-maps-QGIS
   ```

2. **Maak een Branch**
   ```bash
   git checkout -b feature/geweldige-feature
   # of
   git checkout -b fix/bug-beschrijving
   ```

3. **Maak je Wijzigingen**
   - Houd commits klein en gefocust
   - Schrijf duidelijke commit messages

4. **Test je Code**
   - Test met verschillende QGIS versies indien mogelijk
   - Test met verschillende datasets
   - Check dat bestaande functionaliteit nog werkt

5. **Update Documentatie**
   - Update README.md indien nodig
   - Update relevante docs/ bestanden
   - Voeg entry toe aan CHANGELOG.md

6. **Push & Open PR**
   ```bash
   git push origin feature/geweldige-feature
   ```
   - Ga naar GitHub
   - Open Pull Request
   - Beschrijf wat je hebt veranderd en waarom

## ✅ Commit Message Format

Gebruik duidelijke, beschrijvende commit messages:

```
[type] Korte beschrijving (max 50 karakters)

Optionele langere beschrijving van wat er is veranderd en waarom.

- Bullet points voor details
- Verwijs naar issues: #123
```

**Types:**
- `feat`: Nieuwe feature
- `fix`: Bug fix
- `docs`: Documentatie wijzigingen
- `style`: Code stijl (formatting, geen functionaliteit)
- `refactor`: Code refactoring
- `test`: Test wijzigingen
- `chore`: Build process, dependencies, etc.

**Voorbeelden:**
```
feat: Voeg ondersteuning toe voor 8-punts braille

docs: Verbeter installatiehandleiding voor macOS

fix: Los CRS mismatch probleem op in model (#42)
```

## 🧪 Testing

### Handmatige Tests
Voor je een PR opent:
1. Test met minimaal 2 verschillende datasets
2. Test op verschillende QGIS versies (indien mogelijk)
3. Controleer dat STL export nog werkt
4. Verify braille is correct gerenderd

### Test Checklist
- [ ] Model draait zonder errors
- [ ] Python script laadt correct in Processing Toolbox
- [ ] Stijlen worden correct toegepast
- [ ] Braille rendering is correct (1.5mm punten)
- [ ] STL export werkt
- [ ] Documentatie is bijgewerkt
- [ ] Geen nieuwe warnings in Log Messages

## 📚 Documentatie Bijdragen

### Structuur
```
docs/
├── installation.md    # Installatie-instructies
├── user_guide.md      # Gebruikershandleiding
└── examples.md        # Voorbeelden (TODO)

styles/
└── STIJLEN.md        # Stijlbestanden uitleg
```

### Taal
- Primair: Nederlands
- README: Tweetalig (NL + EN)
- Code comments: Nederlands of Engels

### Formatting
- Gebruik Markdown
- Voeg headers toe voor navigatie
- Gebruik code blocks met syntax highlighting
- Voeg screenshots toe waar nuttig

## 🐛 Bug Fix Proces

1. **Reproduceer de bug**
   - Volg exact de stappen uit het issue
   - Documenteer wat je ziet vs wat je verwacht

2. **Vind de oorzaak**
   - Check Log Messages panel
   - Add debug prints indien nodig
   - Isoleer het probleem

3. **Fix & Test**
   - Maak de kleinst mogelijke wijziging
   - Test dat het probleem is opgelost
   - Test dat je niks anders hebt gebroken

4. **Document**
   - Update CHANGELOG.md
   - Voeg comment toe aan issue
   - Beschrijf de fix in je PR

## 💡 Feature Development

### Voor je begint
1. Open een issue om de feature te bespreken
2. Wacht op feedback van maintainers
3. Plan de implementatie

### Tijdens development
- Houd het simpel
- Volg bestaande code stijl
- Voeg documentatie toe
- Overweeg backwards compatibility

### Voor je PR opent
- Test grondig
- Update documentatie
- Voeg voorbeelden toe
- Check dat het past bij project visie

## 📦 Nieuwe Stijlen Toevoegen

Als je een nieuwe QML stijl wilt toevoegen:

1. **Maak de stijl**
   - Test grondig in QGIS
   - Gebruik duidelijke naming
   - Pas aan voor 3D-print optimalisatie

2. **Documenteer**
   - Voeg toe aan `styles/STIJLEN.md`
   - Beschrijf wanneer te gebruiken
   - Voeg screenshots toe indien mogelijk

3. **Test**
   - Test met verschillende laagtypen
   - Test op verschillende schalen
   - Print een test (indien mogelijk)

## ❓ Vragen?

- 💬 Open een [Discussion](https://github.com/MaurienStroobant/3D-printable-tactile-maps-QGIS/discussions)
- 🐛 Probleem? Open een [Issue](https://github.com/MaurienStroobant/3D-printable-tactile-maps-QGIS/issues)

## 🙏 Erkenning

Alle bijdragen worden gewaardeerd en erkend:
- Contributors lijst in README
- Vermelding in CHANGELOG
- Credit in commit history

Bedankt voor je bijdrage aan toegankelijke cartografie! 🗺️✨
