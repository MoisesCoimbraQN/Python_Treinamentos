# 🐍 Jornada de Estudos e Práticas em Python

Bem-vindo ao meu repositório de estudos em Python! Este espaço reúne exercícios, mini-projetos e treinamentos desenvolvidos para consolidar os fundamentos da linguagem, evoluindo do controle de fluxo básico até estruturas de dados avançadas, módulos nativos e conceitos de programação funcional.

---

## 🛠️ O que Aprendi e Pratiquei

Abaixo está um resumo dos tópicos e estruturas exploradas em cada arquivo deste repositório:

### 1. 🔤 Strings, Métodos de Tipo e Tratamento de Texto
* **`conta_vogais.py`**: Prática com manipulação de strings e métodos embutidos para iteração, filtragem e contagem de caracteres.
* **`identificando_palavras_longas.py`**: Utilização do método `.split()` para fatiamento, tokenização de texto e análise de comprimento de palavras.
* **`aula_61_cpf.py` & `validacao_cpf.py`**: Algoritmo de validação dos dígitos verificadores do CPF, envolvendo cálculo matemático sobre strings e tratamento de exceções.

### 2. 🧮 Operadores, Lógica e Controle de Fluxo
* **`contador_cedulas.py`**: Algoritmo de caixa eletrônico simulando a contagem de notas com operadores de divisão inteira (`//`) e resto/módulo (`%`).
* **`praticando_if_elif_else.py`**: Controle de decisão estruturado e encadeamento de condições.
* **`praticando_for_while.py` & `aula_76.py`**: Prática de laços de repetição (`for` e `while`), incluindo controle de fluxo e iterações contínuas.

### 3. 📦 Listas, Conjuntos (`set`) e Métodos Iteráveis
* **`gerenciador_tarefas.py`**: Gerenciamento de listas com os métodos `.append()` e `.pop()`, além do uso de `enumerate()` para manipular índices e elementos simultaneamente.
* **`aula_75_video_126.py` & `aula_80_video_132.py`**: Uso de conjuntos (`set`) para remoção e identificação de elementos duplicados em sequências e listas.

### 4. 🗂️ Dicionários, Funções Anônimas (`lambda`) e Ordenação
* **`aula_76_video_120.py` & `aula_78_video_119.py`**: Definição, estruturação e manipulação de métodos de dicionários (`dict`).
* **`aula_77_video_124.py`**: Criação de um questionário interativo utilizando dicionários para armazenar perguntas, opções e respostas certas.
* **`aula_81_video_133.py`**: Uso avançado da função `sorted()` combinada com expressões `lambda` como chave de ordenação (`key`) para organizar dicionários.

### 5. ⚙️ Funções, Empacotamento (`*args`) e Closures
* **`calculadora.py`, `valor_da_gorjeta.py` & `aula_70_video_110`**: Definição de funções simples, passagem de parâmetros e retornos.
* **`aula_71_video_111.py` & `aula_72_video_113.py`**: Empacotamento e desempacotamento de argumentos de tamanho dinâmico usando `*args`.
* **`praticando_funcoes.py`, `closures_arquivos.py` & `aula_74_video_116.py`**: Conceito de funções de alta ordem e *closures* (fechamentos), onde funções internas preservam o escopo de variáveis externas.

### 6. 🎲 Módulos Nativos e Jogos Interativos
* **`gerador_de_senha.py`**: Uso do módulo `random` e de métodos como `choice` e `shuffle` para geração aleatória e segura de senhas.
* **`jogo_adivinhar_numero.py` & `jogo_pedra.py`**: Jogos de terminal combinando sorteio aleatório, laços interativos e validação de regras.

---

## 📂 Estrutura do Repositório

```text
.
├── Curso_Udemy_2024/                 # Treinamento específico do curso Udemy
│   ├── aula_61_cpf.py                # Validação dos dígitos de CPF
│   ├── aula_70_video_110.py          # Definição e uso de funções simples
│   ├── aula_71_video_111.py          # Empacotamento e desempacotamento com *args
│   ├── aula_72_video_113.py          # Funções avançadas utilizando *args
│   ├── aula_74_video_116.py          # Closure de funções (fechamento)
│   ├── aula_75_video_126.py          # Verificação e eliminação de duplicados com set
│   ├── aula_76.py                    # Repetição contínua com laço while
│   ├── aula_76_video_120.py          # Métodos úteis de dicionários
│   ├── aula_77_video_124.py          # Sistema de questionário/quiz com dicionários
│   ├── aula_78_video_119.py          # Estruturação e definições de dicionários
│   ├── aula_80_video_132.py          # Algoritmo para encontrar primeiro elemento duplicado
│   └── aula_81_video_133.py          # Ordenação de dicionários com sorted() e lambda
├── .gitignore                         # Arquivos ignorados pelo controle de versão
├── calculadora.py                     # Funções para cálculos simples
├── closures_arquivos.py               # Exercícios de escopos e closures
├── conta_vogais.py                    # Contador de vogais e manipulação de strings
├── contador_cedulas.py                # Simulador de caixa eletrônico (operadores // e %)
├── gerador_de_senha.py                # Gerador de senhas (módulo random)
├── gerenciador_tarefas.py             # Gerenciador com append, pop e enumerate
├── identificando_palavras_longas.py   # Análise de textos e uso de .split()
├── jogo_adivinhar_numero.py          # Jogo de adivinhação
├── jogo_pedra.py                      # Jogo Pedra, Papel e Tesoura
├── praticando_for_while.py            # Laços for e while
├── praticando_funcoes.py              # Exercícios com definição de funções
├── praticando_if_elif_else.py         # Controle de fluxo estruturado
├── testeteste.py                      # Arquivo para rascunhos e testes rápidos
├── validacao_cpf.py                   # Função de validação de CPF com exceções
└── valor_da_gorjeta.py                # Calculadora de gorjetas
