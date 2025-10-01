from graphviz import Digraph

# Definición de clases para el diagrama de clases
class Obra:
    def __init__(self, nombre, autor, cronologia, tecnica, subtecnica, material, estado, ubicacion, procedencia=None):
        self.nombre = nombre
        self.autor = autor
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.material = material
        self.estado = estado
        self.ubicacion = ubicacion
        self.procedencia = procedencia
        self.copia_de = None  # Asociación 0..1 a Obra
        self.realizada_por = None  # Rol: autor o alumno

class Estudio:
    def __init__(self, lugar, conclusion):
        self.lugar = lugar
        self.conclusion = conclusion

# Diagrama de clases con asociaciones, cardinalidades y roles
dot = Digraph(comment='Diagrama de Clases La Gioconda')

# Clases (cajas)
dot.node('Obra', '''Obra
----------------------
+ nombre
+ autor
+ cronologia
+ tecnica
+ subtecnica
+ material
+ estado
+ ubicacion
+ procedencia
----------------------
+ copia_de: Obra [0..1]
+ realizada_por: str
''', shape='box')

dot.node('Estudio', '''Estudio
----------------------
+ lugar
+ conclusion
''', shape='box')

# Asociaciones (flechas)
dot.edge('Obra', 'Obra', label='copia_de [0..1]', arrowhead='vee')
dot.edge('Obra', 'Estudio', label='estudiada_en [0..*]', arrowhead='vee')

# Mostrar diagrama
dot.render('diagrama_clases_gioconda', format='png', view=False)

print("Diagrama de clases generado como 'diagrama_clases_gioconda.png'.")

# Si quieres abrir el diagrama en el navegador:
# import os
# os.system('$BROWSER diagrama_clases_gioconda.png')