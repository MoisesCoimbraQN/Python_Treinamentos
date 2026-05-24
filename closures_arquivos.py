#-------------------------------#
# closure em funções

def multiplicar (multiplicador):                #função externa que retorna uma função interna que tem acesso a variável multiplicador
    def multiplo(numero):
        return multiplicador * numero
    return multiplo

duplicar = multiplicar(2)                       #a variável multiplicador recebe o valor 2 e guarda o valor 
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)

print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))

def multiplicar (multiplicador, numero):
    return multiplicador * numero

mult2 = multiplicar(2,3)
print(mult2)

#-------------------------------#
# Listas e arquivos

lista1 = [1,2,3,4]

print(lista1.index(5))
# print(lista1[-1])

vt_estado = ['AM', 'MG', 'RS', 'TO']

vt_estado.insert(2, 'SP')

print(vt_estado)
# print(type(vt_estado))


print(type(vt_estado[:2]))

#-------------------------------# 
# Manipulação de arquivos
#usando a função open para criar um objeto do tipo arquivo

arquivo = open("TesteArquivos.txt", "w", encoding='utf8')
print(arquivo.readline())   #leitura de linha
dados = '\nAdicionando texto ao arquivo'
arquivo.write(dados)
arquivo.close()    


import csv
import random

nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]
profissoes = ["Engenheiro", "Professor", "Médico", "Designer", "Advogado", "Programador", "Arquiteto", "Jornalista"]
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre", "Recife", "Salvador", "Brasília"]

with open("dados.csv", "w", newline='', encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)                                              # Criando um objeto escritor para escrever no arquivo CSV
    escritor.writerow(["nome", "idade", "profissao", "cidade"])                     # Cabeçalho

    for _ in range(50):                                                                                                            
        nome = random.choice(nomes)                                                  # Gerando um nome aleatório a partir da lista de nomes  (51 registros)                  
        idade = random.randint(18, 65)
        profissao = random.choice(profissoes)
        cidade = random.choice(cidades)
        escritor.writerow([nome, idade, profissao, cidade])

with open('dados.csv') as dados:
    leitor_csv = csv.reader(dados, delimiter=',', quotechar='"')
    next(leitor_csv)
    for dado in dados:
        print(dado)

dados_novos = [['Ana1' , 181 ,'Jornalista1111' ,'Curitiba2222'],             #adicionando novos dados a lista de dados_novos
               ['xxx' , 181 ,'xxxxx' ,'xxxxxxx']]

with open('dados.csv', 'a', newline='') as dados:
    escritor_csv = csv.writer(dados, delimiter=',', quotechar='"')
    for dado in dados_novos:
        escritor_csv.writerow(dado)

with open('dados.csv') as dados:
    leitor_csv = csv.reader(dados, delimiter=',', quotechar='"')
    next(leitor_csv)
    for dado in dados:
        print(dado)



#-------------------------------#
#  Manipulação de arquivos JSON

import json

#criando um dicionário de dicionários para usarmos como exemplo
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

#convertendo o dicionário para uma string o formato json
contatos_json = json.dumps(contatos, indent=4)           #a função dumps converte o dicionário para uma string no formato json 
                                                        #o parâmetro indent é usado para formatar a string com indentação de 4 espaços

#exibindo a string convertida
print(contatos_json)

arquivo = open('AgendaJson', 'w')
arquivo.write(contatos_json)
arquivo.close()

print(type(contatos_json))

#convertendo json para dict
cotatos_dict= json.loads(contatos_json)

print(type(cotatos_dict))

contato2 = {
    "Ana  Wayne":
        {"Celular":"651212124321",
         "Email":"bat@c51a31sd5f21s12averna.com.br"}
    }
contato2= json.dumps(contato2, indent=4)
arquivo2 = open('AgendaJson', 'w')
arquivo2.write(contato2)
arquivo2.close()


arquivo2 = open('AgendaJson', 'r')
conteudo_arquivo2 = arquivo2.read()
arquivo2.close()
print(conteudo_arquivo2)











