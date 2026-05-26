# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome222'

pessoa[chave] = 'Luiz Coimbra'
pessoa['sobrenome'] = 'Nascimento'
pessoa['profissao'] = 'Bancário'

print(pessoa[chave])

pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome222'])

#get
# print(pessoa.get('sobrenome')) # o get tenta achar a chave, 
#se nao achar passa para o prox sem interromper o cod
#por padrão é none se não encontrar
if pessoa.get('sobrenome') is None: 
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

del pessoa['profissao']
if pessoa.get('profissao') is None: 
    print('NÃO EXISTE')
else:
    print(pessoa['profissao'])

# print('ISSO Não vai')


# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
    'idade': 25
}

print(len(pessoa))    # Saída: 3 (tem 3 chaves)
print(pessoa.keys())  # Saída: dict_keys(['nome', 'sobrenome', 'idade'])
print(pessoa.values())# Saída: dict_values(['Aline', 'Souza', 25])

# O items traz os pares em formato de tuplas: (chave, valor)
print(pessoa.items()) # Saída: dict_items([('nome', 'Aline'), ...])

# .get() retorna None se a chave não existir, em vez de quebrar o código
print(pessoa.get('peso'))  # Saída: None
print(pessoa.get('peso', 'Não informado'))  # Saída: Não informado (valor padrão)

# .setdefault() checa se a chave existe. Se não existir, ele adiciona com o valor que você escolheu
pessoa.setdefault('altura', 1.70)
print(pessoa['altura'])  # Saída: 1.70

# .pop() remove a chave informada e te devolve o valor dela
nome_removido = pessoa.pop('nome')
print(nome_removido)  # Saída: Aline

# .popitem() apaga o ÚLTIMO item que foi adicionado ao dicionário
ultima_chave = pessoa.popitem() 

# .update() atualiza o dicionário. Ele adiciona novas chaves e atualiza as que já existem
pessoa.update({
    'idade': 26,       # Atualizou de 25 para 26
    'cidade': 'BH'     # Adicionou uma nova chave
})

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())



import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
# d2 = d1.copy() #copia rasa
# #os valores que são mutáveis no dicionário serão
# #afetados pelas mudanças feitas no variável atribuída

# d2['c1'] = 1000 #não muda
# d2['l1'][1] = 'lissta é mutável, cópia rasa' #muda

# print(d1)
# print(d2)

d3= copy.deepcopy(d1)

d3['c1'] = 1000 #não muda
d3['l1'][1] = 'lista é mutável, mas não muda na deepcopy'

print (d1)
print(d3)


# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro 
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
p1.update({
    'nome': 'novo valor',
    'idade': 30,
})
p1.update(nome='novo valor', idade=30)
tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)