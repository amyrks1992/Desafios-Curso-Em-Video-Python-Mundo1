#PROGRAMA CONVERSÃO EM DÓLAR
'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira,
e mostre quantos dólares ela pode comprar. Considere 1.00$ = 3.27'''

print('PROGRAMA CONVERSÃO EM DÓLAR')

valor = float(input('Digite quantos reais você tem na sua carteira: '))

dolar = valor/3.27

print('Você tem {} reais na sua carteira, Então pode comprar {:.2f} dólares.'
      .format(valor,dolar))






