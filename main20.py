from typing import List

# Representación en Python del diagrama de clases UML solicitado


class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.roles: List['Rol'] = []

class Rol:
    def __init__(self, persona: Persona):
        self.persona = persona

class Responsable(Rol):
    def __init__(self, persona: Persona):
        super().__init__(persona)
        self.proyectos_dirigidos: List['Proyecto'] = []

class Tecnico(Rol):
    def __init__(self, persona: Persona):
        super().__init__(persona)
        self.proyectos_participados: List['Proyecto'] = []
        self.actuaciones_participadas: List['Actuacion'] = []

class Proyecto:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.actuaciones: List['Actuacion'] = []
        self.responsables: List[Responsable] = []
        self.tecnicos: List[Tecnico] = []

class Actuacion:
    def __init__(self, descripcion: str):
        self.descripcion = descripcion
        self.tecnicos: List[Tecnico] = []
        self.proyecto: Proyecto = None