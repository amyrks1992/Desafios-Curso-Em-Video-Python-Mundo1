'''
- Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado.
A multa irá custar 7,00 reais para cada km acima do limite.
'''
import random

velocidade = int(input('Qual a velocidade do carro: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você ultrapassou o limite de velocidade, então '
          'receberá uma multa.')
    print('Para cada km acima é cobrado 7,00 reais, portando a '
          'sua multa foi de {} reais.'.format(multa))

else:
    print('Você está no limite de velocidade permitido.')