# Definición de clases para las figuras geométricas

class Figura:
    def __init__(self, color):
        self.color = color

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

class Rectangulo(Figura):
    def __init__(self, color, ancho, alto):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto

class Cuadrado(Rectangulo):
    def __init__(self, color, lado):
        super().__init__(color, lado, lado)

class Ovalo(Figura):
    def __init__(self, color, eje_mayor, eje_menor):
        super().__init__(color)
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

# Instanciación de los objetos según el enunciado
circulo_negro = Circulo(color="negro", radio=5)
rectangulo_naranja = Rectangulo(color="naranja", ancho=8, alto=4)
cuadrado_azul = Cuadrado(color="azul", lado=6)
ovalo_amarillo = Ovalo(color="amarillo", eje_mayor=7, eje_menor=3)