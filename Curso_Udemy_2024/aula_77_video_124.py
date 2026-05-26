#DICIONÁRIOS

pessoa = {}

chave1 = 'nome'
chave2 = 'sobrenome'
pessoa[chave1]= 'Moises'
pessoa[chave2] = 'Coimbra '
print(pessoa[chave2])

print(pessoa)

del pessoa[chave2]
print(pessoa)

if pessoa.get('sobrenome') is None:   #get pesquisa se uma chave existe no dict
    print ('Chave não existe no dict')
else:
    print(pessoa['sobrenome'])



print(pessoa.__len__()) #conta chaves

pessoa.setdefault('profissao', 'bancario') #inclui uma chave e um valor padrao no dict 

pessoa.items() #vai retornar uma tupla com chave e valor 
print(pessoa.items())

for chave, valor in pessoa.items():
    print(chave, valor)

print(pessoa['profissao']) 

pessoa_copia = pessoa.copy() # faz uma copia rasa do dict, mas os elementos variaveis ainda sofrem influencias das alterações(listas)

import copy
pessoa_copia = copy.deepcopy(pessoa) # aqui a copia é profunda e não ha interação entre os elementos variaveis

pessoa.update({
    'nome': 'lineker',
    'endereco': 'rua francisco sales'   
})

print(pessoa)

#tambem podemos fazer o update com 
pessoa.update(nome = 'Maria', profissao = 'gerente')
print(pessoa)


# Exercício: Quiz de Perguntas e Respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtde_acertos = 0 #variavel fora do for para ser utilizada no ambiente global e contabilizar os acertos
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])

    opcoes = pergunta['Opções']      #usando o enumerate para pegar o indice junto com a opção
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()
    
    escolha= input('Escola uma opção:')

    acertou= False
    escolha_int = None
    qtde_opcoes = len (opcoes)


    if escolha.isdigit():              #verificando se o dado digitado é um digito
        escolha_int = int(escolha)
    
    if escolha_int is not None:          #se o dado não for invalido 
        if escolha_int >= 0 and escolha_int < qtde_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:      #verificando se a opção escolhida é igual a resposta correta
                acertou = True                                   #se a resposta estiver correta, a variável acertou recebe True, caso contrário, permanece False                       

    if acertou:
        qtde_acertos += 1 #contando acertos
        print('Acertou')
    else: 
        print('Errou')

print ('Você acertou', qtde_acertos)
print ('de', len(perguntas), 'perguntas!')
    


