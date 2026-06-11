import json
import os
from figuras import Figurinha
from gerenciador import Gerenciador

class GerenciadorDados:
    def __init__(self, nome_arquivo="meu_album.json"):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        self.arquivo = os.path.join(diretorio_atual, nome_arquivo)

    def salvar(self, gerenciador: Gerenciador):

        dados = {
            "album": [],
            "repetidas": []
        }

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

        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    def carregar(self) -> Gerenciador:
       
        novo_gerenciador = Gerenciador()

        print(f"\n[SISTEMA] Tentando ler o arquivo em: {self.arquivo}")

        if not os.path.exists(self.arquivo):
            print("[SISTEMA] Aviso: Arquivo de origem não encontrado. Iniciando coleção zerada.")
            return novo_gerenciador

        with open(self.arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)

        for item in dados.get("album", []):
            fig = Figurinha(item["id"], item["nome"], item["pais"], item["posicao"], item["raridade"])
            novo_gerenciador.album.adicionar(fig)

        for item in dados.get("repetidas", []):
            fig = Figurinha(item["id"], item["nome"], item["pais"], item["posicao"], item["raridade"])
            novo_gerenciador._adicionar_repetida(fig)

        print(f"[SISTEMA] Sucesso! Foram carregadas {novo_gerenciador.quantidade_repetidas} figurinhas repetidas.")
        return novo_gerenciador