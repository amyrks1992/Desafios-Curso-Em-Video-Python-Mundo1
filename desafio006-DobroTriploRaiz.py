#PROGRAMA DOBRO, TRIPLO E RAIZ QUADRADA

num = int(input('Digite um número: '))

dobro = num*2
triplo = num*3
raiz = num**0.5
#num**(1/2)
# para formatar as casas decimais de um número -> :.numero de casasf
#\n -> quebra de linha

#print('O número é ', num, 'o seu dobro é ', dobro, 'o seu triplo é ', triplo
       #, ' e a sua raiz quadrada é ', raiz)

print('O número é {}. \n o seu dobro é {}. \n o seu triplo é {}. '
      '\n e a sua raiz quadrada é {:.2f}. '.format(num,dobro,triplo,raiz))