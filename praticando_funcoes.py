

# def calcula_idade (ano_nascimento=None, ano_atual=None):
#     ano_nascimento = int(input('Digite o ano de nascimento: '))
#     ano_atual = int(input('Digite o ano atual: '))
#     return ano_atual - ano_nascimento

# idade = calcula_idade()    
# print(f' A idade é {idade} anos.')

# def conta_caracteres(palavra):
#     return len(palavra)

# palavra = input('Digite a palavra para contar os caracteres: ')
# contador = conta_caracteres(palavra)
# print(contador)

# def saudacao(hora):
#     if hora < 12:
#         return 'Bom dia!'
#     if 12 <= hora <= 18:
#         return 'Boa tarde!'
#     return 'Boa noite!'

# hora = int(input('Digite a hora: '))
# print(saudacao(hora))

# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
# numero_convertido  = []

# def conversor_int(lista):
#     for numero in lista:
#         return numero_convertido.append(int(numero))

# def verifica_conversao (lista):
#     for numero in lista:
#         if not isinstance(numero, int):
#             return 'Erro na conversão'
#         return 'Conversão efetuada com sucesso!'

# conversor_int(telefones)
# print(verifica_conversao(numero_convertido))

# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
# def teste(telefones):
#     for i, numero in enumerate(telefones):
#         print(f"Telefone {i}: {numero}")

# teste(telefones)


# valores = input("Digite os valores das vendas: ").split()
# print(valores)
# def soma_valores(valores):
#     total = 0
#     for numero in valores:
#         numero = int(numero)
#         total = total + numero
#     return f' O total das vendas foi {total}'
# print(soma_valores(valores))

# #solução do instrutor

# valores = input("Digite os valores das vendas: ").split() 
# total = sum(map(float, valores)) 
# print(f"O total de vendas foi: {total}") 



# valores = input("Digite os valores das vendas: ").split()

# def numeros_pares(lista):
#     valores_pares = []
#     for numero in lista:
#         numero = int(numero)
#         if numero % 2 == 0:
#             valores_pares.append(numero)
#     return valores_pares
# print(numeros_pares(valores))

# exibir_pares = list(filter(numeros_pares, valores_pares))
# print(exibir_pares)

# valores = input("Digite os valores das vendas: ").split()
# pares = filter(lambda x: int(x) % 2 ==0, valores)
# print("Números pares:", " ".join(pares)) 


# produtos = input("Digite os produtos: ").split()
# valores = input("Digite os valores: ").split()

# def lista_completa (produto, valor):
#     return f' {produto} : {valor}'

# for produto, valor in zip(produtos, valores):
#     print(lista_completa(produto, valor))


# x = int(input('Digite o primeiro numero: '))
# y = int(input('Digite o segundo numero: '))
# tc = input('Escolha a operação (| + | - | * | / |): ')
# resultado = (lambda x, y: x+y if tc == '+' else x-y if tc == '-' else  x*y if tc =='*' else x/y)
# print(resultado(x, y))

# #closure
# def valor_com_desconto (taxa):
#     def valor_item ( valor):
#         return  f'O valor a pagar, com o desconto, é de R$ {valor - valor * taxa}'
#     return valor_item

# valor = int(input('Digite o valor da compra: '))
# taxa = int(input('Digite a porcentagem de desconto: '))/100
# desconto = valor_com_desconto(taxa)
# valor_inteiro  = desconto(valor)
# print(valor_inteiro )

#recursivas
# def somatorio (n):
#     if n == 1:
#         return 1
#     return n + somatorio(n-1) 

# numero = int(input("Digite um número: ")) 
# print(f"A soma de 1 a {numero} é: {somatorio(numero)}")

# lista = ['a', 'b', 'c']
# listab = []


# for i, item in enumerate(lista):
#     item2 = lista[i]*2 
#     listab.append(item2)

# print(listab)



