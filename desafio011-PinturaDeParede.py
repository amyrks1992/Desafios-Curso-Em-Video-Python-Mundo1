#PROGRAMA PINTURA DE PAREDE
'''
Faça um programa que leia a largura e altura de uma parede em metros, calcule
a sua área e a quantidadede tinta necessária para pintá-la, sabendo que cada
litro de tinta pinta 2m²
'''

print('PROGRAMA PINTURA DE PAREDE')
print('OBS: Cada litro de tinta pinta 2m².')

largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))

area = largura * altura

tinta = area/2

print('O valor da largura é {}m.\nO valor da altura é {}m.\n'
      'O valor da área é {:.2f}m².\nPortanto, sendo'
      'que o litro de tinta pinta 2m², você precisará'
      'de {} litros. '.format(largura,altura,area,tinta))

