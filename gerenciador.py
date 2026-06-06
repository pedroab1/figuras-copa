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

    def _adicionar_repetida(self, figurinha: Figurinha):
        """
        Método interno para adicionar um nó na lista de repetidas.
        """
        novo_nodo = NodoLista(figurinha)
        if self.cabeca_repetidas is None:
            self.cabeca_repetidas = novo_nodo
        else:
            atual = self.cabeca_repetidas
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo
            
        self.quantidade_repetidas += 1

    def listar_repetidas(self) -> str:
        """
        Mostra a lista de figurinhas repetidas.
        """
        if self.cabeca_repetidas is None:
            return "Você não tem figurinhas repetidas."
        
        resultado = "--- FIGURINHAS REPETIDAS ---\n"
        atual = self.cabeca_repetidas
        while atual is not None:
            resultado += f"{atual.figurinha}\n"
            atual = atual.proximo
        return resultado

    def buscar_repetida(self, id_figurinha: int) -> Figurinha:
        """
        Busca uma figurinha específica na pilha de repetidas.
        """
        atual = self.cabeca_repetidas
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                return atual.figurinha
            atual = atual.proximo
        return None
