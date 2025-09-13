#Escreva um progama que leia dois numeros enteiros e compare-os, mostrando na tela uma mensagem: O primeiro é maior. O segundo é maior. Nao existe valor maior. os dois sao iguais.
valor1 = int(input('Digite um numero: '))
valor2 = int(input('Digite mais um numero: '))
if valor1 > valor2:
    print('O primeiro é maior.')
elif valor1 < valor2:
    print('O segundo é maior.')
else:
    print('Não existe valor maior, os dois sao iguais.')

#concluido