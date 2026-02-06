#Escreva um programa que leia um valor em metros, e o exiba convertido em cm e mm.

metros = float(input('Digite um valor em metros: '))

cm = metros*100
mm = metros*1000

print('O valor digitado foi {} metros.\n O seu valor em centímetros é {} cm.\n'
      'E o seu valor em milímetros é {} mm'.format(metros,cm,mm))


