'''
028 - Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deve escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint

num_pc = randint(0,5) #pc escolhe um numero entre 0 e 5

num_usuario = int(input('O pc escolheu um número de 0 à 5. Qual'
                        ' foi o número escolhido? '))

if num_usuario == num_pc:
    print('PARABÉNS, VOCÊ VENCEU! O número do pc foi {}.'.format(num_pc))
else:
    print('QUE PENA :(, VOCÊ PERDEU. O número do pc foi {}.'.format(num_pc))
