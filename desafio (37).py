#Escreva um progama que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao: 1 para binario. 2 para octal. 3 para hexadecimal.
numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma base para conversão:
[ 1 ] para BINARIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida. Tente novamente.')

#concluido