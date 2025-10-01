# Definición textual de las clases según el modelo UML propuesto

class Proyecto:
    """
    Representa un proyecto en el que se participa.
    Características:
    - nombre: Nombre del proyecto.
    - descripcion: Breve descripción del proyecto.
    - miembros: Lista de miembros del equipo que participan.
    - lugar_actuacion: Lugar donde se desarrolla el proyecto.
    """
    def __init__(self, nombre, descripcion, lugar_actuacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.miembros = []
        self.lugar_actuacion = lugar_actuacion

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

class MiembroDelEquipo:
    """
    Representa a un miembro del equipo de trabajo.
    Características:
    - nombre: Nombre del miembro.
    - profesion: Profesión o rol dentro del equipo.
    - experiencia: Años de experiencia profesional.
    """
    def __init__(self, nombre, profesion, experiencia):
        self.nombre = nombre
        self.profesion = profesion
        self.experiencia = experiencia

class LugarDeActuacion:
    """
    Representa el lugar donde se desarrolla el proyecto.
    Características:
    - nombre: Nombre del lugar (ciudad, país, empresa, remoto, etc.).
    - tipo: Tipo de lugar (oficina, remoto, cliente, etc.).
    """
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

# Ejemplo de uso
if __name__ == "__main__":
    lugar = LugarDeActuacion("Madrid", "Oficina")
    proyecto = Proyecto("Sistema de Gestión", "Desarrollo de software para gestión empresarial", lugar)
    miembro1 = MiembroDelEquipo("Ana", "Desarrolladora", 5)
    miembro2 = MiembroDelEquipo("Luis", "Analista", 8)
    proyecto.agregar_miembro(miembro1)
    proyecto.agregar_miembro(miembro2)

    print(f"Proyecto: {proyecto.nombre}")
    print(f"Descripción: {proyecto.descripcion}")
    print(f"Lugar de actuación: {proyecto.lugar_actuacion.nombre} ({proyecto.lugar_actuacion.tipo})")
    print("Miembros del equipo:")
    for m in proyecto.miembros:
        print(f"- {m.nombre}, {m.profesion}, {m.experiencia} años de experiencia")