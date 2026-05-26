import random


lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

#Como a lista de lista é considerada uma matriz, podemos usar um loop for para iterar sobre cada sublista e imprimir seus elementos. O código abaixo faz isso:
lista_de_lista_aleatoria = [[random.randint(1, 10) for _ in range(10)] for _ in range(12)]
for lista in lista_de_lista_aleatoria:
    print(lista)

def encontra_numero (lista_de_inteiros):
    numero_checado = set()                  #set é mais rápido para verificar se um elemento existe, pois é implementado como uma tabela hash
    primeiro_duplicado= -1                  #padrão (não esta na lista)

    for numero in lista_de_inteiros:
        if numero in numero_checado:
            primeiro_duplicado = numero 
            break

        numero_checado.add(numero)          # a cada laço for, o numero é adicionado ao set numero_checado
    
    return primeiro_duplicado

# Executando a função para cada sublista da sua matriz:
for sublista in lista_de_listas_de_inteiros:
    resultado = encontra_numero(sublista)
    print(f"Lista: {sublista} -> Primeiro duplicado: {resultado}")

#Da lista aleatoria    
for sublista in lista_de_listas_de_inteiros:
    resultado = encontra_numero(sublista)
    print(f"Lista_aleatoria: {sublista} -> Primeiro duplicado: {resultado}")    