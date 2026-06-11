from nodolista import NodoLista
from figuras import Figurinha

class Album:
    def __init__(self, total_figurinhas_album: int = 670):
        self.cabeca = None
        self.tamanho = 0
        self.total_figurinhas = total_figurinhas_album

    def adicionar(self, figurinha: Figurinha) -> bool:
        if self.buscar(figurinha.id) is not None:
            return False 
        
        novo_nodo = NodoLista(figurinha)
        
        if self.cabeca is None:
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo
            
        self.tamanho += 1
        return True

    def remover(self, id_figurinha: int) -> bool:
        atual = self.cabeca
        anterior = None
        
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                
                self.tamanho -= 1
                return True 
            
            anterior = atual
            atual = atual.proximo
            
        return False 

    def buscar(self, id_figurinha: int) -> Figurinha:
        atual = self.cabeca
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                return atual.figurinha
            atual = atual.proximo
        return None

    def buscar_por_jogador(self, nome: str) -> str:
        atual = self.cabeca
        resultado = ""
        while atual is not None:
            if nome.lower() in atual.figurinha.nome.lower():
                resultado += f"{atual.figurinha}\n"
            atual = atual.proximo
            
        return resultado if resultado else "Nenhum jogador encontrado com este nome."

    def buscar_por_selecao(self, pais: str) -> str:
        atual = self.cabeca
        resultado = ""
        while atual is not None:
            if pais.lower() == atual.figurinha.pais.lower():
                resultado += f"{atual.figurinha}\n"
            atual = atual.proximo
            
        return resultado if resultado else "Nenhuma figurinha desta seleção encontrada."

    def ver_album_completo(self) -> str:
        if self.cabeca is None:
            return "Seu álbum está vazio."
        
        atual = self.cabeca
        resultado = "--- SEU ÁLBUM ---\n"
        while atual is not None:
            resultado += f"{atual.figurinha}\n"
            atual = atual.proximo
        return resultado

    def ver_porcentagem_concluida(self) -> str:
        porcentagem = (self.tamanho / self.total_figurinhas) * 100
        return f"Progresso do Álbum: {self.tamanho}/{self.total_figurinhas} figurinhas ({porcentagem:.2f}% concluído)"