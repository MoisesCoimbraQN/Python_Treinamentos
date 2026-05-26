def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

saudacao_1 = criar_saudacao('Bom dia')
print(saudacao_1('Moises'))
saudacao_2 = criar_saudacao('Boa noite')
print(saudacao_2('Moises'))

#closure e funções que retornam outras funções 
#mesma lógica de função dentro de funcão adiando os argumentos 

def multiplicador(multiplicador):
    def multiplo(numero):
        return multiplicador * numero 
    return multiplo

duplicando = multiplicador(2)
triplicando = multiplicador(3)
quadruplicando = multiplicador(4)

print(duplicando(2))
print(triplicando(2))
print(quadruplicando(2))