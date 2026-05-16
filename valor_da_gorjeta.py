def gorjeta(valor, percentual):
    return valor * percentual

def valor_total(valor, gorjeta):
    return valor + gorjeta  

def main():
    try:
        print('+' * 40, 'FECHAMENTO DE CONTA' , '+' * 40 )
        valor = float(input('Digite o valor do consumo: '))
        percentual = float(input('Digite o percentual de gorjeta:'))/100
        valor_gorjeta = gorjeta(valor, percentual)
        total_pagar = valor_total(valor, valor_gorjeta)
        print(f'\nO valor da gorjeta é: R$ {valor_gorjeta:.2f}.')  
        print(f'O total a pagar é: R$ {total_pagar:.2f}.')  
    except ValueError:
        print('Atenção: Digite apenas números.')
        main()
    except NameError:
        print('\nTente novamente.')
        main()

try:
    main()
finally:
    print('\nEm caso de dúvidas, procure pelo gerente.')