from figuras import Figurinha

class NodoFila:
    def __init__(self, figurinha: Figurinha):

        self.figurinha = figurinha
        self.proximo = None