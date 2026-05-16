texto = input('Digite um texto: ').split(' ') #separ o texto em palavras usando o método split, que por padrão separa por espaços
palavras = []
for palavra in texto:
    if len(palavra) >= 10:
        palavras.append(palavra)


if palavras:
    print('Palavras longas encontradas:\n')
    for palavra in palavras:
        print('  ', palavra, '   \n')
else:
    print('Seu texto não tem nenhuma palavra com mais de 10 caracteres! Se quiser reformule.')
