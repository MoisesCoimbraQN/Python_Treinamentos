# 🐍 Jornada de Estudos e Práticas em Python

Bem-vindo ao meu repositório de estudos em Python! Este espaço reúne exercícios, mini-projetos e utilitários desenvolvidos durante meus treinamentos em 2024. O objetivo deste repositório é consolidar os fundamentos da linguagem, desde estruturas condicionais básicas até conceitos mais avançados de programação funcional e manipulação de dados.

---

## 🛠️ O que Aprendi e Pratiquei

Abaixo está um resumo dos conceitos fundamentais de Python explorados em cada arquivo/script deste repositório:

### 1. 🔤 Strings, Métodos de Tipo e Tratamento de Texto
* **`conta_vogais.py`**: Prática intensiva com manipulação de strings e métodos embutidos para iteração, filtragem e contagem de caracteres.
* **`identificando_palavras_longas.py`**: Utilização do método `.split()` para fatiamento, tokenização de texto e análise de comprimento de palavras em frases.

### 2. 🧮 Operadores Aritméticos, Lógica e Controle de Fluxo
* **`contador_cedulas.py`**: Algoritmo de caixa eletrônico simulando a contagem de notas utilizando operadores aritméticos de divisão inteira (`//`) e resto/módulo (`%`), aliados a estruturas condicionais.
* **`praticando_if_elif_else.py`**: Exercícios focados no domínio de tomada de decisões, validações e encadeamento de condições com `if`, `elif` e `else`.
* **`praticando_for_while.py`**: Prática de laços de repetição (`for` e `while`), controle de iterações e algoritmos repetitivos.

### 3. 📦 Estruturas de Dados (Listas, Dicionários, Tuplas e Iteradores)
* **`gerenciador_tarefas.py`**: Gerenciamento e manipulação de listas utilizando métodos de inserção e remoção (`append`, `pop`) e a função embutida `enumerate()` para acesso simultâneo a índices e elementos.
* **`Curso_Udemy_2024` / Ordenação de Dicionários**: Aplicação avançada da função `sorted()` para ordenar dicionários por chave ou valor, utilizando funções anônimas (`lambda`) como chave de ordenação (`key`).

### 4. ⚙️ Funções, Closures e Tratamento de Exceções
* **`calculadora.py` & `valor_da_gorjeta.py`**: Construção e modularização de código com funções simples, recebimento de parâmetros e retorno de valores.
* **`praticando_funcoes.py` & `closures_arquivos.py`**: Conceito de funções de alta ordem, escopo de variáveis e *closures* (funções internas que guardam o estado do escopo externo).
* **`validacao_cpf.py`**: Validação de dados de entrada, aplicação de regras de negócio e tratamento de exceções com blocos `try/except`.

### 5. 🎲 Módulos Nativos e Jogos Interativos
* **`gerador_de_senha.py`**: Utilização do módulo nativo `random` e métodos de amostragem/embaralhamento como `choice` e `shuffle` para geração segura de caracteres.
* **`jogo_adivinhar_numero.py` & `jogo_pedra.py`**: Jogos interativos de terminal unindo geração aleatória de números/opções, laços `while` e validações condicionais.

---

## 📂 Estrutura do Repositório

```text
.
├── Curso_Udemy_2024/                 # Scripts do curso Udemy (Ordenação de dicionários com lambda)
├── .gitignore                         # Arquivo de configuração de arquivos ignorados no Git
├── calculadora.py                     # Funções matemáticas simples
├── closures_arquivos.py               # Exercícios de closures e escopos
├── conta_vogais.py                    # Contador de vogais e manipulação de strings
├── contador_cedulas.py                # Simulador de caixa eletrônico (operadores // e %)
├── gerador_de_senha.py                # Gerador de senhas com módulo random (choice, shuffle)
├── gerenciador_tarefas.py             # Gerenciador de tarefas com listas, pop, append e enumerate
├── identificando_palavras_longas.py   # Análise de strings utilizando .split()
├── jogo_adivinhar_numero.py          # Jogo de adivinhação interativo
├── jogo_pedra.py                      # Jogo Pedra, Papel e Tesoura
├── praticando_for_while.py            # Exercícios com laços for e while
├── praticando_funcoes.py              # Exercícios com definição e retorno de funções
├── praticando_if_elif_else.py         # Exercícios com controle de fluxo estruturado
├── testeteste.py                      # Arquivo de testes rápidos de código
├── validacao_cpf.py                   # Algoritmo e validação de CPF com tratamento de exceções
└── valor_da_gorjeta.py                # Calculadora de gorjeta com funções
