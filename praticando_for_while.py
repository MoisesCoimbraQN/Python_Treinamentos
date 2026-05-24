clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
for cliente in clientes:
    print('Cliente:', cliente)


contador = 0
while contador < 10:
    print("Processando dados...")
    contador += 1

mensagem = 'Bem-vindo ao Buscante'
for msg in range(5):
    print(mensagem)


valores = [10, 20, 30, 40, 50]
total = 0
for i in range(len(valores)):
    total = total + valores[i]
    print('Somando item', i+1)
print('O valor total das receitas é:', 'R$', total)

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
for projeto in projetos:
    if projeto is not None:
        print('-', projeto, 'é um projeto válido.')
    else:
        print('- projeto Ausente')

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
for livro in livros:
    if livro == "O Hobbit":
        print(f'Livro encontrado: {livro}')
        break   
print('Busca encerrada.')

estoque = 5
while estoque >0:
    estoque -= 1
    print(f'Venda realizada! Estoque restante: {estoque}.')
print('Estoque esgotado')

for i in range (10,0, -1):
    if i % 2 == 0:
        print(f'Faltam apenas {i} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {i} segundos restantes.')     
print ('Aproveite a promoção agora')         

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro['estoque'] >0:
        print(f'Livro disponível: {livro['nome']}')

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] == 0:
        continue
    print(f"Livro disponível: {livro['nome']}")


nome= ''
senha=''

while len(nome) < 5 or len(senha) < 8:
    nome = input('Digite o nome do usuário: ')
    senha = input('Digite a senha do usuário: ')
    if len(nome) < 5:
        print('Digite um nome com pelo menos 5 caracteres!')
        continue
    if len(senha) < 8 :
        print('Digite uma senha com pelo menos 8 caracteres')
        continue

    print (f'A senha para o usuário {nome} foi cadastrada com sucesso!')

