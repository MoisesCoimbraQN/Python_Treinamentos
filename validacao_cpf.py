

print('#'*30, 'VALIDADOR DE CPF', '#'*30)

def valida_cpf(numero):
    try:
        if numero.isdigit() and len(numero) == 11:
            return f'\nO CPF {numero[0:3]}.{numero[3:6]}.{numero[6:9]}-{numero[9:]} é válido.\n'
        else:
            return 'Digite apenas números' if numero.isdigit() == False else 'Verifique se o número digitado tem 11 dígitos.'
    except ValueError:
        print('Digite apenas números.')
        
numero = input('Digite seu CPF: ')
print(valida_cpf(numero))
