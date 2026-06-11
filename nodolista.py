from figuras import Figurinha

class NodoLista:
    def __init__(self, figurinha: Figurinha):

        self.figurinha = figurinha
        self.proximo = None