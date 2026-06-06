class Figurinha:
    def __init__(self, id_figurinha: int, nome: str, pais: str, posicao: str, raridade: str):
        """
        Inicializa uma nova figurinha com os atributos exigidos pelo projeto.
        """
        self.id = id_figurinha
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade

    def __str__(self):
        """
        Define como a figurinha será exibida ao usarmos a função print().
        Isso facilitará muito a visualização no terminal depois.
        """
        return f"[{self.id}] {self.nome} ({self.pais}) - {self.posicao} | {self.raridade}"