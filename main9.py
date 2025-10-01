from enum import Enum, auto

class Cuadro(Enum):
    LAS_MENINAS = auto()
    LA_GIOCONDA = auto()
    EL_GRITO = auto()
    LA_NOCHE_ESTRELLADA = auto()

class Representa(Enum):
    INFANTA_MARGARITA = auto()
    MONA_LISA = auto()
    EDVARD_MUNCH = auto()
    VAN_GOGH = auto()

class Pintor(Enum):
    VELAZQUEZ = auto()
    DA_VINCI = auto()
    MUNCH = auto()
    VAN_GOGH = auto()

class Lugar(Enum):
    MADRID = auto()
    PARIS = auto()
    OSLO = auto()
    AMSTERDAM = auto()

class Copias(Enum):
    SI = auto()
    NO = auto()

class Tecnica(Enum):
    OLEO = auto()
    TEMPLE = auto()
    PASTEL = auto()

class Material(Enum):
    LIENZO = auto()
    TABLA = auto()
    PAPEL = auto()

class Conservacion(Enum):
    EXCELENTE = auto()
    BUENA = auto()
    REGULAR = auto()
    MALA = auto()

class ObraArte:
    def __init__(self, cuadro, representa, pintor, lugar, copias, tecnica, material, ubicacion, conservacion):
        self.cuadro = cuadro
        self.representa = representa
        self.pintor = pintor
        self.lugar = lugar
        self.copias = copias
        self.tecnica = tecnica
        self.material = material
        self.ubicacion = ubicacion
        self.conservacion = conservacion

    def mostrar_info(self):
        print("╔════════════════════════════════════════════════╗")
        print(f"║ Cuadro:        {self.cuadro.name.replace('_', ' ').title():30}║")
        print(f"║ Representa:    {self.representa.name.replace('_', ' ').title():30}║")
        print(f"║ Pintor:        {self.pintor.name.replace('_', ' ').title():30}║")
        print(f"║ Pintado en:    {self.lugar.name.replace('_', ' ').title():30}║")
        print(f"║ ¿Copias?:      {self.copias.name.title():30}║")
        print(f"║ Técnica:       {self.tecnica.name.title():30}║")
        print(f"║ Material:      {self.material.name.title():30}║")
        print(f"║ Ubicación:     {self.ubicacion:30}║")
        print(f"║ Conservación:  {self.conservacion.name.title():30}║")
        print("╚════════════════════════════════════════════════╝")

# Ejemplo de uso:
obra = ObraArte(
    cuadro=Cuadro.LAS_MENINAS,
    representa=Representa.INFANTA_MARGARITA,
    pintor=Pintor.VELAZQUEZ,
    lugar=Lugar.MADRID,
    copias=Copias.SI,
    tecnica=Tecnica.OLEO,
    material=Material.LIENZO,
    ubicacion="Museo del Prado, Madrid",
    conservacion=Conservacion.EXCELENTE
)

obra.mostrar_info()