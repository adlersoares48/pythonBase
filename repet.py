'''for letra in 'Adler':
    print(letra)'''

'''palavra = 'Adler'
for letra in palavra:
    print(letra)'''


for index in range(5):
    if index == 0:
        print('Primeira linha')
    elif index == 2:
        print('É a terceira linha')
    else:
        print('Não é a primeira linha')

amigos = ['João', 'Pedro', 'Leonardo', 'Henrique']
for amigo in range(len(amigos)):
    print(f'{amigo} - {amigos[amigo]}')