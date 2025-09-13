from time import sleep
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
opcao = 0

while opcao != 5:
        print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos numeros\n[ 5 ] Sair do progama')
        opcao = int(input('Digite a opção: '))
        print('-=' * 25)
        if opcao == 1:
            print(f'A soma de {valor1} com {valor2} é igual a {valor1 + valor2}')
        elif opcao == 2:
             print(f'A multiplicação de {valor1} com {valor2} é igual a {valor1 * valor2}')
        elif opcao == 3:
            if valor1 > valor2:
                print(f'O numero {valor1} é maior que o numero {valor2}')
            elif valor2 > valor1:
                print(f'O numero {valor2} é maior que o numero {valor1}')
            else:
                print(f'O numero {valor1} é igual a o numero {valor2}')
        elif opcao == 4:
            valor1 = int(input('Digite um valor: '))
            valor2 = int(input('Digite outro valor: '))
        elif opcao == 5:
            print('Finalizando...')
        else:
            print('Opção invalida, tente novamente.')
        print('-=' * 25)
        sleep(3)
print('FIM')

# concluido