'''
PROGRAMA ARREDONDAMENTO - TRUNCATE

016 - Crie um programa que leia um número real qualquer na tela pelo
teclado e mostre na tela a sua porção inteira.
'''

import math

num = float(input("Digite um número real: "))
num_arrend = math.trunc(num)

print("O número real é {}, e a sua porção inteira é {}".format(num,num_arrend))

