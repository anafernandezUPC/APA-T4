"""
Ana Fernández Tejero
Este fichero contiene la implementación de un generador de números
pseudoaleatorios mediante el algoritmo de congruencia lineal (LGC).
"""


class Aleat:
    """
    Representa un generador de números pseudoaleatorios implementado
    como un objeto iterador.

    Atributos:
    modulo (int): El espacio de estados máximo del generador.
    multiplicador (int): Factor multiplicativo de la ecuación recursiva.
    incremento (int): Constante aditiva de la ecuación recursiva.
    estado (int): Valor actual del registro del generador.

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """
        Configura los parámetros iniciales del generador por medio de
        argumentos nombrados obligatorios.
        """
        self.modulo = m
        self.multiplicador = a
        self.incremento = c
        self.estado = x0

    def __next__(self):
        """
        Avanza el estado del algoritmo LGC y devuelve el siguiente entero.
        """
        self.estado = (
            self.multiplicador * self.estado + self.incremento
        ) % self.modulo
        return self.estado

    def __iter__(self):
        """
        Satisface el protocolo de iteración devolviendo la propia instancia.
        """
        return self

    def __call__(self, x0):
        """
        Permite el reinicio del estado interno utilizando una nueva semilla.
        """
        self.estado = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora basada en corrutinas para la obtención de aleatorios.

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
    """
    valor_actual = x0
    while True:
        valor_actual = (
            a * valor_actual + c
        ) % m
        entrada = yield valor_actual
        if entrada is not None:
            valor_actual = entrada


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)