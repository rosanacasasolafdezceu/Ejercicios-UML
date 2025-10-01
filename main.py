# Ejercicio 1. Definición de clases para cada figura geométrica

class Circulo:
    def __init__(self, color, diametro):
        self.color = color
        self.diametro = diametro

class Rectangulo:
    def __init__(self, color, longitud, anchura):
        self.color = color
        self.longitud = longitud
        self.anchura = anchura

class Cuadrado:
    def __init__(self, color, lado):
        self.color = color
        self.lado = lado

class Obalo:
    def __init__(self, color, eje_mayor, eje_menor):
        self.color = color
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

# Soluciones tentativas (objetos con valores)
c1 = Circulo(color="gris", diametro=1)
r1 = Rectangulo(color="naranja", longitud=2, anchura=1)
q1 = Cuadrado(color="azul", lado=1)
o1 = Obalo(color="amarillo", eje_mayor=2, eje_menor=1)

# Ejemplo de impresión de los objetos
print(f"c1: Circulo. color: {c1.color}. diámetro={c1.diametro}")
print(f"r1: Rectángulo. color: {r1.color}. longitud={r1.longitud}. anchura={r1.anchura}")
print(f"q1: Cuadrado. color: {q1.color}. lado={q1.lado}")
print(f"o1: Óvalo. color: {o1.color}. eje mayor={o1.eje_mayor}. eje menor={o1.eje_menor}")