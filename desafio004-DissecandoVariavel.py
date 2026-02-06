#PROGRAMA DISSECANDO UMA VARIÁVEL#

a = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(a))
print('Esse valor só tem espaços? ', a.isspace())
print('Esse valor é um número?', a.isnumeric())
print('Esse valor é alfabético? ', a.isalpha())
print('Esse valor é alfanumérico? ', a.isalnum())
print('Esse valor está em maiúscula?', a.isupper())
