'''
022 - Crie um program que leia o nome completo
de uma pessoa e mostre:
O nome com todas as letras maiúsculas.
O nome com todas minúsculas.
Quantas letras ao todo sem contar os espaços.
Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o seu nome completo: ')).strip()#colcando strip aqui, eleima a chance
#espaços desnecessários.

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))





