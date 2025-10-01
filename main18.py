class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Matrícula: {self.matricula}")

class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}")

# Ejemplo de uso
if __name__ == "__main__":
    estudiante = Estudiante("Ana", 20, "2024001")
    profesor = Profesor("Dr. López", 45, "Matemáticas")

    estudiante.mostrar_info()
    print("---")
    profesor.mostrar_info()