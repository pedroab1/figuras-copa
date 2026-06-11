class Figurinha:
    def __init__(self, id_figurinha: int, nome: str, pais: str, posicao: str, raridade: str):
        self.id = id_figurinha
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade

    def __str__(self):
        return f"[{self.id}] {self.nome} ({self.pais}) - {self.posicao} | {self.raridade}"