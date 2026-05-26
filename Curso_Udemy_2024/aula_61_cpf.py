# DEFININDO O PRIMEIRO DIGITO DO CPF
cpf = input('Digite o seu CPF (apenas números): ').replace('-', '').replace('.','')  #substituindo os caracteres '-' e '.' por uma string vazia usando o método replace
nove_primeiros_n = cpf[:9]
contador = 10

#Definindo o primeiro digito do CPF
"""
Multiplique cada um dos 9 primeiros dígitos do seu CPF por uma sequência decrescente de pesos, começando em \(10\) e indo até \(2\).
Some todos os resultados.
"""
resultado = 0 
for numero in nove_primeiros_n:
     resultado += int(numero) * contador #
     contador -= 1

"""
Divida o valor da soma por \(11\) e pegue o resto da divisão
Regra: Se o resto da divisão for menor que \(2\) (ou seja, \(0\) ou \(1\)), o 1º dígito verificador é \(0\). Caso contrário, o dígito é \(11\) menos o resto.
"""
digito1 = ((resultado)%11)
digito1 = digito1 if digito1 < 2 else 11 - digito1
print(digito1)

#DEFININDO O SEGUNDO DIGITO DO CPF
"""
Multiplique os 9 primeiros dígitos do CPF somados ao 1º dígito verificador recém-calculado por pesos decrescentes de \(11\) a \(2\).
Some todos os resultados e divida por \(11\) para obter o resto.
Regra: Novamente, se o resto da divisão for menor que \(2\), o 2º dígito verificador é \(0\). Caso contrário, o dígito é \(11\) menos o resto
"""

dez_primeiros_n = cpf[:10]
contador2 = 11

resultado2 = 0 
for numero2 in dez_primeiros_n:
    resultado2 += int(numero2) * contador2
    contador2 -= 1

digito2 = ((resultado2)%11)    
digito2 = digito2 if digito2 < 2 else 11 - digito2
print(digito2)

cpf_gerado = f'{nove_primeiros_n}{digito1}{digito2}'

print(cpf_gerado)

#validando os cpfs
if cpf == cpf_gerado:
     print(f'O CPF {cpf} é válido')
else:
     print('CPF inválido')

#metodos para limpar o cpf caso o usuário forneça dados alem de numeros 
#pode utilizar o metodo replace;
#pode importar 're" e utilizar, p exemplo: cfp = re.sub(r'[0-9], '', '746.824.890-70)
#voce pode implementar um codigo para verificar se o usuario esta inserindo n repetidos, por exemplo
# entrada_n_repetidos = entrada == entrada[0]*len(entrada), a entrada seia o input para digitar o cpf
