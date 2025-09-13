#crie um algoritmo que leia um numero e mostre o seu dobro, tripo e raiz quadrada
numero = int(input('digite um numero: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print('o dobro de {} é {}\no triplo é {}\na raiz quadrada é {:.2f}'.format(numero, dobro, triplo, raiz))
#concluido