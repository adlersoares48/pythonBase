'''Acordei = True
Fome = True

if Acordei and Fome:
    print('Eu faço meu café da manhã')
elif Acordei == True and Fome == False:
    print('Estou acordado, mas sem fome')
else:
    print('Estou dormindo')'''


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(10,11,3))