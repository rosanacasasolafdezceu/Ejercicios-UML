# Ejemplo de diagrama UML usando texto (cajas y flechas) para mostrar asociaciones entre clases.
# Supongamos que en el Ejercicio 7 tienes estas clases:
# - Persona
# - Libro
# - Biblioteca

# Aquí tienes una representación UML en texto:

+-----------+        +-----------+        +-------------+
|  Persona  |<------>|   Libro   |<------>|  Biblioteca |
+-----------+        +-----------+        +-------------+
    |                   ^                     |
    |                   |                     |
    +-------------------+---------------------+

# Asociaciones:
# - Una Persona puede tener varios Libros (flecha de Persona a Libro).
# - Un Libro pertenece a una Biblioteca (flecha de Libro a Biblioteca).
# - Una Biblioteca puede tener varios Libros (flecha de Biblioteca a Libro).

# Si quieres el código Python con las asociaciones, sería algo así:

class Libro:
    def __init__(self, titulo, autor):
      self.titulo = titulo
      self.autor = autor

class Persona:
    def __init__(self, nombre):
      self.nombre = nombre
      self.libros = []  # Asociación: Persona tiene Libros

    def agregar_libro(self, libro):
      self.libros.append(libro)

class Biblioteca:
    def __init__(self, nombre):
      self.nombre = nombre
      self.libros = []  # Asociación: Biblioteca tiene Libros

    def agregar_libro(self, libro):
      self.libros.append(libro)

# Ejemplo de uso:
biblioteca = Biblioteca("Central")
libro1 = Libro("1984", "George Orwell")
libro2 = Libro("El Quijote", "Miguel de Cervantes")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

persona = Persona("Juan")
persona.agregar_libro(libro1)

# Así se representan las asociaciones entre las clases.