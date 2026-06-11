import json
import os
from figuras import Figurinha
from gerenciador import Gerenciador

class GerenciadorDados:
    def __init__(self, nome_arquivo="meu_album.json"):
        """
        Inicializa a classe responsável por ler e escrever no disco.
        Garante que o caminho seja absoluto com base na pasta onde os scripts estão salvos.
        """
        # Descobre a pasta absoluta onde este script (gerenciador_dados.py) está localizado
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        # Une o caminho da pasta com o nome do arquivo JSON solicitado
        self.arquivo = os.path.join(diretorio_atual, nome_arquivo)

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

        # Linha de diagnóstico para ajudar a identificar problemas de caminho de arquivo
        print(f"\n[SISTEMA] Tentando ler o arquivo em: {self.arquivo}")

        if not os.path.exists(self.arquivo):
            print("[SISTEMA] Aviso: Arquivo de origem não encontrado. Iniciando coleção zerada.")
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

        print(f"[SISTEMA] Sucesso! Foram carregadas {novo_gerenciador.quantidade_repetidas} figurinhas repetidas.")
        return novo_gerenciador