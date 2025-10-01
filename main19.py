from typing import List, Optional

class Museo:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.colecciones: List[Coleccion] = []
        self.salas: List[Sala] = []

    def agregar_coleccion(self, coleccion: 'Coleccion'):
        self.colecciones.append(coleccion)

    def agregar_sala(self, sala: 'Sala'):
        self.salas.append(sala)

class Coleccion:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.objetos: List[ObjetoArqueologico] = []

    def agregar_objeto(self, objeto: 'ObjetoArqueologico'):
        self.objetos.append(objeto)

class Ubicacion:
    def __init__(self, descripcion: str):
        self.descripcion = descripcion

class Sala(Ubicacion):
    def __init__(self, nombre: str, piso: int):
        super().__init__(f"Sala: {nombre}, Piso: {piso}")
        self.nombre = nombre
        self.piso = piso

class Almacen(Ubicacion):
    def __init__(self, nombre: str):
        super().__init__(f"Almacén: {nombre}")
        self.nombre = nombre

class Restauracion:
    def __init__(self, fecha: str, descripcion: str):
        self.fecha = fecha
        self.descripcion = descripcion

class ObjetoArqueologico:
    def __init__(self, nombre: str, ubicacion: Ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.restauraciones: List[Restauracion] = []

    def agregar_restauracion(self, restauracion: Restauracion):
        self.restauraciones.append(restauracion)