#Operadores Aritimeticos: +(SOMA) -(SUBTRAÇÃO) *(MULTIPLICAÇÃO) /(DIVISÃO) //(DIVISÃO COM ARREDONDAMENTO) %(RESTO DA DIVISÃO) **(EXPONENCIAÇÃO)

#Operadores Lógicos: AND OR NOT

#Operadores Relacionais: ==(IGUAL) !=(DIFERENTE) >(MAIOR) <(MENOR) 

#Operadores de Atribuição: =(RECEBE) +=(VALOR + ELE MESMO = ALGO) -=(VALOR - ELE MESMO = ALGO) /=(VALOR / ELE MESMO = ALGO) *=(VALOR * ELE MESMO = ALGO)

'''num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
soma = num1 + num2
print(f'O resultado de {num1} + {num2} é {soma}')'''

print('Olá! Bem vindo a calculadora Soares!')
print('Selecione abaixo a opção de calculo desejada: \n(1)Adição\n(2)Subtração\n(3)Multiplicação\n(4)Divisão')
escolha = int(input('Opção: '))
while escolha < 1 or escolha > 4:
    print('Número invalido, tente novamente...')
    print('Selecione abaixo a opção de calculo desejada: \n(1)Adição\n(2)Subtração\n(3)Multiplicação\n(4)Divisão')
    escolha = int(input('Opção: '))
print('Agora digite os números desejados para realizar a equação')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if escolha == 1:
    soma = num1 + num2
    print(f'O resultado de {num1} + {num2} é igual a {soma}')
elif escolha == 2:
    subtrai = num1 - num2
    print(f'O resultado de {num1} - {num2} é igual a {subtrai}')
elif escolha == 3:
    mult = num1 * num2
    print(f'O resultado de {num1} x {num2} é igual a {mult}')
else:
    div = num1 / num2
    print(f'O resultado de {num1} / {num2} é igual a {div}')

print('Volte sempre!')