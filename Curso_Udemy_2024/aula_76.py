import os
palavra_secreta = 'PERFUME'
letras_acertadas = ''
numero_tentativas = 10

while numero_tentativas > 0:
    letra_digitada = input('Digite uma letra: ').upper()

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra por vez.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    else:
        numero_tentativas -= 1
        print(f'Letra incorreta! Você tem {numero_tentativas} tentativas restantes.')
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada', palavra_formada)

if palavra_formada == palavra_secreta:
    print('Você ganhou!')
else:
    print('Você perdeu!')
