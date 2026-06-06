import os
from figuras import Figurinha
from gerenciador import Gerenciador
from gerenciador_dados import GerenciadorDados

# Lista de seleções válidas para tratamento de erro de entrada
SELECOES_VALIDAS = [
    "brasil", "argentina", "franca", "alemanha", "espanha", 
    "inglaterra", "portugal", "holanda", "italia", "uruguai"
]

def exibir_menu():
    """Imprime o menu iterativo no terminal."""
    print("\n" + "="*45)
    print(" 🏆 SISTEMA DE ÁLBUM DA COPA 2026 🏆 ")
    print("="*45)
    print("1. Abrir pacotinho (Adicionar Figuri8" \
    "nha)")
    print("2. Ver Álbum Completo")
    print("3. Ver Progresso do Álbum")
    print("4. Buscar Figurinha por Número")
    print("5. Buscar Figurinha por Jogador")
    print("6. Buscar Figurinha por Seleção")
    print("7. Ver Figurinhas Repetidas")
    print("8. Propor Troca com Amigo")
    print("9. Ver Última Troca (Histórico FIFO)")
    print("0. Salvar e Sair")
    print("="*45)
