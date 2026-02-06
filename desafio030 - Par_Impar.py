'''
030 - Crie um program que leia um número inteiro e mostre
na tela se ele é PAR ou ÍMPAR.
'''

print('PROGRAMA PAR OU ÍMPAR')
print('Um número inteiro é um número sem vírgula.')

num = int(input('Digite um número inteiro para saber se ele é'
                ' PAR ou ÍMPAR: '))

if num % 2 == 0:
    print('O número {} é divisível por 2, então ele é PAR.'.format(num))
else:
    print('O número {} não é divisível por 2, então ele é ÍMPAR'
          '.'.format(num))

