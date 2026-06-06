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
        