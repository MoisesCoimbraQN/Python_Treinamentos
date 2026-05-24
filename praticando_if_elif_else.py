# print('Quantidade de produtos vendidos')

# macas = int(input('Digite a quantidade de maças vendidas: '))
# bananas = int(input('Digite a quantidade de bananas vendidas: '))

# if macas > bananas:
#     print(f'As maças tiveram mais vendas. Foram vendidas {macas}')
# elif bananas == macas:
#     print(f'Bananas e maças foram vendidas na mesma quantidade: {bananas}')
# else:
#     print(f'As bananas tiveram mais vendas. Foram vendidas {bananas}')


# print('Cálculo do total de dias das atividades.\n')

# atividade_a = int(input('Informe os dias das atividades A: '))
# atividade_b = int(input('Informe os dias das atividades B: '))
# atividade_c = int(input('Informe os dias das atividades C: '))

# if (atividade_a >= 0 and atividade_b >= 0 and atividade_c>= 0):
#     tempo_total = atividade_a    + atividade_b + atividade_c
#     print(f'Tempo total das atividades foram {tempo_total}')
# else:
#     print('Os dias não podem ser negativos')

# print('Verificando a temperatura\n')

# temperatura = int(input('Digite aa temperatura atual: '))
# temp_max = 25

# if temperatura > temp_max:
#     print('Alerta! Temperatura acima do permitido!!!')
# else:
#     print('Temperatura dentro do permitido.')

# print('Cálculo do IMC\n')

# peso= float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))

# imc = peso/altura**2

# print(f'Seu IMC é {imc}')

# if imc < 18.5:
#     print('Você esta abaixo do peso!')
# elif imc < 25:
#     print('Você com peso ideal !')
# else:
#     print('Você está acima do peso!')


# limite = 3000.0
# despesas = float(input("Digite o total de despesas do mês (R$): "))

# if despesas > limite:
#     print("Atenção! Você ultrapassou o limite do orçamento.")
# else:
#     print("Você está dentro do orçamento.")


# hora_atual = int(input("Digite a hora atual (formato 24 horas): "))

# if 8 <= hora_atual < 18:
#     print("Acesso permitido.")
# else:
#     print("Acesso negado.")


# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))

# media = (nota1 + nota2 + nota3) / 3

# if media >= 7:
#     print("Aprovado")
# elif 5 <= media < 7:
#     print("Recuperação")
# else:
#     print("Reprovado")

#     distancia = float(input("Digite a distância percorrida (em km): "))

# if distancia <= 100:
#     print("Valor do pedágio: R$ 10,00")
# elif 100 < distancia <= 200:
#     print("Valor do pedágio: R$ 20,00")
# else:
#     print("Valor do pedágio: R$ 30,00")

# print("Verificando se um número é par ou impar\n")

# numero = int(input('Digite um número para verificar: '))

# if numero % 2 == 0:
#     print(f'O número {numero} é par.')
# else: 
#     print(f'O número {numero} é ímpar.')

# renda = float(input("Digite o valor da sua renda mensal: "))
# parcela = float(input("Digite o valor da parcela desejada: "))

# if renda > 2000 and parcela <= 0.3 * renda:
#     print("Empréstimo aprovado!")
# elif renda <= 2000:
#     print("Empréstimo negado: renda insuficiente.")
# else:
#     print("Empréstimo negado: parcela acima de 30% da renda.")


idade = 8
type(idade)