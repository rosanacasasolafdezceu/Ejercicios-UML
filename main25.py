class Libro:
    """
    Representa un conjunto de hojas de papel manuscritas o impresas que, cosidas o encuadernadas, forman un volumen.
    Invariantes:
        - Las hojas deben ser de papel.
        - Las hojas deben estar manuscritas o impresas.
        - Las hojas deben estar cosidas o encuadernadas.
        - El conjunto de hojas forma un volumen.
    """
    def __init__(self, hojas, tipo_texto, encuadernado):
        """
        hojas: lista de hojas de papel
        tipo_texto: 'manuscrito' o 'impreso'
        encuadernado: True si las hojas están cosidas o encuadernadas
        """
        self.hojas = hojas
        self.tipo_texto = tipo_texto
        self.encuadernado = encuadernado

class Muestra:
    """
    Representa una parte o porción extraída de un conjunto, por métodos que permiten considerarla representativa del mismo.
    Invariantes:
        - La muestra es parte de un conjunto.
        - La muestra se extrae por métodos que la hacen representativa.
    """
    def __init__(self, conjunto, parte, metodo_representativo):
        """
        conjunto: el conjunto del que se extrae la muestra
        parte: la porción extraída
        metodo_representativo: método usado para extraer la muestra y considerarla representativa
        """
        self.conjunto = conjunto
        self.parte = parte
        self.metodo_representativo = metodo_representativo