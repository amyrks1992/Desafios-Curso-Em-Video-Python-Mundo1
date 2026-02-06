'''
PROGRAMA SENO, COSSENO, TANGENTE
018 - Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math

angulo = float(input("Digite um angulo:"))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O angulo é {:.2f}. O seu seno é {:.2f}, o seu cosseno é {:.2f} "
      "e a sua tangente é {:.2f}."
      .format(angulo,seno,cosseno,tangente))