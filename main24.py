from abc import ABC, abstractmethod

class EstadoEdificio(ABC):
    @abstractmethod
    def descripcion(self):
        pass

class Hospital(EstadoEdificio):
    def descripcion(self):
        return "Edificio funcionando como Hospital"

class Escuela(EstadoEdificio):
    def descripcion(self):
        return "Edificio funcionando como Escuela"

class Vivienda(EstadoEdificio):
    def descripcion(self):
        return "Edificio funcionando como Vivienda"

class Edificio:
    def __init__(self):
        self.estados = []

    def agregar_estado(self, estado: EstadoEdificio):
        if estado not in self.estados:
            self.estados.append(estado)

    def quitar_estado(self, estado: EstadoEdificio):
        if estado in self.estados:
            self.estados.remove(estado)

    def mostrar_estados(self):
        return [estado.descripcion() for estado in self.estados]

# Ejemplo de uso
if __name__ == "__main__":
    edificio = Edificio()
    edificio.agregar_estado(Hospital())
    edificio.agregar_estado(Escuela())
    print(edificio.mostrar_estados())  # ['Edificio funcionando como Hospital', 'Edificio funcionando como Escuela']
    edificio.agregar_estado(Vivienda())
    print(edificio.mostrar_estados())  # ['Edificio funcionando como Hospital', 'Edificio funcionando como Escuela', 'Edificio funcionando como Vivienda']
    edificio.quitar_estado(Escuela())
    print(edificio.mostrar_estados())  # ['Edificio funcionando como Hospital', 'Edificio funcionando como Vivienda']