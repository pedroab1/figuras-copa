from figuras import Figurinha

class NodoLista:
    def __init__(self, figurinha: Figurinha):
        """
        Nó para a Fila FIFO (Trocas e Histórico).
        Guarda a figurinha e o ponteiro para o próximo nó na fila.
        """
        self.figurinha = figurinha
        self.proximo = None