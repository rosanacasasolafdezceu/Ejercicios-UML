from graphviz import Digraph

# Clases para representar los objetos
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
        self.copia_de = None
        self.realizada_por = None

class Estudio:
    def __init__(self, lugar, conclusion):
        self.lugar = lugar
        self.conclusion = conclusion

# Objetos
gioconda_original = Obra(
    nombre="La Gioconda original",
    autor="Leonardo Da Vinci",
    cronologia="1503-1516",
    tecnica="óleo",
    subtecnica="sfumato",
    material="madera de álamo",
    estado="peor que réplica",
    ubicacion="Museo Louvre"
)

replica_gioconda = Obra(
    nombre="Réplica La Gioconda",
    autor="Anónimo",
    cronologia="1503-1516",
    tecnica="óleo",
    subtecnica="pincelada simple",
    material="madera de nogal",
    estado="mejor que original",
    ubicacion="Museo del Prado",
    procedencia="Colecciones Reales"
)

replica_gioconda.copia_de = gioconda_original
replica_gioconda.realizada_por = "Alumno de escuela de Leonardo"

estudio_prado = Estudio(
    lugar="Museo del Prado",
    conclusion="Realizada por alumno contemporáneo a Leonardo"
)

# Diagrama de objetos con cajas y flechas
dot = Digraph(comment='Diagrama de Objetos La Gioconda')

# Cajas (objetos)
dot.node('O1', 'Obra\n"La Gioconda original"\nAutor: Leonardo Da Vinci\nTécnica: óleo/sfumato\nMaterial: álamo\nUbicación: Louvre')
dot.node('O2', 'Obra\n"Réplica La Gioconda"\nAutor: Anónimo\nTécnica: óleo/pincelada simple\nMaterial: nogal\nUbicación: Prado\nProcedencia: Colecciones Reales')
dot.node('E1', 'Estudio\nLugar: Museo del Prado\nConclusión: Realizada por alumno contemporáneo a Leonardo')

# Flechas (relaciones)
dot.edge('O2', 'O1', label='copia_de')
dot.edge('O2', 'E1', label='estudiada_en')
dot.edge('O2', 'O2', label='realizada_por: alumno de escuela de Leonardo', style='dashed')

# Guardar y mostrar el diagrama
dot.render('/workspaces/Ejercicios-UML/diagrama_objetos_gioconda', format='png', view=False)

print("Diagrama generado: /workspaces/Ejercicios-UML/diagrama_objetos_gioconda.png")
print("Puedes abrirlo con:")
print('$BROWSER /workspaces/Ejercicios-UML/diagrama_objetos_gioconda.png')

# Mostrar información en consola
def mostrar_obra(obra):
    print(f"Obra: {obra.nombre}")
    print(f"  Autor: {obra.autor}")
    print(f"  Cronología: {obra.cronologia}")
    print(f"  Técnica: {obra.tecnica}")
    print(f"  Sub-técnica: {obra.subtecnica}")
    print(f"  Material: {obra.material}")
    print(f"  Estado: {obra.estado}")
    print(f"  Ubicación: {obra.ubicacion}")
    if obra.procedencia:
        print(f"  Procedencia: {obra.procedencia}")
    if obra.copia_de:
        print(f"  Copia de: {obra.copia_de.nombre}")
    if obra.realizada_por:
        print(f"  Realizada por: {obra.realizada_por}")
    print()

mostrar_obra(replica_gioconda)
mostrar_obra(gioconda_original)
print(f"Estudio en {estudio_prado.lugar}: {estudio_prado.conclusion}")