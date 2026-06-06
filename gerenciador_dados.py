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

        # 2. Percorrer a lista encadeada de repetidas
        atual = gerenciador.cabeca_repetidas
        while atual is not None:
            fig = atual.figurinha
            dados["repetidas"].append({
                "id": fig.id,
                "nome": fig.nome,
                "pais": fig.pais,
                "posicao": fig.posicao,
                "raridade": fig.raridade
            })
            atual = atual.proximo

        # Gravar no arquivo (ensure_ascii=False mantém os acentos corretos)
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    def carregar(self) -> Gerenciador:
        """
        Lê o arquivo JSON e remonta as listas encadeadas originais.
        """
        novo_gerenciador = Gerenciador()

        # Se o arquivo não existir (primeira vez rodando), retorna um gerenciador vazio
        if not os.path.exists(self.arquivo):
            return novo_gerenciador

        with open(self.arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)

        # Reconstruir o álbum (Lendo os dados e gerando novos nós encadeados)
        for item in dados.get("album", []):
            fig = Figurinha(item["id"], item["nome"], item["pais"], item["posicao"], item["raridade"])
            novo_gerenciador.album.adicionar(fig)

        # Reconstruir a pilha de repetidas
        for item in dados.get("repetidas", []):
            fig = Figurinha(item["id"], item["nome"], item["pais"], item["posicao"], item["raridade"])
            novo_gerenciador._adicionar_repetida(fig)

        return novo_gerenciador