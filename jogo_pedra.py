import random

print('***** JOGO PEDRA, PAPEL E TESOURA*****\n')
print('Escolha um item para jogar: R(Pedra), P(Papel), T(Tesoura). Para finalizar digite SAIR.\n')

while True: #laço para validar a entrada do usuário, garantindo que seja um número inteiro
    rodadas = input('Escolha a quantidade de rodadas: ')
    if rodadas.isdigit():
        rodadas = int(rodadas)
        print(f'Você escolheu {rodadas} rodadas.')
        break #sair do laço se a entrada for válida
    else:
        print('Entrada inválida! Digite apenas números inteiros.')


#função principal dojogo
def jogo():
    contador_rodadas = 0 #contador
    opcoes = ['R', 'P', 'T', 'SAIR'] #lista de opções válidas, incluindo a opção de sair do jogo
    pontos_jogador = 0
    pontos_computador = 0
    while contador_rodadas < rodadas:
        escolha_jogador = input("***** Digite sua escolha (R, P ou T)***** ").upper()
        print()
        escolha_computador = random.choice(opcoes)

        if escolha_jogador not in opcoes: #validação da escolha do jogador
            print(" As opções são R, P e T. Tente outra vez.\n")
            continue
            
        if escolha_jogador == 'SAIR': #condição para sair do jogo, mostrando o placar final
            if pontos_jogador > pontos_computador:
                print(f'PLACAR: {pontos_jogador} para Você X {pontos_computador} para o Computador\n')
                print(f'Jogo Finalizado! Você ganhou!')
            else:
                print(f'PLACAR: {pontos_jogador} para Você X {pontos_computador} para o Computador\n')
                print(f'Jogo Finalizado! Você Perdeu!')
            break
        
        
        if escolha_jogador == escolha_computador:
            print ('Empate. Você e o computador escolheram o mesmo item.\n')
            contador_rodadas +=1
        elif (escolha_jogador == 'R' and escolha_computador == 'T' or
            escolha_jogador == 'P' and escolha_computador == 'R' or
            escolha_jogador == 'T' and escolha_computador == 'P'):
            print('Você ganhou. Ponto para o você.\n')
            pontos_jogador += 1
            contador_rodadas +=1
        else:
            print('Você perdeu. Ponto para o computador.\n')
            pontos_computador += 1
            contador_rodadas +=1

    if pontos_jogador > pontos_computador: #condição para determinar o vencedor, mostrando o placar final sem sair do jogo, caso o número de rodadas seja atingido
        print(f'PLACAR: {pontos_jogador} para Você X {pontos_computador} para o Computador')
        print(f'Jogo Finalizado! Você ganhou!')
    elif pontos_jogador == pontos_computador:
        print(f'PLACAR: {pontos_jogador} para Você X {pontos_computador} para o Computador')
        print(f'Jogo Finalizado! Empate!')
    else:
        print(f'PLACAR: {pontos_jogador} para Você X {pontos_computador} para o Computador')
        print(f'Jogo Finalizado! Você Perdeu!')

jogo()