'''
024 - Crie um programa que leia o nome de uma cidade, e
diga se ela começa ou não com o nome 'SANTO'.
'''

cidade = str(input('Digite o nome de uma cidade: ')).strip()

print(cidade.find('Santo'))
#print(cidade[:5].upper() == 'SANTO') - isso garante que independente de como a pessoa escreva
#o tratamento vai dar certo, pois ela ficará em maiúscula antes da verificação.
