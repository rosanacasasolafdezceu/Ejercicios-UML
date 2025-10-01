class Punto:
    def __init__(self, x: float, y: float, poligono=None):
        self.x = x
        self.y = y
        self._poligono = poligono

    @property
    def poligono(self):
        return self._poligono


class Poligono:
    def __init__(self):
        self._puntos = []

    def agregar_punto(self, punto: Punto):
        if punto.poligono is not None and punto.poligono is not self:
            raise ValueError("El punto ya está asignado a otro polígono.")
        self._puntos.append(punto)
        punto._poligono = self

    def cantidad_vertices(self):
        return len(self._puntos)

    def validar(self):
        if self.cantidad_vertices() < 3:
            raise ValueError("Un polígono requiere al menos 3 puntos.")

    def obtener_vertices(self):
        return [(p.x, p.y) for p in self._puntos]

    def calcular_perimetro(self):
        if self.cantidad_vertices() < 3:
            raise ValueError("No es un polígono válido.")
        perimetro = 0
        n = len(self._puntos)
        for i in range(n):
            p1 = self._puntos[i]
            p2 = self._puntos[(i + 1) % n]
            distancia = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
            perimetro += distancia
        return perimetro