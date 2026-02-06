'''
034 - Escreva um program que pergunte o salário de um
funcionário e calcule o valor do seu aumento.
Para salários superiores à R$1250,00, calcule um aumento
de 10%.
Para os inferiores ou iguais o aumento será de 15%.
'''

salario = float(input('Digite o valor do seu salário: '))
aumento01 = (salario * 10/100) + salario
aumento02 = (salario * 15/100) + salario

if salario > 1250:
    print('Como o seu salário é de {}, o seu aumento será de'
          ' 10%. O seu novo salário será de {}.'.format(salario,aumento01))
else:
    print('Como o seu salário é de {}, o seu aumento será de'
          ' 15%. O seu novo salário será de {}.'.format(salario, aumento02))
