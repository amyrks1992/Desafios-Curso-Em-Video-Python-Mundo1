'''
Faça um programa que leia um ano qualquer e mostre
se ele é BISSEXTO.
'''
from datetime import date
print('Digite 0 para saber se o ano atual é ou não BISSEXTO.')
ano = int(input('Digite um ano para saber se é ou não BISSEXTO: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))

else:
    print('O ano de {}, não é BISSEXTO.'.format(ano))