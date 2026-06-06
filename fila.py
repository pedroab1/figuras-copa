from nodofila import NodoFila
from figuras import Figurinha

class Fila:
    def __init__(self):
        """
        Inicializa uma fila vazia.
        """
        self._inicio = None
        self._fim = None

    def enqueue(self, figurinha: Figurinha):
        """
        Adiciona uma figurinha no final da fila.
        """
        novo_nodo = NodoFila(figurinha)
        
        # Se a fila está vazia, o novo nó é o início e o fim ao mesmo tempo
        if self._inicio is None:
            self._inicio = novo_nodo
            self._fim = novo_nodo
        else:
            # O último atual aponta para o novo nó, e o novo nó passa a ser o último
            self._fim.proximo = novo_nodo
            self._fim = novo_nodo

    def dequeue(self) -> Figurinha:
        """
        Remove e retorna a figurinha do início da fila.
        """
        if self._inicio is None:
            return None # A fila está vazia
        
        figurinha_removida = self._inicio.figurinha
        self._inicio = self._inicio.proximo
        
        # Se removemos o único elemento, o fim também precisa ser None
        if self._inicio is None:
            self._fim = None
            
        return figurinha_removida

    def peek(self) -> Figurinha:
        """
        Retorna a figurinha do início da fila sem removê-la.
        """
        if self._inicio is None:
            return None
        return self._inicio.figurinha

    def limpar(self):
        """
        Esvazia a fila completamente.
        """
        self._inicio = None
        self._fim = None