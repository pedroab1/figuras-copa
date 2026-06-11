from nodofila import NodoFila
from figuras import Figurinha

class Fila:
    def __init__(self):

        self._inicio = None
        self._fim = None

    def enqueue(self, figurinha: Figurinha):

        novo_nodo = NodoFila(figurinha)
        
        if self._inicio is None:
            self._inicio = novo_nodo
            self._fim = novo_nodo
        else:
            self._fim.proximo = novo_nodo
            self._fim = novo_nodo

    def dequeue(self) -> Figurinha:

        if self._inicio is None:
            return None
        
        figurinha_removida = self._inicio.figurinha
        self._inicio = self._inicio.proximo
        
        if self._inicio is None:
            self._fim = None
            
        return figurinha_removida

    def peek(self) -> Figurinha:

        if self._inicio is None:
            return None
        return self._inicio.figurinha

    def limpar(self):

        self._inicio = None
        self._fim = None