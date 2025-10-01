from graphviz import Digraph

class EstructuraArqueologica:
    def __init__(self, codigo, datacion, materiales):
        self.codigo = codigo
        self.datacion = datacion
        self.materiales = materiales
        self.subestructuras = []

    def agregar_subestructura(self, subestructura):
        self.subestructuras.append(subestructura)

    def __str__(self):
        return f"{self.codigo} ({self.datacion})"

# Diagrama de clases
dot = Digraph(comment='Diagrama de Clases EstructuraArqueologica')

dot.node('EstructuraArqueologica', '''EstructuraArqueologica
--------------------------
- codigo: str
- datacion: str
- materiales: list
- subestructuras: list
+ agregar_subestructura()
+ __str__()''')

dot.edge('EstructuraArqueologica', 'EstructuraArqueologica', label='compuesta por', arrowhead='vee')

dot.render('estructura_arqueologica_diagrama', format='png', view=True)