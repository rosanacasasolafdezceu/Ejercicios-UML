from typing import List, Optional

class Ventana:
    def __init__(self, altura: float, ancho: float, arco_doble: bool, decoracion_exterior: bool, tipo_cierre: str, vidriera_color: Optional[str] = None):
        self.altura = altura
        self.ancho = ancho
        self.arco_doble = arco_doble
        self.decoracion_exterior = decoracion_exterior
        self.tipo_cierre = tipo_cierre  # 'tela blanca', 'vidriera incolora', 'vidriera color'
        self.vidriera_color = vidriera_color  # None, 'incolora', 'color'

class Abside:
    def __init__(self, forma: str, ventanas: List[Ventana]):
        self.forma = forma  # 'semicircular'
        self.ventanas = ventanas

class Nave:
    def __init__(self, tipo: str):
        self.tipo = tipo  # 'sencilla', 'basilical'

class Crucero:
    def __init__(self, brazos_salientes: bool):
        self.brazos_salientes = brazos_salientes

class IglesiaRomanica:
    def __init__(
        self,
        importancia: str,  # 'menor', 'mayor'
        naves: List[Nave],
        crucero: Optional[Crucero],
        absides: List[Abside],
        orientacion_cabecera: str  # 'oriente'
    ):
        self.importancia = importancia
        self.naves = naves
        self.crucero = crucero
        self.absides = absides
        self.orientacion_cabecera = orientacion_cabecera