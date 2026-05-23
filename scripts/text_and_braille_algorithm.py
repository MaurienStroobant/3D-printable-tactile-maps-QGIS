# -*- coding: utf-8 -*-
"""
Tekst + Braille combineren in één vectorlaag — geen externe plugins vereist.

Installatie: kopieer dit bestand naar je QGIS Processing scripts map.
  Windows : C:/Users/<naam>/AppData/Roaming/QGIS/QGIS3/profiles/default/processing/scripts/
  Linux/Mac: ~/.local/share/QGIS/QGIS3/profiles/default/processing/scripts/

Herstart daarna QGIS of klik op Refresh in de Processing Toolbox.
"""

from qgis.core import (
    Qgis,
    QgsFeature,
    QgsFeatureSink,
    QgsField,
    QgsFields,
    QgsGeometry,
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingException,
    QgsProcessingParameterCrs,
    QgsProcessingParameterEnum,
    QgsProcessingParameterFeatureSink,
    QgsProcessingParameterNumber,
    QgsProcessingParameterString,
)
from qgis.PyQt.QtCore import QCoreApplication, QMetaType
from qgis.PyQt.QtGui import QFont, QFontMetrics, QPainterPath, QTransform

FONT_FAMILY = "Arial"

# ── braille-tabel ─────────────────────────────────────────────────────────────
# Braille-standaard: 6-punts raster, 2 kolommen x 3 rijen
# Puntindeling:  1 4
#                2 5
#                3 6
# Elke letter is een tuple van puntnummers die actief zijn.
# Afmetingen in tienden van millimeter (conform ISO 11548-1):
#   puntdiameter  : 1.5  mm  → 15
#   horizontale stap (dx): 2.5  mm  → 25
#   verticale stap   (dy): 2.5  mm  → 25
#   celbreedte          : 6.0  mm  → 60
#   celhoogte           : 10.0 mm  → 100

BRAILLE_DIM = {
    "dot_radius": 7.5,  # straal van elk punt (tienden mm) → diameter 1,5 mm (ISO 11548-1)
    "dx": 25,           # horizontale afstand tussen punt 1 en 4 (2,5 mm)
    "dy": 25,           # verticale afstand tussen puntrijen (2,5 mm)
    "cell_w": 60,       # breedte per cel inclusief witruimte (6,0 mm)
    "cell_h": 100,      # hoogte per cel (10,0 mm)
}

# Punt-coördinaten binnen een cel, relatief aan linksonder van de cel
# Punt 1=linksboven, 2=linksmidden, 3=linksonder, 4=rechtsboven, 5=rechtsmidden, 6=rechtsonder
def _dot_positions():
    dx = BRAILLE_DIM["dx"]
    dy = BRAILLE_DIM["dy"]
    return {
        1: (0,    2 * dy),
        2: (0,    1 * dy),
        3: (0,    0),
        4: (dx,   2 * dy),
        5: (dx,   1 * dy),
        6: (dx,   0),
    }

DOT_POS = _dot_positions()

# Braille-alfabet (grade 1, basis Latijns alfabet + cijfers + spatie)
BRAILLE_MAP = {
    'a': (1,),
    'b': (1, 2),
    'c': (1, 4),
    'd': (1, 4, 5),
    'e': (1, 5),
    'f': (1, 2, 4),
    'g': (1, 2, 4, 5),
    'h': (1, 2, 5),
    'i': (2, 4),
    'j': (2, 4, 5),
    'k': (1, 3),
    'l': (1, 2, 3),
    'm': (1, 3, 4),
    'n': (1, 3, 4, 5),
    'o': (1, 3, 5),
    'p': (1, 2, 3, 4),
    'q': (1, 2, 3, 4, 5),
    'r': (1, 2, 3, 5),
    's': (2, 3, 4),
    't': (2, 3, 4, 5),
    'u': (1, 3, 6),
    'v': (1, 2, 3, 6),
    'w': (2, 4, 5, 6),
    'x': (1, 3, 4, 6),
    'y': (1, 3, 4, 5, 6),
    'z': (1, 3, 5, 6),
    ' ': (),  # spatie = lege cel

    # Geaccentueerde letters — gebaseerd op internationaal gangbare
    # Westeuropese braillestandaarden (o.a. compatibel met Nederlands en Frans).
    # Voor minder gangbare talen kunnen deze cellen afwijken van de
    # officiële nationale standaard.
    'à': (1, 2, 3, 5, 6),
    'á': (1, 2, 3, 5, 6),
    'â': (1, 6),
    'ã': (3, 4, 5),
    'ä': (3, 4, 5),
    'å': (3, 4, 5, 6),
    'æ': (3, 4, 6),
    'ç': (1, 2, 3, 4, 6),
    'è': (2, 3, 4, 6),
    'é': (1, 2, 3, 4, 5),
    'ê': (1, 2, 6),
    'ë': (1, 2, 4, 6),
    'ì': (3, 4),
    'í': (3, 4),
    'î': (1, 4, 6),
    'ï': (1, 2, 4, 5, 6),
    'ð': (2, 3, 4, 5, 6),
    'ñ': (1, 2, 4, 5, 6),
    'ò': (3, 4, 6),
    'ó': (3, 4, 6),
    'ô': (1, 4, 5, 6),
    'õ': (1, 3, 4, 6),
    'ö': (2, 4, 6),
    'ø': (2, 4, 6),
    'ù': (2, 3, 4, 5, 6),
    'ú': (2, 3, 4, 5, 6),
    'û': (1, 5, 6),
    'ü': (1, 2, 5, 6),
    'ý': (1, 3, 4, 5, 6),
    'þ': (2, 3, 4, 6),
    'ÿ': (1, 3, 4, 5, 6),
    'œ': (2, 4, 6),
    'ß': (2, 3, 4, 6),
}

# Cijfers gebruiken dezelfde puntpatronen als a-j, maar worden
# voorafgegaan door het cijferteken (punten 3, 4, 5, 6).
# Na een spatie of aan het begin van een cijferreeks wordt het
# cijferteken opnieuw geplaatst. Binnen een aaneengesloten reeks
# cijfers wordt het cijferteken maar éénmaal geplaatst.
CIJFERTEKEN = (3, 4, 5, 6)

CIJFER_MAP = {
    '1': (1,),
    '2': (1, 2),
    '3': (1, 4),
    '4': (1, 4, 5),
    '5': (1, 5),
    '6': (1, 2, 4),
    '7': (1, 2, 4, 5),
    '8': (1, 2, 5),
    '9': (2, 4),
    '0': (2, 4, 5),
}

# Layout-opties
LAYOUT_BRAILLE_BOVEN  = 0
LAYOUT_TEKST_BOVEN    = 1
LAYOUT_BRAILLE_LINKS  = 2
LAYOUT_BRAILLE_RECHTS = 3


# ── braille → polygonen ───────────────────────────────────────────────────────

def _render_dots(dot_list, x_offset, r, segments, all_geoms):
    """Voeg de puntpolygonen voor één cel toe aan all_geoms."""
    import math
    for dot_num in dot_list:
        cx, cy = DOT_POS[dot_num]
        cx += x_offset
        pts = []
        for i in range(segments):
            angle = 2 * math.pi * i / segments
            pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
        pts.append(pts[0])
        coords = ", ".join(f"{x:.4f} {y:.4f}" for x, y in pts)
        g = QgsGeometry.fromWkt(f"POLYGON(({coords}))")
        if g and not g.isNull():
            all_geoms.append(g)


def braille_to_geometry(text):
    """
    Zet tekst om naar braille-puntpolygonen (cirkels als veelhoeken).

    Cijfers worden correct voorafgegaan door het cijferteken (punten 3,4,5,6).
    Het cijferteken wordt één keer geplaatst bij het begin van een
    aaneengesloten reeks cijfers; na een spatie of letter begint een
    nieuwe reeks en wordt het cijferteken opnieuw geplaatst.

    Geeft (QgsGeometry | None, lijst_onbekende_tekens) terug.
    """
    r        = BRAILLE_DIM["dot_radius"]
    cell_w   = BRAILLE_DIM["cell_w"]
    segments = 32  # hogere waarde = rondere cirkels

    errors    = []
    all_geoms = []
    col       = 0
    in_cijferreeks = False

    for char in text:
        lower = char.lower()

        if char == ' ':
            col += 1
            in_cijferreeks = False
            continue

        if lower in CIJFER_MAP:
            if not in_cijferreeks:
                _render_dots(CIJFERTEKEN, col * cell_w, r, segments, all_geoms)
                col += 1
                in_cijferreeks = True
            _render_dots(CIJFER_MAP[lower], col * cell_w, r, segments, all_geoms)
            col += 1

        elif lower in BRAILLE_MAP:
            in_cijferreeks = False
            _render_dots(BRAILLE_MAP[lower], col * cell_w, r, segments, all_geoms)
            col += 1

        else:
            errors.append(repr(char))
            in_cijferreeks = False
            col += 1

    if not all_geoms:
        return None, errors

    combined = QgsGeometry.collectGeometry(all_geoms)
    if combined and not combined.isNull():
        combined = combined.makeValid()
    return (combined if combined and not combined.isNull() else None), errors
    return (combined if combined and not combined.isNull() else None), errors


# ── tekst → polygonen ─────────────────────────────────────────────────────────

def rings_to_polygons_with_holes(subpath_polys):
    if not subpath_polys:
        return []

    geoms, ring_pts = [], []
    for poly in subpath_polys:
        pts = [(p.x(), p.y()) for p in poly]
        if pts and pts[0] != pts[-1]:
            pts.append(pts[0])
        if len(pts) < 4:
            continue
        coords = ", ".join(f"{x:.6f} {y:.6f}" for x, y in pts)
        g = QgsGeometry.fromWkt(f"POLYGON(({coords}))")
        if g and not g.isNull():
            geoms.append(g)
            ring_pts.append(pts)

    n = len(geoms)
    if n == 0:
        return []
    if n == 1:
        return [geoms[0]]

    is_hole_of = [None] * n
    for j in range(n):
        for i in range(n):
            if i == j:
                continue
            if geoms[i].contains(geoms[j]):
                if is_hole_of[j] is None or geoms[i].area() < geoms[is_hole_of[j]].area():
                    is_hole_of[j] = i

    holes_for = {i: [] for i in range(n)}
    outer_indices = []
    for j in range(n):
        if is_hole_of[j] is not None:
            holes_for[is_hole_of[j]].append(ring_pts[j])
        else:
            outer_indices.append(j)

    result = []
    for i in outer_indices:
        outer_coords = ", ".join(f"{x:.6f} {y:.6f}" for x, y in ring_pts[i])
        rings = [f"({outer_coords})"]
        for hole_pts in holes_for[i]:
            rings.append("(" + ", ".join(f"{x:.6f} {y:.6f}" for x, y in hole_pts) + ")")
        g = QgsGeometry.fromWkt("POLYGON(" + ", ".join(rings) + ")")
        if g and not g.isNull():
            result.append(g)
    return result


def text_to_geometry(text, font_size_pt=72.0, letter_spacing=0.0):
    font = QFont(FONT_FAMILY, int(font_size_pt))
    font.setPixelSize(int(font_size_pt * 1.333))
    fm = QFontMetrics(font)

    errors, all_geoms = [], []
    x_cursor = 0.0

    for char in text:
        if char == " ":
            x_cursor += fm.horizontalAdvance(" ") + letter_spacing
            continue
        char_path = QPainterPath()
        char_path.addText(0, 0, font, char)
        if char_path.isEmpty():
            errors.append(repr(char))
            x_cursor += fm.horizontalAdvance(char) + letter_spacing
            continue

        t = QTransform()
        t.translate(x_cursor, 0)
        t.scale(1.0, -1.0)  # Y-as spiegelen
        char_path = t.map(char_path)

        all_geoms.extend(rings_to_polygons_with_holes(
            char_path.toSubpathPolygons(QTransform())
        ))
        x_cursor += fm.horizontalAdvance(char) + letter_spacing

    if not all_geoms:
        return None, errors
    combined = QgsGeometry.collectGeometry(all_geoms)
    if combined and not combined.isNull():
        combined = combined.makeValid()
    return (combined if combined and not combined.isNull() else None), errors
    return (combined if combined and not combined.isNull() else None), errors


# ── positionering ─────────────────────────────────────────────────────────────

def translate_geom(geom, dx, dy):
    g = QgsGeometry(geom)
    g.translate(dx, dy)
    return g


def combine_layouts(geom_braille, geom_tekst, layout, gap):
    """
    Positioneert braille en tekst ten opzichte van elkaar.
    Beide worden verschoven zodat de combinatie start op (0, 0).
    """
    bb_b = geom_braille.boundingBox()
    bb_t = geom_tekst.boundingBox()

    w_b = bb_b.xMaximum() - bb_b.xMinimum()
    h_b = bb_b.yMaximum() - bb_b.yMinimum()
    h_t = bb_t.yMaximum() - bb_t.yMinimum()

    if layout == LAYOUT_BRAILLE_BOVEN:
        # Braille onderkant op y = h_t + gap, tekst onderkant op y = 0
        dy_b = (h_t + gap) - bb_b.yMinimum()
        dy_t = -bb_t.yMinimum()
        dx_b = -bb_b.xMinimum()
        dx_t = -bb_t.xMinimum()

    elif layout == LAYOUT_TEKST_BOVEN:
        # Tekst onderkant op y = h_b + gap, braille onderkant op y = 0
        dy_t = (h_b + gap) - bb_t.yMinimum()
        dy_b = -bb_b.yMinimum()
        dx_b = -bb_b.xMinimum()
        dx_t = -bb_t.xMinimum()

    elif layout == LAYOUT_BRAILLE_LINKS:
        # Braille linkerkant op x = 0, tekst linkerkant op x = w_b + gap
        dx_b = -bb_b.xMinimum()
        dx_t = w_b + gap - bb_t.xMinimum()
        dy_b = -bb_b.yMinimum()
        dy_t = -bb_t.yMinimum()

    else:  # LAYOUT_BRAILLE_RECHTS
        w_t = bb_t.xMaximum() - bb_t.xMinimum()
        # Tekst linkerkant op x = 0, braille linkerkant op x = w_t + gap
        dx_t = -bb_t.xMinimum()
        dx_b = w_t + gap - bb_b.xMinimum()
        dy_b = -bb_b.yMinimum()
        dy_t = -bb_t.yMinimum()

    return translate_geom(geom_braille, dx_b, dy_b), translate_geom(geom_tekst, dx_t, dy_t)


# ── Processing algoritme ──────────────────────────────────────────────────────

class TextAndBraille(QgsProcessingAlgorithm):

    TEXT           = "TEXT"
    FONT_SIZE      = "FONT_SIZE"
    LETTER_SPACING = "LETTER_SPACING"
    LAYOUT         = "LAYOUT"
    CRS            = "CRS"
    OUTPUT         = "OUTPUT"

    LAYOUT_OPTIONS = [
        "Braille boven, tekst onder",
        "Tekst boven, braille onder",
        "Braille links, tekst rechts",
        "Tekst links, braille rechts",
    ]

    def tr(self, s):
        return QCoreApplication.translate("TextAndBraille", s)

    def createInstance(self):
        return TextAndBraille()

    def name(self):
        return "textandbraille"

    def displayName(self):
        return self.tr("Tekst en Braille combineren")

    def group(self):
        return self.tr("Tekst gereedschappen")

    def groupId(self):
        return "tekstgereedschappen"

    def shortHelpString(self):
        return self.tr(
            """
            Genereert een vectorlaag met zowel de gewone tekst (Arial, polygonen
            met echte gaten) als de bijbehorende brailletekst.

            De twee worden naast of onder elkaar geplaatst met een tussenruimte
            van 1x de letterhoogte. Kies de gewenste layout via de parameter.

            Geen externe plugins vereist.
            Als er geen tekst wordt opgegeven is de uitvoer null.

            Cijfers worden voorafgegaan door het cijferteken (punten 3,4,5,6).
            Geaccentueerde letters (e-accent, u-umlaut, c-cedille, ...) zijn
            opgenomen op basis van de internationale UEB-standaard. Voor minder
            gangbare talen kunnen deze braillecellen afwijken van de officiele
            nationale standaard.
            """
        )

    def shortDescription(self):
        return self.tr("Combineert gewone tekst en braille in één laag.")

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterString(
            self.TEXT, self.tr("Invoertekst"),
            multiLine=False, optional=True
        ))
        self.addParameter(QgsProcessingParameterNumber(
            self.FONT_SIZE, self.tr("Lettergrootte tekst (pt)"),
            type=QgsProcessingParameterNumber.Double,
            defaultValue=72.0, minValue=4.0, maxValue=1000.0
        ))
        self.addParameter(QgsProcessingParameterNumber(
            self.LETTER_SPACING, self.tr("Extra spatering tekst (px)"),
            type=QgsProcessingParameterNumber.Double,
            defaultValue=0.0, minValue=-200.0, maxValue=500.0
        ))
        self.addParameter(QgsProcessingParameterEnum(
            self.LAYOUT, self.tr("Layout"),
            options=self.LAYOUT_OPTIONS,
            defaultValue=0
        ))
        self.addParameter(QgsProcessingParameterCrs(
            self.CRS, self.tr("Coordinatenstelsel"),
            defaultValue="EPSG:31370"
        ))
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT, self.tr("Tekst en Braille"),
            type=QgsProcessing.TypeVectorPolygon,
            defaultValue=QgsProcessing.TEMPORARY_OUTPUT
        ))

    def processAlgorithm(self, parameters, context, feedback):
        input_text = self.parameterAsString(parameters, self.TEXT, context)
        font_size  = self.parameterAsDouble(parameters, self.FONT_SIZE, context)
        spacing    = self.parameterAsDouble(parameters, self.LETTER_SPACING, context)
        layout     = self.parameterAsEnum(parameters, self.LAYOUT, context)
        crs        = self.parameterAsCrs(parameters, self.CRS, context)

        fields = QgsFields()
        fields.append(QgsField("id",   QMetaType.Type.Int))
        fields.append(QgsField("type", QMetaType.Type.QString))
        fields.append(QgsField("text", QMetaType.Type.QString))

        (sink, dest_id) = self.parameterAsSink(
            parameters=parameters,
            name=self.OUTPUT,
            context=context,
            fields=fields,
            geometryType=Qgis.WkbType.MultiPolygon,
            crs=crs,
        )
        if sink is None:
            raise QgsProcessingException(self.invalidSinkError(parameters, self.OUTPUT))

        # Lege invoer → twee null-features
        if not input_text or not input_text.strip():
            feedback.pushInfo(self.tr("Geen tekst opgegeven, uitvoer is null."))
            for fid, ftype in [(1, "tekst"), (2, "braille")]:
                feat = QgsFeature(fields)
                feat["id"]   = fid
                feat["type"] = ftype
                feat["text"] = None
                feat.setGeometry(QgsGeometry())
                sink.addFeature(feat, QgsFeatureSink.Flag.FastInsert)
            return {self.OUTPUT: dest_id}

        feedback.pushInfo(f"Renderen tekst: '{input_text}'")
        geom_tekst, tekst_errors = text_to_geometry(
            text=input_text,
            font_size_pt=font_size,
            letter_spacing=spacing,
        )
        if tekst_errors:
            feedback.pushWarning(f"Tekst — overgeslagen tekens: {tekst_errors}")

        feedback.pushInfo(f"Renderen braille: '{input_text}'")
        geom_braille, braille_errors = braille_to_geometry(input_text)
        if braille_errors:
            feedback.pushWarning(f"Braille — onbekende tekens: {braille_errors}")

        # Positioneren als beide beschikbaar zijn
        if geom_tekst and not geom_tekst.isNull() \
                and geom_braille and not geom_braille.isNull():
            bb_t = geom_tekst.boundingBox()
            gap  = bb_t.yMaximum() - bb_t.yMinimum()  # 1× letterhoogte
            geom_braille, geom_tekst = combine_layouts(
                geom_braille, geom_tekst, layout, gap
            )

        for fid, ftype, geom in [
            (1, "braille", geom_braille),
            (2, "tekst",   geom_tekst),
        ]:
            feat = QgsFeature(fields)
            feat["id"]   = fid
            feat["type"] = ftype
            feat["text"] = input_text
            feat.setGeometry(geom if geom and not geom.isNull() else QgsGeometry())
            sink.addFeature(feat, QgsFeatureSink.Flag.FastInsert)

        feedback.pushInfo(self.tr("Klaar."))
        return {self.OUTPUT: dest_id}
