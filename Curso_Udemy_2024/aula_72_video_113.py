# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


numeros = list(input('Digite os números para multiplicar, separados por vírgula: ').split(','))
numeros = [int(n) for n in numeros]  # Convertendo os elementos da lista para inteiros

def multiplica (*args):
    total = 1
    for n in args:
        total = total * n
    return total 

valor_resultante = multiplica(*numeros)
print(valor_resultante)


# Crie uma função que recebe um número e retorna se ele é par ou ímpar. CLASSICO 
x = input('Digite um número: ')
x =  int(x)
def par_impar (x):

    if isinstance( x, int):
        if x % 2 == 0:
            return print(f'O número {x} é par!')
        else:
            print(f'O número {x} não é par!')
    else:
        'O número digitado não é válido'
    return par_impar

par_impar(x)




# def multiplicar(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total


# multiplicação = multiplicar(10, 2, 3, 4, 5)
# print(multiplicação)


# # Crie uma função fala se um número é par ou ímpar.
# # Retorne se o número é par ou ímpar.
# def par_impar(numero):
#     multiplo_de_dois = numero % 2 == 0

#     if multiplo_de_dois:
#         return f'{numero} é par'
#     return f'{numero} é ímpar'


# outro_par_impar = par_impar
# dois_e_par = outro_par_impar(2)
# print(dois_e_par)
# print(par_impar(3))
# print(par_impar(15))
# print(par_impar(16))

# print(par_impar is outro_par_impar)