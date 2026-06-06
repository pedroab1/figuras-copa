import json
import os
from figuras import Figurinha
from gerenciador import Gerenciador

class GerenciadorDados:
    def __init__(self, nome_arquivo="meu_album.json"):
        """
        Inicializa a classe responsável por ler e escrever no disco.
        """
        self.arquivo = nome_arquivo

    def salvar(self, gerenciador: Gerenciador):
        """
        Converte as listas encadeadas em um formato de dicionário que o módulo 
        JSON do Python consegue gravar em um arquivo de texto.
        """
        dados = {
            "album": [],
            "repetidas": []
        }

        # 1. Percorrer a lista encadeada do álbum e extrair os dados
        atual = gerenciador.album.cabeca
        while atual is not None:
            fig = atual.figurinha
            dados["album"].append({
                "id": fig.id,
                "nome": fig.nome,
                "pais": fig.pais,
                "posicao": fig.posicao,
                "raridade": fig.raridade
            })
            atual = atual.proximo