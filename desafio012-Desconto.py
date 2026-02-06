#PROGRAMA DESCONTO
'''
Faça um algoritmo que leia o preço de um produto e mostre o seu novo valor
com 5% de desconto.
'''

print('PROGRAMA DESCONTO')
print('OBS: Desconto de 5%.')

preco = float(input('Digite o valor do produto: R$ '))
desconto = preco*(5/100)
#novo_preco = preco - (preco * 5/100)
novo_preco = preco - desconto

print('O valor do produto é {} reais.\nCom o desconto de {}%, o seu '
      'novo valor é {} reais.'.format(preco, desconto,novo_preco))
