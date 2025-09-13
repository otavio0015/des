#faça um progama que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
numeros = [n1, n2, n3]
numeros_sort = sorted(numeros)
print('O maior valor é {}'.format(numeros_sort[2]))
print('O menor valor é {}'.format(numeros_sort[0]))

#concluido