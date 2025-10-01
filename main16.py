class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.padre = None         # Asociación 0..1: una persona puede tener un padre
        self.madre = None         # Asociación 0..1: una persona puede tener una madre
        self.hijos = []           # Asociación 0..*: una persona puede tener varios hijos
        self.hermanos = []        # Asociación 0..*: una persona puede tener varios hermanos

    def agregar_padre(self, padre):
        self.padre = padre
        padre.hijos.append(self)

    def agregar_madre(self, madre):
        self.madre = madre
        madre.hijos.append(self)

    def agregar_hermano(self, hermano):
        if hermano not in self.hermanos and hermano != self:
            self.hermanos.append(hermano)
            hermano.hermanos.append(self)

    def agregar_hijo(self, hijo):
        if hijo not in self.hijos:
            self.hijos.append(hijo)
            if self not in (hijo.padre, hijo.madre):
                # Asignar rol padre/madre si no está asignado
                if self.edad > hijo.edad:
                    if not hijo.padre:
                        hijo.padre = self
                    elif not hijo.madre:
                        hijo.madre = self

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"