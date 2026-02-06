# Desenvolva um programa que
# leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = int(input('Digite a sua primeira nota: '))
nota2 = int(input('Digite a sua segunda nota: '))

print('A sua 1ª nota foi {}. \n A sua 2ª nota foi {}. \n Portanto, a sua média é {}'
      .format(nota1,nota2, (nota1+nota2)/2))