from typing import List

class ElementoArquitectonico:
    def __init__(self, descripcion: str, material: str):
        self.descripcion = descripcion
        self.material = material

class Portada(ElementoArquitectonico):
    def __init__(self, descripcion: str, material: str, estilo: str):
        super().__init__(descripcion, material)
        self.estilo = estilo

class Puerta(ElementoArquitectonico):
    def __init__(self, descripcion: str, material: str, ancho: float, alto: float):
        super().__init__(descripcion, material)
        self.ancho = ancho
        self.alto = alto

class Ventana(ElementoArquitectonico):
    def __init__(self, descripcion: str, material: str, tipo: str):
        super().__init__(descripcion, material)
        self.tipo = tipo

class Balcon(ElementoArquitectonico):
    def __init__(self, descripcion: str, material: str, capacidad: int):
        super().__init__(descripcion, material)
        self.capacidad = capacidad

class Fachada:
    def __init__(self, elementos: List[ElementoArquitectonico]):
        self.elementos = elementos

class Edificio:
    def __init__(self, nombre: str, direccion: str, fachada: Fachada):
        self.nombre = nombre
        self.direccion = direccion
        self.fachada = fachada

class EspacioAbierto:
    def __init__(self, nombre: str, tipo: str, edificios: List[Edificio]):
        self.nombre = nombre
        self.tipo = tipo  # 'calle' o 'plaza'
        self.edificios = edificios

class Ciudad:
    def __init__(self, nombre: str, espacios: List[EspacioAbierto]):
        self.nombre = nombre
        self.espacios = espacios