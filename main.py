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

def main():
    # 1. Inicializa o persistidor e tenta carregar dados existentes do JSON
    persistencia = GerenciadorDados("meu_album.json")
    meu_gerenciador = persistencia.carregar()

   # 2. Carrega o gerenciador do "Amigo" a partir de um arquivo JSON separado
    persistencia_amigo = GerenciadorDados("amigo_album.json")
    amigo_gerenciador = persistencia_amigo.carregar()
    print("Bem-vindo ao seu Álbum de Figurinhas!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            print("\n--- ADICIONAR FIGURINHA ---")
            try:
                # Tratamento de Erro: O ID precisa ser um número
                id_fig = int(input("Número (ID) da Figurinha: "))
                if id_fig <= 0:
                    print("Erro: O número da figurinha deve ser maior que zero.")
                    continue
                    
                nome = input("Nome do Jogador/Estádio: ").strip()
                if not nome:
                    print("Erro: O nome não pode ficar em branco.")
                    continue
                    
                # Tratamento de Erro: Validação de código de seleção
                pais = input("Seleção (País): ").strip()
                if pais.lower() not in SELECOES_VALIDAS:
                    print(f"Erro: Seleção '{pais}' inválida.")
                    print(f"Seleções aceitas: {', '.join(SELECOES_VALIDAS).title()}")
                    continue
                    
                posicao = input("Posição: ").strip()
                raridade = input("Raridade (Comum, Prata, Ouro, Lenda): ").strip()

                # Instancia a figurinha e manda para o gerenciador processar
                nova_fig = Figurinha(id_fig, nome, pais, posicao, raridade)
                resultado = meu_gerenciador.receber_figurinha(nova_fig)
                print(f"\nResultado: {resultado}")
                
            except ValueError:
                print("Erro de Digitação: O Número (ID) deve ser um valor numérico inteiro. Letras não são aceitas.")

        elif opcao == '2':
            print("\n" + meu_gerenciador.album.ver_album_completo())

        elif opcao == '3':
            print("\n" + meu_gerenciador.album.ver_porcentagem_concluida())

        elif opcao == '4':
            try:
                id_busca = int(input("\nDigite o número da figurinha que deseja buscar: "))
                fig = meu_gerenciador.album.buscar(id_busca)
                if fig:
                    print(f"\nFigurinha Encontrada no Álbum: {fig}")
                else:
                    print("\nVocê ainda não tem essa figurinha colada no álbum.")
            except ValueError:
                print("Erro: Digite apenas números.")

        elif opcao == '5':
            nome_busca = input("\nDigite o nome do jogador: ").strip()
            print("\nResultados da Busca:")
            print(meu_gerenciador.album.buscar_por_jogador(nome_busca))

        elif opcao == '6':
            pais_busca = input("\nDigite a seleção: ").strip()
            print("\nResultados da Busca:")
            print(meu_gerenciador.album.buscar_por_selecao(pais_busca))

        elif opcao == '7':
            print("\n" + meu_gerenciador.listar_repetidas())
            print(f"Total na pilha de repetidas: {meu_gerenciador.quantidade_repetidas}")

        elif opcao == '8':
            print("\n--- ÁREA DE TROCAS ---")
            print(f"DICA: O amigo possui {amigo_gerenciador.quantidade_repetidas} figurinhas repetidas no arquivo dele.")
            try:
                minha_id = int(input("\nQual figurinha SUA você quer oferecer? "))
                amigo_id = int(input("Qual figurinha do AMIGO você quer receber? "))
                
                # Executa a lógica complexa de troca passando o gerenciador do amigo
                resultado_troca = meu_gerenciador.propor_troca(minha_id, amigo_id, amigo_gerenciador)
                print(f"\n{resultado_troca}")
            except ValueError:
                print("Erro: Os IDs das figurinhas devem ser números inteiros.")

        elif opcao == '9':
            print("\n--- HISTÓRICO DE TROCAS (FIFO) ---")
            ultima = meu_gerenciador.historico.ver_ultima_troca()
            if ultima:
                print(f"Última figurinha adquirida via troca (Topo da Fila): {ultima}")
            else:
                print("Nenhuma troca foi registrada no histórico ainda.")

        elif opcao == '0':
            print("\nSalvando seus dados no disco...")
            persistencia.salvar(meu_gerenciador)
            print("Dados salvos com sucesso! Encerrando o sistema. Boa sorte na apresentação!")
            break

        else:
            print("\nOpção inválida. Digite um número de 0 a 9.")

if __name__ == "__main__":
    main()