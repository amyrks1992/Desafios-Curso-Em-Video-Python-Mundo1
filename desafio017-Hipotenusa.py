'''
PROGRAMA HIPOTENUSA

017 - Faça um programa que leia o comprimento do cateto oposto,
 e do cateto adjacente de um triângulo retângulo. Calcule e
  mostre o comprimento da hipotenusa.
'''

'''
metodo sem importação
co = float(input("digite o valor do cateto oposto:"))
ca = float(input("digite o valor do cataeto adjaceste:"))
hip = co**2 + ca**2 **(1/2)

print(" A hipotenusa vai medir {:.2f}.".format(hip))
'''

import math

cat_oposto = float(input("digite o valor do cateto oposto:"))
cat_adjacente = float(input("digite o valor do cateto adjaceste:"))

hipo = math.hypot(cat_oposto,cat_adjacente)

print("A hipotenusa irá medir {:.2f}.".format(hipo))