from abc import ABC, abstractmethod
from typing import List

class EntidadGeografica(ABC):
    def __init__(self, nombre: str, codigo: str):
        self.nombre = nombre
        self.codigo = codigo

class Punto(EntidadGeografica):
    def __init__(self, nombre: str, codigo: str, x: float, y: float):
        super().__init__(nombre, codigo)
        self.x = x
        self.y = y

class Linea(EntidadGeografica):
    def __init__(self, nombre: str, codigo: str, puntos: List[Punto]):
        super().__init__(nombre, codigo)
        if len(puntos) < 2:
            raise ValueError("Una línea debe tener al menos dos puntos.")
        self.puntos = puntos

class Area(EntidadGeografica):
    def __init__(self, nombre: str, codigo: str, puntos: List[Punto]):
        super().__init__(nombre, codigo)
        if len(puntos) < 3:
            raise ValueError("Un área debe tener al menos tres puntos.")
        self.puntos = puntos