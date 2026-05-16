import random

letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maisculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
caracteres_especiais = '!@#$%¨&*()_+'

caratres = letras_maisculas+letras_minusculas+numeros+caracteres_especiais 

senha = []



import random
 

def gerar_senha():
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiais = "!@#$%&*"
 
    senha = [
        random.choice(maiusculas),  #choice singular
        random.choice(minusculas),
        random.choice(numeros),     
        random.choice(especiais)    
    ]
 
    todos_caracteres = maiusculas + minusculas + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8))      #choice plural, k é a quantidade de caracteres adicionais para a senha
    random.shuffle(senha)   #embaralha a senha para não ficar previsível
    return ''.join(senha)
 
print(f"Senha gerada: {gerar_senha()}")