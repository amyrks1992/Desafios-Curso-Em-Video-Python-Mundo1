'''
035 - Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou não
formar um triângulo.
'''

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 + reta2 > reta3:

    if reta1 + reta3 > reta2:

        if reta2 + reta3 > reta1:
            print('Como a soma de duas retas é menor que a terceira,'
          'então elas podem formam um triângulo. ')

else:
    print('Como a soma de duas retas é menor que a terceira,'
          'então elas não formam um triângulo. ')