from fila import Fila
from figuras import Figurinha

class Historico:
    def __init__(self):
        """
        Inicializa o histórico de trocas usando a implementação própria de Fila.
        """
        self.registro = Fila()

    def registrar_troca(self, figurinha_adquirida: Figurinha):
        """
        Adiciona a figurinha resultante da troca ao histórico (enfileira).
        """
        self.registro.enqueue(figurinha_adquirida)

    def ver_ultima_troca(self) -> Figurinha:
        """
        Apenas espia qual foi a última figurinha que entrou na fila para ser processada (peek).
        """
        return self.registro.peek()
        
    def limpar_historico(self):
        """
        Limpa todos os registros de trocas.
        """
        self.registro.limpar()