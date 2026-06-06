from figuras import Figurinha

class NodoLista:
    def __init__(self, figurinha: Figurinha):
        """
        Nó para a lista encadeada (Álbum).
        Guarda a figurinha e o ponteiro para o próximo nó.
        """
        self.figurinha = figurinha
        self.proximo = None