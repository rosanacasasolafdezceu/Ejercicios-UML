from datetime import date, timedelta

class Libro:
    def __init__(self, id_libro, titulo, tematica):
        self.id_libro = id_libro
        self.titulo = titulo
        self.tematica = tematica
        self.ejemplares = 1  # cantidad de ejemplares disponibles

class Prestamo:
    def __init__(self, libro, lector, fecha_prestamo, es_empleado=False):
        self.libro = libro
        self.lector = lector
        self.fecha_prestamo = fecha_prestamo
        self.es_empleado = es_empleado
        self.plazo_max = timedelta(days=60 if es_empleado else 30)
        self.fecha_entrega = fecha_prestamo + self.plazo_max

    def esta_vencido(self, fecha_actual):
        return fecha_actual > self.fecha_entrega

class Lector:
    def __init__(self, id_lector, nombre, direccion):
        self.id_lector = id_lector
        self.nombre = nombre
        self.direccion = direccion
        self.penalizaciones = 0

    def aplicar_penalizacion(self):
        self.penalizaciones += 1

class Empleado(Lector):
    def __init__(self, id_lector, nombre, direccion, id_empleado):
        super().__init__(id_lector, nombre, direccion)
        self.id_empleado = id_empleado

class Estanteria:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.libros = []

    def agregar_libro(self, libro):
        if len(self.libros) < self.capacidad:
            self.libros.append(libro)
            return True
        return False

class Planta:
    def __init__(self, numero, estanterias):
        self.numero = numero
        self.estanterias = estanterias  # lista de Estanteria

    def capacidad_total(self):
        return sum(e.capacidad for e in self.estanterias)

class Biblioteca:
    def __init__(self, plantas):
        self.plantas = plantas  # lista de Planta
        self.lectores = []
        self.empleados = []
        self.prestamos = []

    def registrar_lector(self, lector):
        self.lectores.append(lector)

    def registrar_empleado(self, empleado):
        self.empleados.append(empleado)

    def registrar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def capacidad_total(self):
        return sum(planta.capacidad_total() for planta in self.plantas)