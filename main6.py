from datetime import date

class Persona:
    def __init__(self, nombre: str, apellido1: str, apellido2: str, fecha_nacimiento: date, sexo: str, identificacion: str):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.identificacion = identificacion

# Ejemplo de uso recogido en una "caja" (bloque de código)
if __name__ == "__main__":
    persona_ejemplo = Persona(
        nombre="Ana",
        apellido1="García",
        apellido2="López",
        fecha_nacimiento=date(1990, 5, 12),
        sexo="F",
        identificacion="12345678A"
    )
    print(f"Nombre: {persona_ejemplo.nombre}")
    print(f"Apellidos: {persona_ejemplo.apellido1} {persona_ejemplo.apellido2}")
    print(f"Fecha de nacimiento: {persona_ejemplo.fecha_nacimiento}")
    print(f"Sexo: {persona_ejemplo.sexo}")
    print(f"Identificación: {persona_ejemplo.identificacion}")