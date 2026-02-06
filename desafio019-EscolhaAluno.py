'''
019 - Um professor quer sortear um dos seus quatro alunos para
apagar o quadro. Faça um programa que ajude ele. Lendo o nome deles
e o nome escolhido.
'''

import random

aluno_01 = input("Digite o nome do primeiro aluno: ")
aluno_02 = input("Digite o nome do segundo aluno: ")
aluno_03 = input("Digite o nome do terceiro aluno: ")
aluno_04 = input("Digite o nome do quarto aluno: ")

alunos = [aluno_01,aluno_02,aluno_03,aluno_04]

escolhido = random.choice(alunos)

print( "o aluno escolhido foi {}.".format(escolhido))