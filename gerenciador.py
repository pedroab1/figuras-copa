from album import Album
from nodolista import NodoLista
from figuras import Figurinha
from historico import Historico

class Gerenciador:
    def __init__(self):

        self.album = Album()
        self.historico = Historico()
        
        self.cabeca_repetidas = None
        self.quantidade_repetidas = 0

    def receber_figurinha(self, figurinha: Figurinha):

        if not self.album.adicionar(figurinha):
            self._adicionar_repetida(figurinha)
            return f"Repetida! {figurinha.nome} foi para a pilha de trocas."
        return f"Nova! {figurinha.nome} colada no álbum."

    def _adicionar_repetida(self, figurinha: Figurinha):

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

        if self.cabeca_repetidas is None:
            return "Você não tem figurinhas repetidas."
        
        resultado = "--- FIGURINHAS REPETIDAS ---\n"
        atual = self.cabeca_repetidas
        while atual is not None:
            resultado += f"{atual.figurinha}\n"
            atual = atual.proximo
        return resultado

    def buscar_repetida(self, id_figurinha: int) -> Figurinha:

        atual = self.cabeca_repetidas
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                return atual.figurinha
            atual = atual.proximo
        return None

    def _remover_repetida(self, id_figurinha: int) -> bool:

        atual = self.cabeca_repetidas
        anterior = None
        
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                if anterior is None:
                    self.cabeca_repetidas = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.quantidade_repetidas -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def propor_troca(self, minha_repetida_id: int, amigo_repetida_id: int, gerenciador_amigo: 'Gerenciador') -> str:
        minha_fig = self.buscar_repetida(minha_repetida_id)
        amigo_fig = gerenciador_amigo.buscar_repetida(amigo_repetida_id)
        
        if not minha_fig:
            return "Erro: Você não possui a figurinha oferecida nas suas repetidas."
        if not amigo_fig:
            return "Erro: O usuário alvo não possui a figurinha solicitada nas repetidas."
            
        if self.album.buscar(amigo_repetida_id) is not None:
            return "Troca cancelada: Você já tem essa figurinha no seu álbum."
        if gerenciador_amigo.album.buscar(minha_repetida_id) is not None:
            return "Troca cancelada: O outro usuário já tem a sua figurinha no álbum dele."
            
        self._remover_repetida(minha_repetida_id)
        gerenciador_amigo._remover_repetida(amigo_repetida_id)
        
        self.album.adicionar(amigo_fig)
        gerenciador_amigo.album.adicionar(minha_fig)
        
        self.historico.registrar_troca(amigo_fig)
        gerenciador_amigo.historico.registrar_troca(minha_fig)
        
        return f"Sucesso! Troca efetuada. Você enviou {minha_fig.nome} e recebeu {amigo_fig.nome}."