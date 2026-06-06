from nodolista import NodoLista
from figuras import Figurinha

class Album:
    def __init__(self, total_figurinhas_album: int = 670):
        """
        Inicializa o álbum vazio. 
        O total de figurinhas padrão (670) é usado para calcular a porcentagem.
        """
        self.cabeca = None
        self.tamanho = 0
        self.total_figurinhas = total_figurinhas_album

    def adicionar(self, figurinha: Figurinha) -> bool:
        """
        Adiciona uma figurinha ao álbum.
        Retorna True se foi adicionada com sucesso, ou False se for repetida.
        """
        # Regra de negócio: Se a figurinha já está no álbum, é repetida.
        if self.buscar(figurinha.id) is not None:
            return False 
        
        novo_nodo = NodoLista(figurinha)
        
         # Se o álbum está vazio, o novo nó se torna a cabeça
        if self.cabeca is None:
            self.cabeca = novo_nodo
        else:
            # Percorre a lista até achar o último nó (onde 'proximo' é None)
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            # Faz o último nó apontar para o novo
            atual.proximo = novo_nodo
            
        self.tamanho += 1
        return True

    def remover(self, id_figurinha: int) -> bool:
        """
        Busca e remove uma figurinha pelo ID.
        Retorna True se removeu, ou False se não encontrou.
        """
        atual = self.cabeca
        anterior = None
        
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                # Se a figurinha a ser removida for a primeira (cabeça)
                if anterior is None:
                    self.cabeca = atual.proximo
                # Se estiver no meio ou no final
                else:
                    anterior.proximo = atual.proximo
                
                self.tamanho -= 1
                return True # Removida com sucesso
            
            # Avança os ponteiros
            anterior = atual
            atual = atual.proximo
            
        return False # Figurinha não encontrada

    def buscar(self, id_figurinha: int) -> Figurinha:
        """
        Busca específica pelo número (ID) da figurinha.
        """
        atual = self.cabeca
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                return atual.figurinha
            atual = atual.proximo
        return None
    def buscar_por_jogador(self, nome: str) -> str:
        """
        Busca todas as figurinhas que correspondam ao nome do jogador.
        Como não podemos usar listas (list) nativas, retornamos uma string formatada.
        """
        atual = self.cabeca
        resultado = ""
        while atual is not None:
            # O .lower() ignora se o usuário digitou maiúsculo ou minúsculo
            if nome.lower() in atual.figurinha.nome.lower():
                resultado += f"{atual.figurinha}\n"
            atual = atual.proximo
            
        return resultado if resultado else "Nenhum jogador encontrado com este nome."

    def buscar_por_selecao(self, pais: str) -> str:
        """
        Busca todas as figurinhas que correspondam ao nome da seleção (país).
        """
        atual = self.cabeca
        resultado = ""
        while atual is not None:
            if pais.lower() == atual.figurinha.pais.lower():
                resultado += f"{atual.figurinha}\n"
            atual = atual.proximo
            
        return resultado if resultado else "Nenhuma figurinha desta seleção encontrada."

    def ver_album_completo(self) -> str:
        """
        Retorna uma string com todas as figurinhas coladas no álbum.
        """
        if self.cabeca is None:
            return "Seu álbum está vazio."
        
        atual = self.cabeca
        resultado = "--- SEU ÁLBUM ---\n"
        while atual is not None:
            resultado += f"{atual.figurinha}\n"
            atual = atual.proximo
        return resultado

    def ver_porcentagem_concluida(self) -> str:
        """
        Calcula e retorna a porcentagem baseada no tamanho atual da lista.
        """
        porcentagem = (self.tamanho / self.total_figurinhas) * 100
        return f"Progresso do Álbum: {self.tamanho}/{self.total_figurinhas} figurinhas ({porcentagem:.2f}% concluído)"