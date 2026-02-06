'''
020 - O mesmo professor do desafio anterior quer sortear a ordem
de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos 4 alunos e a ordem sorteada.
'''

import random

aluno01 = str(input('Digite o nome do primeiro aluno: '))
aluno02 = str(input('Digite o nome do segundo aluno: '))
aluno03 = str(input('Digite o nome do terceiro aluno: '))
aluno04 = str(input('Digite o nome do quarto aluno: '))

alunos =[aluno01,aluno02,aluno03,aluno04]

ordem = random.shuffle(alunos)

print("A ordem de apresentação será: ")
print(alunos)