# Definición de dos triángulos que comparten un lado usando las clases dadas

from main13 import Punto, Poligono  # Asumiendo que las clases están en main13.py

# Crear puntos
A = Punto(0, 0)
B = Punto(1, 0)
C = Punto(0.5, 1)
D = Punto(1.5, 1)

# Triángulo 1: ABC
triangulo1 = Poligono()
triangulo1.add_punto(A)
triangulo1.add_punto(B)
triangulo1.add_punto(C)

# Triángulo 2: BCD (comparten el lado BC)
triangulo2 = Poligono()
triangulo2.add_punto(B)
triangulo2.add_punto(C)
triangulo2.add_punto(D)

# Mostrar los vértices de cada triángulo
print("Triángulo 1 vértices:", triangulo1.mostrar_vertices())
print("Triángulo 2 vértices:", triangulo2.mostrar_vertices())