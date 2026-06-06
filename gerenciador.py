from album import Album
from nodolista import NodoLista
from figuras import Figurinha
from historico import Historico

class Gerenciador:
    def __init__(self):
        """
        Inicializa o gerenciador da coleção do usuário.
        Ele controla o Álbum, a lista de repetidas e o histórico de trocas.
        """
        self.album = Album()
        self.historico = Historico()
        
        # Estrutura para as repetidas (Lista Encadeada)
        self.cabeca_repetidas = None
        self.quantidade_repetidas = 0

    def receber_figurinha(self, figurinha: Figurinha):
        """
        Tenta adicionar a figurinha no álbum. Se o álbum retornar False (já tem),
        ela vai automaticamente para a pilha de repetidas.
        """
        if not self.album.adicionar(figurinha):
            self._adicionar_repetida(figurinha)
            return f"Repetida! {figurinha.nome} foi para a pilha de trocas."
        return f"Nova! {figurinha.nome} colada no álbum."
