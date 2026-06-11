# Sistema de Álbum de Figurinhas — Copa 2026

Projeto desenvolvido para a disciplina de **Estrutura de Dados**, com o objetivo de simular um sistema de gerenciamento de figurinhas da Copa do Mundo.

O sistema permite cadastrar figurinhas, organizar o álbum, controlar repetidas, realizar buscas, propor trocas com outro colecionador e salvar os dados em arquivo JSON.

## Funcionalidades

* Adicionar figurinhas ao álbum;
* Identificar figurinhas repetidas;
* Ver álbum completo;
* Consultar progresso do álbum;
* Buscar figurinhas por número, jogador ou seleção;
* Listar figurinhas repetidas;
* Propor troca com outro colecionador;
* Registrar histórico de trocas;
* Salvar e carregar dados em JSON.

## Estruturas Utilizadas

O projeto utiliza estruturas de dados implementadas manualmente, sem uso de `list` ou `deque` para representar a lista encadeada e a fila.

As principais estruturas são:

* **Lista encadeada:** usada para armazenar o álbum e as figurinhas repetidas;
* **Fila FIFO:** usada para registrar o histórico de trocas;
* **Nós encadeados:** usados nas classes `NodoLista` e `NodoFila`.

## Classes Principais

* `Figurinha`: representa uma figurinha do álbum;
* `Album`: gerencia as figurinhas coladas;
* `Gerenciador`: controla álbum, repetidas e trocas;
* `Fila`: implementação própria de fila FIFO;
* `Historico`: registra trocas realizadas;
* `GerenciadorDados`: salva e carrega dados em JSON;
* `NodoLista` e `NodoFila`: nós usados nas estruturas encadeadas.

## Arquivos do Projeto

```text
.
├── album.py
├── amigo_colecionador.json
├── figuras.py
├── fila.py
├── gerenciador.py
├── gerenciador_dados.py
├── historico.py
├── main.py
├── nodofila.py
├── nodolista.py
└── README.md
```

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
```

Acesse a pasta do projeto:

```bash
cd NOME-DO-REPOSITORIO
```

Execute o programa:

```bash
python main.py
```

Ou, dependendo do sistema:

```bash
python3 main.py
```

## Requisitos

* Python 3 instalado;
* Nenhuma biblioteca externa é necessária.

O projeto utiliza apenas recursos nativos do Python.

## Menu do Sistema

Ao executar o programa, o usuário verá o seguinte menu:

```text
1. Abrir pacotinho (Adicionar Figurinha)
2. Ver Álbum Completo
3. Ver Progresso do Álbum
4. Buscar Figurinha por Número
5. Buscar Figurinha por Jogador
6. Buscar Figurinha por Seleção
7. Ver Figurinhas Repetidas
8. Propor Troca com Amigo
9. Ver Última Troca (Histórico FIFO)
0. Salvar e Sair
```

## Persistência de Dados

Os dados são salvos em arquivos JSON.

* `meu_album.json`: armazena o álbum do usuário;
* `amigo_colecionador.json`: simula as figurinhas de outro colecionador.

Ao escolher a opção `0`, o sistema salva os dados antes de encerrar.

## Objetivo Acadêmico

O projeto demonstra o uso prático de:

* Lista encadeada;
* Fila FIFO;
* Programação orientada a objetos;
* Separação de responsabilidades em classes;
* Validação de entradas;
* Persistência em arquivos.

## Autor

Pedro Azevedo Batista

Projeto desenvolvido para a disciplina de **Estrutura de Dados** — Fatec Rio Claro.
