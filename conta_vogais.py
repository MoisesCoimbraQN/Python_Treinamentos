
frase = input('Digite sua frase para a contagem das vogais: ')
vogais = ['a', 'e', 'i', 'o', 'u']

def limpa_texto(frase):
    simbolos = ",.!|?;:''()[]{}áéíóúãõâêôçÁÉÍÓÚÃÕÂÊÔÇ"
    for simbolo in simbolos:
        frase = frase.replace(simbolo, "") #removendo os simbolos da frase usando o método replace, que substitui um caractere por outro, nesse caso por uma string vazia
    frase = list(frase.lower()) #quebrando a frase em uma lista de caracteres usando o método list
    vogais_frase=[]
    for i in range(len(frase)):
        if frase[i] in vogais:
            vogais_frase.append(frase[i])
            #print(f'Vogal encontrada: {frase[i]}')
    return vogais_frase

def contador_vogais(frase):
    vogais_frase = limpa_texto(frase)
    qtde_vogais = {}
    for vogal in vogais_frase:
        qtde_vogais[vogal] = qtde_vogais.get(vogal, 0) +1
    return qtde_vogais
    
for chave, items in contador_vogais(frase).items():
    print(f"A vogal '{chave.upper()}' aparece {items} vezes na frase '{frase.upper()}'.")