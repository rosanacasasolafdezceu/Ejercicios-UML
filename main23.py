from abc import ABC, abstractmethod
from typing import List

class Construccion(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass

class Edificio(Construccion):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print('  ' * nivel + f'Edificio: {self.nombre}')

class ConjuntoConstruido(Construccion):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.componentes: List[Construccion] = []

    def agregar(self, componente: Construccion):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print('  ' * nivel + f'Conjunto: {self.nombre}')
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

# Ejemplo de uso:
if __name__ == "__main__":
    edificio1 = Edificio("Edificio A")
    edificio2 = Edificio("Edificio B")
    conjunto = ConjuntoConstruido("Conjunto Residencial")
    conjunto.agregar(edificio1)
    conjunto.agregar(edificio2)

    conjunto.mostrar()