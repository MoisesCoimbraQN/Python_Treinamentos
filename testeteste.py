# import csv
# import random

# nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]
# profissoes = ["Engenheiro", "Professor", "Médico", "Designer", "Advogado", "Programador", "Arquiteto", "Jornalista"]
# cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre", "Recife", "Salvador", "Brasília"]

# with open("dados.csv", "w", newline='', encoding="utf-8") as arquivo_csv:
#     escritor = csv.writer(arquivo_csv)                                              # Criando um objeto escritor para escrever no arquivo CSV
#     escritor.writerow(["nome", "idade", "profissao", "cidade"])                      # Cabeçalho

#     for _ in range(50):                                                                                                            
#         nome = random.choice(nomes)
#         idade = random.randint(18, 65)
#         profissao = random.choice(profissoes)
#         cidade = random.choice(cidades)
#         escritor.writerow([nome, idade, profissao, cidade])

# with open('dados.csv') as dados:
#     leitor_csv = csv.reader(dados, delimiter=',', quotechar='"')
#     next(leitor_csv)
#     for dado in dados:
#         print(dado)        

# dados_novos = [['Ana1' , 181 ,'Jornalista1111' ,'Curitiba2222'], 
#                ['xxx' , 181 ,'xxxxx' ,'xxxxxxx']]

# with open('dados.csv', 'a', newline='') as dados:
#     escritor_csv = csv.writer(dados, delimiter=',', quotechar='"')
#     for dado in dados_novos:
#         escritor_csv.writerow(dado)        

# import json

# #criando um dicionário de dicionários para usarmos como exemplo
# contatos = {
#     "Clark Kent":
#         {"Celular":"123456",
#          "Email":"super@krypton.com"},
#     "Bruce Wayne":
#         {"Celular":"654321",
#          "Email":"bat@caverna.com.br"}
# }

# #convertendo o dicionário para uma string o formato json
# contatos_json = json.dumps(contatos, indent=10)         

# #exibindo a string convertida
# print(contatos_json)

# arquivo = open('AgendaJson', 'w')
# arquivo.write(contatos_json)
# arquivo.close()

# print(type(contatos_json))


#convertendo json para dict
cotatos_dict= json.loads(contatos_json)

print(type(cotatos_dict))