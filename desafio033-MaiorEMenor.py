'''
033 - Faça um programa que leia três números e mostre
qual é o MAIOR e qual é o MENOR.
'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num2 > num3:
    print('O maior número é {}. E o menor é {}.'.format(num1,num3))

else:
    print('O maior número é {}. E o menor é {}.'.format(num3, num1))

'''
SEGUNDO CÓDIGO
Verificando quem é menor
menor = num1
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
    
Verificando quem é maior
menor = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
'''





