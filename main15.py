class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self._poligonos = []  # lista de referencias a los polígonos a los que pertenece

    @property
    def poligonos(self):
        return self._poligonos

    def add_poligono(self, poligono):
        if poligono not in self._poligonos:
            self._poligonos.append(poligono)


class Poligono:
    def __init__(self):
        self._puntos = []

    def add_punto(self, punto: Punto):
        if punto not in self._puntos:
            self._puntos.append(punto)
            punto.add_poligono(self)

    def num_vertices(self):
        return len(self._puntos)

    def validar(self):
        if self.num_vertices() < 3:
            raise ValueError("Un polígono debe tener al menos 3 puntos.")

    def mostrar_vertices(self):
        return [(p.x, p.y) for p in self._puntos]

    def perimetro(self):
        if self.num_vertices() < 3:
            raise ValueError("No es un polígono válido.")
        per = 0
        for i in range(len(self._puntos)):
            p1 = self._puntos[i]
            p2 = self._puntos[(i+1) % len(self._puntos)]
            per += ((p2.x - p1.x)**2 + (p2.y - p1.y)**2) ** 0.5
        return per


# Ejemplo de diagrama de objetos:
# p1 pertenece a poligono1 y poligono2
p1 = Punto(0, 0)
p2 = Punto(1, 0)
p3 = Punto(1, 1)
p4 = Punto(0, 1)

poligono1 = Poligono()
poligono1.add_punto(p1)
poligono1.add_punto(p2)
poligono1.add_punto(p3)

poligono2 = Poligono()
poligono2.add_punto(p1)
poligono2.add_punto(p3)
poligono2.add_punto(p4)