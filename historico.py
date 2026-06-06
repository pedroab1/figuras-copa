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