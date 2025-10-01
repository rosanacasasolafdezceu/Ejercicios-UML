# Diagrama de objetos en Python usando clases para representar la Catedral de Santiago de Compostela

class Catedral:
    def __init__(self, nombre, ubicacion, inicio_construccion, materiales, estilos, consagraciones, bien_interes_cultural):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.inicio_construccion = inicio_construccion
        self.materiales = materiales
        self.estilos = estilos
        self.consagraciones = consagraciones
        self.bien_interes_cultural = bien_interes_cultural

class Ubicacion:
    def __init__(self, ciudad, provincia, region, pais):
        self.ciudad = ciudad
        self.provincia = provincia
        self.region = region
        self.pais = pais

class Material:
    def __init__(self, tipo):
        self.tipo = tipo

class EstiloArquitectonico:
    def __init__(self, nombre):
        self.nombre = nombre

class Consagracion:
    def __init__(self, fecha):
        self.fecha = fecha

class BienInteresCultural:
    def __init__(self, fecha_declaracion):
        self.fecha_declaracion = fecha_declaracion

# Objetos
ubicacion = Ubicacion("Santiago de Compostela", "La Coruña", "Galicia", "España")
material = Material("Granito")
estilos = [
    EstiloArquitectonico("Románico"),
    EstiloArquitectonico("Gótico"),
    EstiloArquitectonico("Barroco"),
    EstiloArquitectonico("Plateresco"),
    EstiloArquitectonico("Neoclásico")
]
consagraciones = [
    Consagracion(1128),
    Consagracion("3 de abril de 1211")
]
bien_interes_cultural = BienInteresCultural(1896)

catedral = Catedral(
    nombre="Catedral de Santiago de Compostela",
    ubicacion=ubicacion,
    inicio_construccion=1075,
    materiales=[material],
    estilos=estilos,
    consagraciones=consagraciones,
    bien_interes_cultural=bien_interes_cultural
)

# Representación textual del diagrama de objetos
def mostrar_diagrama(catedral):
    print(f"[Catedral] --> {catedral.nombre}")
    print(f"  |-- [Ubicacion] --> {catedral.ubicacion.ciudad}, {catedral.ubicacion.provincia}, {catedral.ubicacion.region}, {catedral.ubicacion.pais}")
    print(f"  |-- [Inicio Construccion] --> {catedral.inicio_construccion}")
    print(f"  |-- [Materiales] --> {[m.tipo for m in catedral.materiales]}")
    print(f"  |-- [Estilos] --> {[e.nombre for e in catedral.estilos]}")
    print(f"  |-- [Consagraciones] --> {[c.fecha for c in catedral.consagraciones]}")
    print(f"  |-- [Bien de Interes Cultural] --> {catedral.bien_interes_cultural.fecha_declaracion}")

if __name__ == "__main__":
    mostrar_diagrama(catedral)