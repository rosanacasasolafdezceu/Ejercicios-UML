from datetime import date

class Actuacion:
    TIPOS = ("sondeo", "excavacion", "seguimiento")

    def __init__(self, fecha_inicio: date, fecha_fin: date, tipo: str):
        if tipo not in self.TIPOS:
            raise ValueError(f"Tipo de actuación inválido: {tipo}")
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo

    def __str__(self):
        return f"Actuación: {self.fecha_inicio} - {self.fecha_fin}\nTipo de actuación: {self.tipo}"

# Ejemplo de uso mostrando en dos "cajas" (prints separados)
act = Actuacion(date(2024, 6, 1), date(2024, 6, 15), "excavacion")

print("Actuación:")
print(f"{act.fecha_inicio} - {act.fecha_fin}")
print("Tipo de actuación:")
print(act.tipo)