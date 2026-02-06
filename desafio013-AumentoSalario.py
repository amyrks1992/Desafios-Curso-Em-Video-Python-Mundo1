#PROGRAMA AUMENTO DE SALÁRIO
'''
Faça um programa que leia o salário de um funcionário e mostre o seu novo salário
com 15% de aumento.
'''

print('PROGRAMA AUMENTO DE SALÁRIO')
print('OBS: Aumento de 15%.')

salario = float(input('Digite o valor do seu salário: '))
aumento = salario *(15/100)

novo_salario = salario + aumento

print('O valor do salário é {} reais.\nCom o aumento de 15%,'
      'o novo valor será de {} reais.'.format(salario,novo_salario))

