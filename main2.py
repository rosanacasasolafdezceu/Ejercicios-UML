# Diagrama de objetos en formato textual usando clases y relaciones

class Persona:
    def __init__(self, nombre, apellido, apellido_de_soltera=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_de_soltera = apellido_de_soltera
        self.pareja = None
        self.padre = None
        self.madre = None

# Objetos
kate = Persona("Kate", "Windsor", "Middleton")
guillermo = Persona("Guillermo", "Windsor")
carlos = Persona("Carlos", "Windsor")
diana = Persona("Diana", "Gales", "Spencer")

# Relaciones
kate.pareja = guillermo
guillermo.pareja = kate

guillermo.padre = carlos
guillermo.madre = diana

# Representación visual simple (texto)
print("""
+-------------------+      casados      +-------------------+
| Kate Windsor      |<----------------->| Guillermo Windsor |
| (nacida Middleton)|                   | de Gales          |
+-------------------+                   +-------------------+
                                              |
                                              | hijo de
                                              v
                                    +-------------------+
                                    | Carlos Windsor    |
                                    | de Gales          |
                                    +-------------------+
                                              |
                                              | hijo de
                                              v
                                    +-------------------+
                                    | Diana de Gales    |
                                    | (nacida Spencer)  |
                                    +-------------------+
""")